
import json
from typing import List
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import os
import pandas as pd


def find_car_data(car: str):
    data = pd.read_csv("data/CarPricesPrediction.csv")

    data["Model"] = data["Model"].str.lower()  
    this_car_data = data[data["Model"] == car.lower()]  


    if this_car_data.empty:
        return {}
    
    return this_car_data.iloc[:1].to_dict()

def find_all_cars_data():
    data = pd.read_csv("data/CarPricesPrediction.csv")
    return data.to_dict()

class CarExtractor(BaseModel):
    car:str = Field("Car model in lowercase letters.")

class CarData(BaseTool):
    name = "CarData"
    description = """This tool extracts data from a car.
    Pass the car model as an argument to this tool."""

    def _run(self, input:str) -> str:
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=CarExtractor)
        template = PromptTemplate(template="""You must analyze the following INPUT and extract the car name given in lower case.
        INPUT:
        -----------------
        {input}
        -----------------
                        Output Format:
                        {output_format}""",
                        input_variables=["input"],
                        partial_variables={"output_format" : parser.get_format_instructions()})
        chain = template | llm | parser
        answer = chain.invoke({"input" : input})
        car = answer['car']
        car = car.lower().strip()
        data = find_car_data(car)
        return json.dumps(data)

class AllCarsData(BaseTool):
    name="AllCarsData"
    description="""Loads data from all cars. No input parameters are required."""
    
    def _run(self, input:str):
        universidades = find_all_cars_data()
        return universidades
