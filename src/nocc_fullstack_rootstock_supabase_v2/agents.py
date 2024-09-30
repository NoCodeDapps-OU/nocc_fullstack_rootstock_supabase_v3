from crewai import Agent

class SmartContractAgents:
    def contract_designer(self):
        return Agent(
            role='Smart Contract Designer',
            goal='Design and implement Solidity smart contracts for Rootstock based on user requirements',
            backstory='You are an expert Solidity developer with years of experience in designing secure and efficient smart contracts for Rootstock.',
            verbose=True,
            allow_delegation=False,
            llm='claude-3-sonnet-20240229'
        )

    def contract_tester(self):
        return Agent(
            role='Smart Contract Tester',
            goal='Create comprehensive test suites for Rootstock smart contracts',
            backstory='You are a meticulous QA engineer specializing in blockchain technology and Rootstock smart contract testing.',
            verbose=True,
            allow_delegation=False,
            llm='claude-3-sonnet-20240229'
        )

class FrontendAgents:
    def frontend_designer(self):
        return Agent(
            role='Frontend Designer',
            goal='Design and implement the frontend structure using HTML and Tailwind CSS',
            backstory='You are an expert frontend designer with years of experience in creating beautiful and responsive web interfaces.',
            verbose=True,
            allow_delegation=False,
            llm='claude-3-sonnet-20240229'
        )

class BackendAgents:
    def supabase_integrator(self):
        return Agent(
            role='Supabase Backend Integrator',
            goal='Design and implement Supabase backend integration',
            backstory='You are an expert in backend development with extensive experience in Supabase integration.',
            verbose=True,
            allow_delegation=False,
            llm='claude-3-sonnet-20240229'
        )