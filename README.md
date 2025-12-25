# WordPress Ecommerce Website Automation Test
In this repository contains an automation test suite built with Playwright, Python & Pytest. I implement the Page Object Model (POM) design pattern. The test suite covers various plugin test in a WordPress ecommerce (WooCommerce) environment.

- FlexTable Plugin
- WooCommerce

Project Documentation PDF: <a href="https://ahmedmanan.github.io/WP_Ecommerce_Automation_Test/documents/Playwright_WordPress_Plugin_Automation_Test.pdf" target="_blank">Playwright_WP_Ecommerce_Website_Automation_Test.pdf</a>

## Table Of Content
- [View Live Report](#view-live-report)
- [Bugs or Issues](#Bugs-or-Issues)
- [Project Setup](#-project-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Environment](#setting-up-environment)
  - [Performing Tests](#performing-tests)
  - [Report Generation](#report-generation)
- [Tests](#tests)
  - [FlexTable Plugin](#part-a-flextable-plugin)
  - [WooCommerce](#part-b-woocommerce)
  - [Test Features](#Test-Features)
- [Additional Topics](#additional-topics)
  - [Playwright Javascript WordPress Plugin Test](#playwright-javascript-wordpress-plugin-test)
  - [Similar Topics & Articles](#similar-topics--articles)

## View Live Report
Check the test report live:
- Allure Report: [View Allure Report](https://ahmedmanan.github.io/WP_Ecommerce_Automation_Test/test_reports/allure-report/index.html)
- HTML Report: [View HTML Self Contained Report](https://ahmedmanan.github.io/WP_Ecommerce_Automation_Test/test_reports/report.html)

## Bugs or Issues
During the test execution, I have experienced multiple bugs & issues. I have reported them in the [Project GitHub Issues](https://github.com/AhmedManan/WP_Ecommerce_Automation_Test/issues)

| Issue | Description                               | Link                                                                                | Status |
|-------|-------------------------------------------|-------------------------------------------------------------------------------------|----|
| 01    | Spelling mistake in plugin documentation  | [View Issue](https://github.com/AhmedManan/WP_Ecommerce_Automation_Test/issues/1) | ❌ |
| 02    | Invalid table shortcode in plugin dashboard page | [View Issue](https://github.com/AhmedManan/WP_Ecommerce_Automation_Test/issues/2) | ❌ |
| 02    | Broken or malformed                       | [View Issue](https://github.com/AhmedManan/WP_Ecommerce_Automation_Test/issues/3) | ❌ |

## ⚙️ Project Setup

### Prerequisites

Before running the playwright tests, ensure you have the following installed on your system:

- Python (Installed in your device)
- Node ( Installed in your device)
- Java ( Installed in your device)
- A Code Editor ( PyCharm is recommended )

### Installation

- Clone this repository to your local machine.
- Install all prerequisites

To run the project in your local system, you need to install all the libraries listed in ``requirements.txt``.

To install all the libraries at once, go to your project root directory and open terminal. Use the below command:
```bash
python -m pip install -r requirements.txt
```   
Install the browsers Playwright needs:
```bash
playwright install
```   
### Setting Up Environment
A .env file is a plain text file used to store environment variables for an application,
especially during local development or testing. It follows a simple key-value format, making
it easy to manage configuration settings. To setup the project you need to create a .env file
using the .env.example file provided in the project repository.
```bash
BASE_URL= Website Base URL
ADMIN_USERNAME= Admin Username
ADMIN_PASSWORD= Admin Password


# Default values you may change
TABLE_URL= Google Spreadsheets URL 
TABLE_NAME='Table Name'
TABLE_DESCRIPTION='This table is created from google sheet to perform automation test on WordPress Plugin'

```   
### Performing Tests
 The simplest way to run your tests is to call the pytest command with no arguments:

 ```bash
 pytest
``` 
 You can specify a file path or directory path after the pytest command. Example:
 ```bash
 pytest tests/test_cases/test_01_login.py
``` 
### Report Generation
 HTML reports are excellent for visually reviewing test results. The most popular plugin for this is pytest-html. First, install the plugin from terminal:
 ```bash
 pip install pytest-html
```
Generating an Allure Report provides a rich, interactive, and visually appealing summary of your test execution results. Here is how to set up and generate an Allure Report, specifically using Pytest (Python) as the example framework.
First, install it from terminal:
 ```bash
 pip install allure-pytest
```
Use the allure generate command to process the raw results into an HTML report structure.
 ```bash
 pytest--alluredir=reports/allure-results
```
Use the allure generate command to process the raw results into an HTML report structure.
 ```bash
 allure generate reports/allure-results-o reports/allure-report
```
The easiest way to view the report locally is to use the allure serve command, which starts a local web server and opens the report in your default browser.
 ```bash
allure serve reports/allure-results
```
| Allure Report | HTML Report |
|-------------|--------|
| <img width="500" height="912" alt="Allure_Report_front_page" src="https://github.com/user-attachments/assets/9794a1ed-e934-4e92-98ce-77de2809d846" /> | <img width="500" height="1032" alt="all_html_report" src="https://github.com/user-attachments/assets/1872d1c6-c1c7-460b-8afd-1aa9207d7bd6" />|
## ✔️ Tests
### Part A: FlexTable Plugin

| Test Case | Description | Status |
|-----------|-------------|--------|
| 01        | Verify WordPress Login Functionality | ✔️ |
| 02        | Verify FlexTable Plugin Activation Status | ✔️ |
| 03        | Navigate to FlexTable Dashboard | ✔️ |
| 04        | Create a New Table Using Google Sheet Input | ✔️ |
| 05        | Verify Table Display Using Shortcode | ✔️ |
| 06        | Enable 'Show Table Title' and 'Show Table Description Below Table | ✔️  |
| 07        | Enable Entry Info & Pagination | ✔️ |
| 08        | Update 'Rows Per Page & Table Height' | ✔️ |
| 09        | Delete the Table and Verify Frontend Removal | ✔️ |

### Part B: WooCommerce

| Scenario | Description | Status |
|----------|-------------|--------|
| 01       | End-to-End Checkout Flow | ✔️ |
| 02       | User Account Order History | ✔️ |

### Test Features
 - Cross Browser Testing
 - Data Driven Testing
 - Data Cleaning
 - Generating Screenshots On Failure
 - Generating Log Reports
 - Protecting Secrets through .env file

## Additional Topics

### Playwright Javascript WordPress Plugin Test
In this bellow mentioned project/repository, it contains an automation test suite built with Playwright & JavaScript to test WordPress & WordPress Plugins. I implement the Page Object Model (POM) design pattern.

 **Project Link:** [JS_Playwright_WP_Plugin_Test](https://github.com/AhmedManan/JS_Playwright_WP_Plugin_Test)

### Similar Topics & Articles

[WordPress Ecommerce Website Automation Test](https://github.com/AhmedManan/WP_Ecommerce_Automation_Test)

[Python Complete Cheat Sheet](https://mananacademy.com/complete-python-cheat-sheet/)

[Complete JavaScript Cheat sheet](https://mananacademy.com/complete-javascript-cheat-sheet/)

[⬆️Back to Top](#qa-wppool-assignment)
