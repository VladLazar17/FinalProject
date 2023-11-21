# Automated Testing Project for https://demo.nopcommerce.com/

This project is developed for automated testing of the nopCommerce demo site using Behavior-Driven Development (BDD) principles. The tests are written in Gherkin syntax and implemented using the Behave framework with Selenium.

## Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (recommended version: 3.11)
- [Selenium](https://www.selenium.dev/)
- [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
- [Behave](https://behave.readthedocs.io/en/latest/)
- [Behave HTML Formatter](https://pypi.org/project/behave-html-formatter/)
- [Gherkin](https://pypi.org/project/gherkin/)
- [Ini](https://pypi.org/project/ini/)


## Folder Structure

- features:
    - login.feature
    - register.feature
    - search_results.feature
    - wishlist.feature

- pages:
    - base_page.py 
    - home_page.py 
    - jewelry_page.py
    - login_page.py
    - search_results_page.py
    - wishlist_page.py
- steps:
   - login_steps.py
   - register_steps.py
   - search_results_steps.py
   - wishlist_steps.py
- browser.py
- environment.py

   

## Usage

### Clone the repository:
```bash
git clone https://github.com/VladLazar17/FinalProject.git
```

### Run the tests:
```bash
behave -f html -o report.html
```
The above command will generate an HTML report in the FinalProjectBDD folder.

## Viewing the HTML Report
Open the generated HTML report in your preferred web browser to view detailed test results.


