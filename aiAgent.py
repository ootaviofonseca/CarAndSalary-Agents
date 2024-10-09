from langchain import hub 
from langchain.agents import Tool, create_react_agent, create_openai_tools_agent    
from langchain_openai import ChatOpenAI
from cars import CarData, AllCarsData
from employee import EmployeeData, EmployeeInstallmentCalculator

import os
from dotenv import load_dotenv

load_dotenv()

class AgenteOpenAIFunctions:
    def __init__(self):
        llm = ChatOpenAI(
            model = "gpt-3.5-turbo",
            api_key = os.getenv("OPENAI_API_KEY")
        )

        # Tools creation
        car_data = CarData()
        all_cars_data = AllCarsData()
        employee_data = EmployeeData()
        employee_maximum_expense = EmployeeInstallmentCalculator()

        self.tools = [ #Tools list
        Tool(name = employee_data.name,
            func = employee_data.run,
            description = employee_data.description,
            return_direct = False 
            ),
        Tool(name = employee_maximum_expense.name,
            func = employee_maximum_expense.run,
            description = employee_maximum_expense.description,
            
            ),
        Tool(name = car_data.name,
            func = car_data.run,
            description =  car_data.description,
            
            ),
        Tool(name = all_cars_data.name,
            func = all_cars_data.run,
            description = all_cars_data.description,
            
            ),

        ]
        # openai functions
        prompt = hub.pull("hwchase17/openai-functions-agent")
        self.agent = create_openai_tools_agent (llm,self.tools, prompt)

        #react
        #prompt = hub.pull("hwchase17/react") 
        #self.agent = create_react_agent(llm, self.tools, prompt)