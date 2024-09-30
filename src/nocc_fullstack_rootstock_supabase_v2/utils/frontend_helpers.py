import os
from litellm import completion
from dotenv import load_dotenv
from ..logger import log_step

load_dotenv()

def generate_html_css(requirements: str) -> tuple:
    prompt = f"""
    Given the following requirements, generate an HTML structure with Tailwind CSS classes:

    Requirements:
    {requirements}

    Please provide a complete HTML file that includes:
    1. Proper HTML5 structure
    2. Tailwind CSS classes for styling
    3. Responsive design considerations
    4. Semantic HTML elements
    5. Comments explaining the purpose of each section
    6. Link to the styles.css file
    7. Script tags for app.js and web3-integration.js files

    Ensure the HTML is valid and follows best practices for modern web development.
    Include a script tag for loading Tailwind CSS from a CDN.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.7
    )

    html_content = response.choices[0].message.content.strip()
    html_content = html_content.replace("```html", "").replace("```", "").strip()
    css_content = "/* Tailwind CSS will be loaded from CDN */"

    log_step("Generated HTML and CSS", html_content)
    return html_content, css_content

def generate_javascript(html_structure: str) -> str:
    prompt = f"""
    Given the following HTML structure, generate JavaScript code to add interactivity and dynamic behavior:

    {html_structure}

    Please provide JavaScript code that includes:
    1. Event listeners for user interactions
    2. DOM manipulation to update the UI dynamically
    3. Any necessary AJAX calls (you can use fetch API)
    4. Error handling and input validation
    5. Comments explaining the purpose of each function or section of code

    Ensure the JavaScript is modern (ES6+) and follows best practices for web development.
    Do not include any Web3 or blockchain-specific code in this file.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.7
    )

    js_content = response.choices[0].message.content.strip()
    js_content = js_content.replace("```javascript", "").replace("```", "").strip()

    log_step("Generated JavaScript", js_content)
    return js_content

def integrate_web3js(frontend_code: str) -> str:
    prompt = f"""
    Given the following frontend code, integrate Web3.js for Rootstock interactions:

    {frontend_code}

    Please provide ONLY the complete JavaScript code that includes:
    1. Necessary Web3.js imports (use unpkg.com CDN for web3)
    2. Rootstock network configuration
    3. Functions to connect to Metamask and switch to the Rootstock network
    4. Functions to interact with Rootstock smart contracts (e.g., read from and write to contracts)
    5. UI elements to display wallet information and transaction status
    6. Error handling for Web3-related operations
    7. Comments explaining the Web3.js integration

    Ensure the integration follows best practices for Web3.js usage and maintains the existing functionality of the frontend.
    Include the FULL code for connecting to Metamask and switching to the Rootstock network.
    Use the Rootstock Testnet for the network configuration.
    Do not include any HTML or explanations, only output the actual JavaScript code.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.7
    )

    js_code = response.choices[0].message.content.strip()
    js_code = js_code.replace("```javascript", "").replace("```", "").strip()
    
    log_step("Integrated Web3.js", js_code)
    return js_code

def integrate_contract(frontend_code: str, contract: str) -> str:
    prompt = f"""
    Given the following frontend code and Solidity smart contract for Rootstock, integrate the contract functionality into the frontend:

    Frontend Code:
    {frontend_code}

    Solidity Smart Contract:
    {contract}

    Please update the frontend code to include:
    1. Functions to call the smart contract methods using Web3.js
    2. UI elements to interact with the smart contract (e.g., forms, buttons)
    3. Display of smart contract data and transaction results
    4. Error handling for contract interactions
    5. Comments explaining the integration of each smart contract function

    Ensure the integration follows best practices for interacting with Solidity smart contracts on Rootstock from a web frontend.
    """

    response = completion(
        model="claude-3-sonnet-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.7
    )

    js_content = response.choices[0].message.content.strip()
    js_content = js_content.replace("```javascript", "").replace("```", "").strip()

    log_step("Integrated Contract", js_content)
    return js_content

def save_frontend(project_name: str, html_content: str, css_content: str, js_content: str, web3js_content: str) -> str:
    result = f"Frontend code generated for {project_name}:\n\nHTML:\n{html_content}\n\nCSS:\n{css_content}\n\nJavaScript:\n{js_content}\n\nWeb3.js:\n{web3js_content}"
    log_step("Generated Frontend", result)
    return result