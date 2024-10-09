from langchain.agents import AgentExecutor
from aiAgent import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

#pergunta = input(": ")

pergunta = "Qual salario de Keven Norman?"
pergunta = "How much can Keven Norman spend on one installment?"
pergunta = "Qual carro mais caro?"
pergunta = "Baseado no salario de Keven Norman, qual o maximo que ele pode gastar em uma parcela de carro?"
pergunta = "Indique carros que cabem no bolso de Donte Richard?"

pergunta = "Qual carro mais caro e o valor da parcela para Boris Gibson?"

pergunta = "Boris Gibson precisaria parcelar de quantas vezes a Silverado ano 2020?"

agent = AgenteOpenAIFunctions()
executor = AgentExecutor(
    agent = agent.agent, 
    tools = agent.tools, 
    verbose=True,
    handle_parsing_errors=True)



resposta = executor.invoke({"input" : pergunta})
print(resposta)