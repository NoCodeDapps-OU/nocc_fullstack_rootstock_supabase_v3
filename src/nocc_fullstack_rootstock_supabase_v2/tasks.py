from crewai import Task

class SmartContractTasks:
    @staticmethod
    def generate_contract(agent, requirements):
        return Task(
            description=f"Generate a Solidity smart contract for Rootstock based on the following requirements: {requirements}",
            agent=agent,
            expected_output="A complete Solidity smart contract code that fulfills the user's requirements for Rootstock."
        )

    @staticmethod
    def generate_tests(agent, contract):
        return Task(
            description=f"Generate a comprehensive test suite for the Rootstock smart contract: {contract}",
            agent=agent,
            expected_output="A set of thorough test cases covering all functions and edge cases of the smart contract, written in JavaScript for Mocha and Chai."
        )

class FrontendTasks:
    @staticmethod
    def design_frontend(agent, requirements):
        return Task(
            description=f"Design and implement the frontend structure using HTML and Tailwind CSS based on the following requirements: {requirements}",
            agent=agent,
            expected_output="Complete HTML structure with Tailwind CSS classes for the frontend."
        )

class BackendTasks:
    @staticmethod
    def setup_supabase(agent, project_details):
        return Task(
            description=f"Set up a Supabase project and create the necessary database structure for: {project_details}",
            agent=agent,
            expected_output="Detailed instructions for setting up Supabase project and database structure."
        )