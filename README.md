# AI Car and Employee Financial Assistant

![Python](https://img.shields.io/badge/Python%2B-%2312343D.svg?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-%23008080.svg?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-%23000.svg?style=for-the-badge&logo=openai&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![dotenv](https://img.shields.io/badge/dotenv-%2300FF99.svg?style=for-the-badge&logo=.env&logoColor=white)

## Project Overview

This project is an AI-powered assistant that helps users make financial decisions related to cars based on their salaries. By using **OpenAI**'s API, the system can answer various queries, such as the maximum car installment an employee can afford based on their salary or recommending cars that fit within a person's budget.

## Features

- Extract employee salary data and calculate the maximum amount they can afford for monthly car installments.
- Fetch car data such as price and model details.
- Provide recommendations for cars that fit within the financial constraints of a given employee.
- Answer financial questions using **OpenAI**'s large language models with integrated **LangChain** tools.

## Technologies

- **Python**: The core programming language used to build the application.
- **LangChain**: Orchestrates the interaction between the user queries and the AI models/tools.
- **OpenAI API**: Provides the language model used to process and generate natural language responses.
- **Pandas**: Manages and processes data related to employee salaries and car prices.
- **dotenv**: Manages environment variables for securely handling API keys.

## Getting Started

1. Clone this repository to your local machine.
2. Install the necessary dependencies listed in the `requirements.txt` file.
3. Set up your `.env` file with your **OpenAI API Key**:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```
4. Run the `main.py` file to start the application.

## File Structure

- **main.py**: The main script where user queries are handled and processed.
- **agent.py**: Defines the AI agent, combining OpenAI tools and LangChain for query processing.
- **employee.py**: Handles employee salary data and computes maximum car installment affordability.
- **cars.py**: Handles car data, including fetching car prices and details.

## How It Works

1. The user provides a query related to cars or employee finances (e.g., "What is the most expensive car Boris Gibson can afford?")
2. The system extracts relevant data from CSV files using **Pandas**.
3. The **LangChain** agent orchestrates the interaction between tools that handle the logic for employee salary or car data.
4. **OpenAI's GPT** model processes natural language queries and provides the appropriate response.


![image](https://github.com/user-attachments/assets/23b8beca-7b6a-4353-b6c4-6a501aad5209)

