# Grafana Automation Testing Project

## Welcome!
This project is my final creation from a software testing and automation course I completed. I poured everything I learned into it to make it as useful and cool as possible. This project brings together automation for web and API testing, focusing on well-structured code, advanced tools, and reports that make the results easy to understand.

## What Does This Project Do?
- **Web UI Testing Automation**: The project uses Selenium to validate the UI of web applications. It ensures that every button, text field, and form behaves exactly as it should.
- **API Testing**: Leveraging Python’s `requests` library, I tested various API calls to ensure the responses are correct and bug-free.
- **Data-Driven Testing**: All tests are powered by CSV files, enabling the execution of multiple scenarios to make sure the application handles everything we throw at it.
- **Fancy Reports**: Allure was used to generate reports that show what passed, what failed, and where improvements are needed. This way, even if you're not a coding expert, you can still understand what's going on.
- **Modularity and Readable Code**: The project is built in a modular way, which means it’s easy to add new tests, features, or make adjustments without losing your mind.

## How Is It Built?
- **`configuration/`**: Contains all the test configuration settings, from browser settings to Allure configurations.
- **`ddt/`**: Stores CSV files that provide all the data used for testing.
- **`extensions/`**: Custom actions like API calls, UI actions, and specific verification checks.
- **`page_objects/`**: Implements the Page Object Model (POM) to organize all page elements in a clean way.
- **`test_cases/`**: This is where all the test scripts live. It’s where the magic happens.
- **`utilities/`**: General tools that assist with managing the tests, like event listeners and configuration helpers.
- **`workflows/`**: Contains full test scenarios and business logic, all broken down in an organized manner.

## Tools and Technologies
- **Language**: Python – classic and reliable.
- **Automation**: Selenium and Pytest for running browser-based tests.
- **API Testing**: Python's `requests` library.
- **Reporting**: Allure – to make everything clear and easy to understand.
- **Data**: CSV format for flexible testing scenarios.

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/atiaron/Grafana-Automation-Testing.git
   ```
2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the tests**:
   Use Pytest to run all tests:
   ```bash
   pytest --alluredir=allure-results
   ```
4. **Generate a report with Allure**:
   ```bash
   allure serve allure-results
   
