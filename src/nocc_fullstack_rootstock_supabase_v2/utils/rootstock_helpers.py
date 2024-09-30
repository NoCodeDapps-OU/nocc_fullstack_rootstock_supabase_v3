import os
from crewai import Agent
from litellm import completion
from dotenv import load_dotenv
from ..logger import log_step

load_dotenv()

def generate_rootstock_contract(requirements: str) -> str:
    agent = Agent(
        role="Smart Contract Generator",
        goal="Generate a Solidity smart contract for Rootstock",
        backstory="You are an expert Solidity developer specializing in Rootstock smart contracts.",
        llm='claude-3-sonnet-20240229'
    )
    
    prompt = f"""
    Given the following requirements, generate a Solidity smart contract for Rootstock:

    Requirements:
    {requirements}

    Please provide a complete Solidity smart contract that includes:
    1. Appropriate state variables and mappings
    2. Relevant functions with proper access controls
    3. Error handling and require statements
    4. Any necessary helper functions
    5. Comments explaining the purpose of each section
    6. Proper SPDX license identifier and pragma statement

    Ensure the contract follows best practices for security and efficiency in Solidity for Rootstock.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.7
    )

    contract = response.choices[0].message.content.strip()
    contract = contract.replace("```solidity", "").replace("```", "").strip()

    log_step("Generated Rootstock Contract", contract)
    return contract

def generate_rootstock_tests(contract: str) -> str:
    prompt = f"""
    Given the following Solidity smart contract for Rootstock, generate a comprehensive test suite using Mocha and Chai:

    {contract}

    Your test suite should include:
    1. Unit tests for each public function
    2. Tests for edge cases and potential error conditions
    3. Tests for different user roles (if applicable)
    4. Tests for any complex logic or calculations

    Provide the COMPLETE test cases in JavaScript format compatible with Mocha and Chai, including setup, execution, and assertions for each test. 
    Ensure that the test suite is complete, syntactically correct, and covers all aspects of the contract.
    Include necessary imports, contract artifacts, and the complete describe/it structure for each test case.
    Use web3.js or ethers.js for interacting with the contract in tests.
    Do not include any explanations or summaries, only output the actual JavaScript code for the tests.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096,
        temperature=0.7
    )

    tests = response.choices[0].message.content.strip()
    tests = tests.replace("```javascript", "").replace("```", "").strip()
    
    log_step("Generated Rootstock Tests", tests)
    return tests

def validate_rootstock_contract(contract: str) -> str:
    prompt = f"""
    Validate the following Solidity smart contract for Rootstock:

    {contract}

    Check for:
    1. Correct syntax and structure
    2. Proper use of Solidity best practices
    3. Potential security vulnerabilities
    4. Gas optimization
    5. Correct use of Rootstock-specific features (if any)

    Provide a detailed validation report, including any issues found and suggestions for improvement.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7
    )

    validation_result = response.choices[0].message.content.strip()
    log_step("Validated Rootstock Contract", validation_result)
    return validation_result

def validate_rootstock_tests(tests: str) -> str:
    prompt = f"""
    Validate the following test suite for a Rootstock smart contract:

    {tests}

    Check for:
    1. Correct use of Mocha and Chai
    2. Comprehensive coverage of all contract functions
    3. Proper setup and teardown of test environment
    4. Correct use of web3.js or ethers.js for contract interaction
    5. Edge case and error condition testing

    Provide a detailed validation report, including any issues found and suggestions for improvement.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7
    )

    validation_result = response.choices[0].message.content.strip()
    log_step("Validated Rootstock Tests", validation_result)
    return validation_result

def setup_project_structure(project_name: str) -> str:
    result = f"Project structure for '{project_name}' set up (simulated)."
    log_step("Set Up Project Structure", result)
    return result

def save_contract(project_name: str, contract: str) -> str:
    result = f"Contract generated for {project_name}:\n\n{contract}"
    log_step("Generated Contract", result)
    return result

def save_tests(project_name: str, tests: str) -> str:
    result = f"Tests generated for {project_name}:\n\n{tests}"
    log_step("Generated Tests", result)
    return result