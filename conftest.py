import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")
table_url = os.getenv("TABLE_URL")
table_name = os.getenv("TABLE_NAME")
table_description = os.getenv("TABLE_DESCRIPTION")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
