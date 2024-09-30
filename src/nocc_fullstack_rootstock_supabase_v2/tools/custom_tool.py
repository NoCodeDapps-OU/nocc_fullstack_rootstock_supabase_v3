from crewai_tools import Tool
from ..utils.rootstock_helpers import (
    setup_project_structure,
    generate_rootstock_contract,
    generate_rootstock_tests,
    validate_rootstock_contract,
    save_contract,
    save_tests,
    validate_rootstock_tests
)
from ..utils.frontend_helpers import (
    generate_html_css,
    generate_javascript,
    integrate_web3js,
    integrate_contract,
    save_frontend
)
from ..utils.backend_helpers import (
    setup_supabase,
    generate_backend_code,
    save_backend_code
)

# Rootstock Project Tools
def setup_project(project_name: str) -> str:
    return setup_project_structure(project_name)

setup_project_tool = Tool(
    name="Setup Rootstock Project",
    description="Sets up a new project structure for Rootstock smart contract development. Requires project_name as input.",
    func=setup_project
)

def generate_contract(args):
    requirements = args.get('requirements', '')
    return generate_rootstock_contract(requirements)

generate_contract_tool = Tool(
    name="Generate Rootstock Contract",
    description="Generates a Rootstock smart contract based on the given requirements.",
    func=generate_contract
)

def generate_tests(args):
    contract = args.get('contract', '')
    return generate_rootstock_tests(contract)

generate_tests_tool = Tool(
    name="Generate Rootstock Tests",
    description="Generates a comprehensive test suite for a given Rootstock smart contract.",
    func=generate_tests
)

def validate_contract(contract: str) -> str:
    return validate_rootstock_contract(contract)

validate_contract_tool = Tool(
    name="Validate Rootstock Contract",
    description="Validates a given Rootstock smart contract for correctness and security.",
    func=validate_contract
)

def validate_tests(tests: str) -> str:
    return validate_rootstock_tests(tests)

validate_tests_tool = Tool(
    name="Validate Rootstock Tests",
    description="Validates the given Rootstock contract test suite for completeness and correctness.",
    func=validate_tests
)

def finalize_project(project_name: str, contract: str) -> str:
    contract_result = save_contract(project_name, contract)
    tests = generate_rootstock_tests(contract)
    tests_result = save_tests(project_name, tests)
    return f"Project finalized. {contract_result} {tests_result}"

finalize_project_tool = Tool(
    name="Finalize Rootstock Project",
    description="Finalizes the Rootstock smart contract project, saving all components.",
    func=finalize_project
)

# Frontend Tools
def generate_html_css_tool(args):
    requirements = args.get('requirements', '')
    return generate_html_css(requirements)

frontend_html_css_tool = Tool(
    name="Generate HTML and CSS",
    description="Generates HTML structure with Tailwind CSS classes based on the given requirements.",
    func=generate_html_css_tool
)

def generate_javascript_tool(html_structure: str) -> str:
    return generate_javascript(html_structure)

frontend_javascript_tool = Tool(
    name="Generate JavaScript",
    description="Generates JavaScript code based on the given HTML structure.",
    func=generate_javascript_tool
)

def integrate_web3js_tool(frontend_code: str) -> str:
    return integrate_web3js(frontend_code)

web3js_integrate_tool = Tool(
    name="Integrate Web3.js",
    description="Integrates Web3.js components into the given frontend code for Rootstock interaction.",
    func=integrate_web3js_tool
)

def integrate_contract_tool(frontend_code: str, contract: str) -> str:
    return integrate_contract(frontend_code, contract)

contract_integrate_tool = Tool(
    name="Integrate Contract",
    description="Integrates the given Rootstock smart contract with the frontend code.",
    func=integrate_contract_tool
)

def save_frontend_tool(project_name: str, html_content: str, css_content: str, js_content: str, web3js_content: str) -> str:
    return save_frontend(project_name, html_content, css_content, js_content, web3js_content)

save_frontend_tool_instance = Tool(
    name="Save Frontend",
    description="Saves the frontend code to the project directory.",
    func=save_frontend_tool
)

# Backend Tools
def setup_supabase_tool(args):
    project_details = args.get('project_details', {})
    return setup_supabase(project_details)

supabase_setup_tool = Tool(
    name="Setup Supabase",
    description="Sets up a Supabase project and creates the necessary database structure.",
    func=setup_supabase_tool
)

def generate_backend_code_tool(project_details: dict, supabase_setup: str) -> str:
    return generate_backend_code(project_details, supabase_setup)

backend_code_generation_tool = Tool(
    name="Generate Backend Code",
    description="Generates backend code for Supabase integration based on the project details and setup.",
    func=generate_backend_code_tool
)

def save_backend_code_tool(project_name: str, backend_code: str) -> str:
    return save_backend_code(project_name, backend_code)

save_backend_code_tool_instance = Tool(
    name="Save Backend Code",
    description="Saves the generated backend code to the project directory.",
    func=save_backend_code_tool
)