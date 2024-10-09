
import json
from typing import List
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import os
import pandas as pd

def find_employee_data(employee):
    data = pd.read_csv("data/Employee_monthly_salary.csv")

    #find the employee data by Name 
    this_employee_data = data[data["Name"].str.lower() == employee]
    
    if this_employee_data.empty:
        return {}
    
    return this_employee_data.iloc[:1].to_dict()

class EmployeeExtractor(BaseModel):
    employee: str = Field("Employee name,  in lowercase letters..")

class EmployeeData(BaseTool):
    name = 'EmployeeData'
    description = """
    This tool extracts the employee's name and salary and makes a summary of what they do at work
    Pass the employee's name as an argument to this tool
    """

    def _run (self, input: str) -> str:
        llm = ChatOpenAI(
            model = "gpt-3.5-turbo",
            api_key = os.getenv("OPENAI_API_KEY")
        )

        parser =  JsonOutputParser(
            pydantic_object = EmployeeExtractor,
        )
        template = PromptTemplate(
                        template="""You must analyze the following entry and extract the employee's name given in lowercase.
                
                        Input:
                        -----------------
                        {input}
                        -----------------

                        Output Format:
                        {output_format}
                        """,
                        input_variables = ["input"],
                        partial_variables = {"output_format" : parser.get_format_instructions()}
                        )
        
        chain = template | llm | parser 
        answer = chain.invoke({"input": input})
        employee =answer['employee']

     
        employee = employee.lower().strip()
        data = find_employee_data(employee)
        
        print(data)
        return json.dumps(data) #create a json object from the data dictionary


def find_employee_maximum_expense(employee):
    data = pd.read_csv("data/Employee_monthly_salary.csv")
    data = data[data["Name"].str.lower() == employee]
    if data.empty:
        return {}
    
    data = data.iloc[:1]
    salary = data["GROSS"].values[0]
    return salary * 0.1

class EmployeeInstallmentCalculator(BaseTool):
    name = 'EmployeeInstallmentCalculator'
    description = """
    This tool calculates the maximum installment an employee can afford based on their salary.
    Pass the employee's name as an argument to this tool.
    """

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY")
        )

        parser = JsonOutputParser(
            pydantic_object=EmployeeExtractor,
        )
        template = PromptTemplate(
            template="""You must analyze the following entry and extract the employee's firts and last name given in lowercase.

            Input:
            -----------------
            {input}
            -----------------

            Output Format:
            {output_format}
            """,
            input_variables=["input"],
            partial_variables={"output_format": parser.get_format_instructions()}
        )

        chain = template | llm | parser
        answer = chain.invoke({"input": input})
        employee = answer['employee']

        employee = employee.lower().strip()
        max_expense = find_employee_maximum_expense(employee)

        return json.dumps({"employee": employee, "maximum_installment": max_expense})
    