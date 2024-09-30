import os
from crewai import Crew, Process
from .agents import SmartContractAgents, FrontendAgents, BackendAgents
from .tasks import SmartContractTasks, FrontendTasks, BackendTasks

class NoccFullstackRootstockSupabaseCrewV2:
    def __init__(self):
        self.smart_contract_agents = SmartContractAgents()
        self.frontend_agents = FrontendAgents()
        self.backend_agents = BackendAgents()

    def run(self, project_name, project_type, contract_requirements, frontend_requirements):
        project_details = {
            "project_name": project_name,
            "project_type": project_type,
            "frontend_requirements": frontend_requirements
        }

        # Smart Contract Tasks
        contract_design_task = SmartContractTasks.generate_contract(self.smart_contract_agents.contract_designer(), contract_requirements)
        test_generation_task = SmartContractTasks.generate_tests(self.smart_contract_agents.contract_tester(), "{result.contract_design_task}")

        # Frontend Tasks
        frontend_design_task = FrontendTasks.design_frontend(self.frontend_agents.frontend_designer(), frontend_requirements)
        
        # Backend Tasks
        backend_setup_task = BackendTasks.setup_supabase(self.backend_agents.supabase_integrator(), project_details)

        crew = Crew(
            agents=[
                self.smart_contract_agents.contract_designer(),
                self.smart_contract_agents.contract_tester(),
                self.frontend_agents.frontend_designer(),
                self.backend_agents.supabase_integrator()
            ],
            tasks=[
                contract_design_task,
                test_generation_task,
                frontend_design_task,
                backend_setup_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result