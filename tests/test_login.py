from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    #Create Login Page object
    login_page = LoginPage(page)

    #Navigate and login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    #verify successful login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    expect(page.locator(".title")).to_have_text("Products")

def test_invalid_login(page: Page):
    #Create Login Page object
    login_page = LoginPage(page)

    #Navigate and login
    login_page.navigate()

    # Login with invalid credentials
    login_page.login("standard_user", "sss")

    # Verify error message using POM locator
    expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

    # Verify user stays on login page
    expect(page).to_have_url("https://www.saucedemo.com/")