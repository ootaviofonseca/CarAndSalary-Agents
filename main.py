from langchain.agents import AgentExecutor
from aiAgent import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

question = "Qual salario de Keven Norman?"
question = "How much can Keven Norman spend on one installment?"
question = "Qual carro mais caro?"
question = "Baseado no salario de Keven Norman, qual o maximo que ele pode gastar em uma parcela de carro?"
question = "Qual carro mais caro e o valor da parcela para Boris Gibson?"
question = "Boris Gibson precisaria parcelar de quantas vezes a Silverado ano 2020?"
question = "Indique carros que cabem no bolso de Donte Richard "

question = "Quais carros com milhagem até 50000 que Donte Richard pode comprar?"


agent = AgenteOpenAIFunctions()
executor = AgentExecutor(
    agent = agent.agent, 
    tools = agent.tools, 
    verbose=True,
    handle_parsing_errors=True)


resposta = executor.invoke({"input" : question})
print(resposta['output'])