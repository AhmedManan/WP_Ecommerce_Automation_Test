# QA WPPOOL Assignment
In this repository contains an automation test suite built with ***Playwright***, ***Python*** & ***Pytest***. I implement the Page Object Model (POM) design pattern. The test suite covers:

- FlexTable Plugin
- WooCommerce

## Table Of Content
- [View Live Report](#-view-live-report)
- [Project Setup](#-project-setup)

## 🔎 View Live Report
Check the test report live:
- Allure Report: [View Allure Report](https://ahmedmanan.github.io/QA_WPPOOL_Assignment/test_reports/allure-report/index.html)
- HTML Report: [View HTML Self Contained Report](https://ahmedmanan.github.io/QA_WPPOOL_Assignment/test_reports/index.html)

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
TABLE_DESCRIPTION='This table is created from google sheet to perform automation test on WPPOOL flextable plugin'

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

### Bonus 

| Task | Description                       | Status |
|------|-----------------------------------|--------|
| 01   | Run the test suite from GitAction | ✔️ |
