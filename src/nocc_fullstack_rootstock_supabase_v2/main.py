import os
from dotenv import load_dotenv
from .crew import NoccFullstackRootstockSupabaseCrewV2

load_dotenv()  # This loads the variables from .env

def run():
    if 'ANTHROPIC_API_KEY' not in os.environ:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    os.environ['OPENAI_API_KEY'] = os.environ['ANTHROPIC_API_KEY']

    crew = NoccFullstackRootstockSupabaseCrewV2()

    project_name = input("Enter the name for your project: ")
    project_type = input("Enter the type of project (e.g., NFT marketplace, DeFi app): ")
    contract_requirements = input("Describe the requirements for your smart contract: ")
    frontend_requirements = input("Describe the requirements for your frontend: ")

    result = crew.run(project_name, project_type, contract_requirements, frontend_requirements)
    print("Project components generated:")
    print(result)

if __name__ == "__main__":
    run()