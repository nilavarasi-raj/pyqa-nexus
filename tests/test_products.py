from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_displayed_after_login(page: Page):

    # Initialize page objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # Login to application
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Verify Products page
    products_page.verify_products_page()

    # Verify product list
    products_page.verify_products_displayed()


