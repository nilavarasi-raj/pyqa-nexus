import pytest
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

def test_locked_out_user_login(page: Page):
    # Initialize Login Page Object
    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    login_page.navigate()

    # Step 2: Login using locked-out user credentials
    login_page.login("locked_out_user", "secret_sauce")

    # Step 3: Verify locked-out error message
    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out."
    )

    # Step 4: Verify user remains on login page
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_empty_username_login(page: Page):
    # Initialize Login Page Object
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate()

    # Leave username empty and enter password
    login_page.login("", "secret_sauce")

    # Verify username required error
    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

    # Verify user stays on login page
    expect(page).to_have_url("https://www.saucedemo.com/")


def test_empty_password_login(page: Page):
    # Initialize Login Page Object
    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    login_page.navigate()

    # Step 2: Enter username and leave password empty
    login_page.login("standard_user", "")

    # Step 3: Verify password required error
    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )

    # Step 4: Verify user stays on login page
    expect(page).to_have_url("https://www.saucedemo.com/")


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "invalid_user",
            "secret_sauce",
            "Username and password do not match"
        ),
        (
            "standard_user",
            "invalid_password",
            "Username and password do not match"
        ),
    ],
    ids=["invalid-username", "invalid-password"]
)
def test_invalid_credentials_data_driven(page: Page, username, password, expected_error):
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate()

    # Execute login with parameterized data
    login_page.login(username, password)

    # Verify expected error
    expect(login_page.error_message).to_contain_text(
        expected_error
    )

    # Verify user stays on login page
    expect(page).to_have_url("https://www.saucedemo.com/")
