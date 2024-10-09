from langchain.agents import AgentExecutor
from aiAgent import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

#pergunta = input(": ")

question = "Qual salario de Keven Norman?"
question = "How much can Keven Norman spend on one installment?"
question = "Qual carro mais caro?"
question = "Baseado no salario de Keven Norman, qual o maximo que ele pode gastar em uma parcela de carro?"
question = "Indique carros que cabem no bolso de Donte Richard?"
question = "Qual carro mais caro e o valor da parcela para Boris Gibson?"
question = "Boris Gibson precisaria parcelar de quantas vezes a Silverado ano 2020?"

agent = AgenteOpenAIFunctions()
executor = AgentExecutor(
    agent = agent.agent, 
    tools = agent.tools, 
    verbose=False,
    handle_parsing_errors=True)


resposta = executor.invoke({"input" : question})
print(resposta)