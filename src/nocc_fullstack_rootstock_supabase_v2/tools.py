from crewai.tools import tool
from .utils.rootstock_helpers import (
    setup_project_structure,
    generate_rootstock_contract,
    generate_rootstock_tests,
    validate_rootstock_contract,
    save_contract,
    save_tests,
    validate_rootstock_tests
)
from .utils.frontend_helpers import (
    generate_html_css,
    generate_javascript,
    integrate_web3js,
    integrate_contract,
    save_frontend
)
from .utils.backend_helpers import (
    setup_supabase,
    generate_backend_code,
    save_backend_code
)

class RootstockProjectSetup:
    @tool("Setup Rootstock project structure")
    def setup_project(project_name: str) -> str:
        """Sets up a new project structure for Rootstock smart contract development."""
        return setup_project_structure(project_name)

class RootstockContractGenerator:
    @tool("Generate Rootstock smart contract")
    def generate_contract(requirements: str) -> str:
        """Generates a Rootstock smart contract based on the given requirements."""
        return generate_rootstock_contract(requirements)

class RootstockTestGenerator:
    @tool("Generate Rootstock contract tests")
    def generate_tests(contract: str) -> str:
        """Generates a comprehensive test suite for a given Rootstock smart contract."""
        return generate_rootstock_tests(contract)

class ContractValidator:
    @tool("Validate Rootstock smart contract")
    def validate_contract(contract: str) -> str:
        """Validates a given Rootstock smart contract for correctness and security."""
        return validate_rootstock_contract(contract)
    
class TestValidator:
    @tool("Validate Rootstock contract tests")
    def validate_tests(tests: str) -> str:
        """Validates the given Rootstock contract test suite for completeness and correctness."""
        return validate_rootstock_tests(tests)

class ProjectFinalizer:
    @tool("Finalize Rootstock project")
    def finalize_project(project_name: str, contract: str) -> str:
        """Finalizes the Rootstock smart contract project, saving all components."""
        contract_result = save_contract(project_name, contract)
        tests = generate_rootstock_tests(contract)
        tests_result = save_tests(project_name, tests)
        return f"Project finalized. {contract_result} {tests_result}"

class FrontendTools:
    @tool("Generate HTML and Tailwind CSS")
    def generate_html_css(requirements: str) -> str:
        """Generates HTML structure with Tailwind CSS classes based on the given requirements."""
        return generate_html_css(requirements)

    @tool("Generate JavaScript")
    def generate_javascript(html_structure: str) -> str:
        """Generates JavaScript code based on the given HTML structure."""
        return generate_javascript(html_structure)

class Web3Tools:
    @tool("Integrate Web3.js")
    def integrate_web3js(frontend_code: str) -> str:
        """Integrates Web3.js components into the given frontend code for Rootstock interaction."""
        return integrate_web3js(frontend_code)

class ContractIntegrationTools:
    @tool("Integrate Smart Contract")
    def integrate_contract(frontend_code: str, contract: str) -> str:
        """Integrates the given Rootstock smart contract with the frontend code."""
        return integrate_contract(frontend_code, contract)

    @tool("Save Frontend")
    def save_frontend(project_name: str, html_content: str, css_content: str, js_content: str, web3js_content: str) -> str:
        """Saves the frontend code to the project directory."""
        return save_frontend(project_name, html_content, css_content, js_content, web3js_content)
    
class BackendTools:
    @tool("Setup Supabase")
    def setup_supabase(project_details: dict) -> str:
        """Sets up a Supabase project and creates the necessary database structure."""
        return setup_supabase(project_details)

    @tool("Generate Backend Code")
    def generate_backend_code(project_details: dict, supabase_setup: str) -> str:
        """Generates backend code for Supabase integration based on the project details and setup."""
        return generate_backend_code(project_details, supabase_setup)

    @tool("Save Backend Code")
    def save_backend_code(project_name: str, backend_code: str) -> str:
        """Saves the generated backend code to the project directory."""
        return save_backend_code(project_name, backend_code)