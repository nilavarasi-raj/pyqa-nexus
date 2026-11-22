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


def test_products_sort_low_to_high(page: Page):

    # Initialize Page Objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Verify products page
    products_page.verify_products_page()

    # Sort products by price (Low to High)
    products_page.sort_products_low_to_high()

    # Get displayed product prices
    actual_prices = products_page.get_product_prices()

    # Verify prices are sorted in ascending order
    assert len(actual_prices) > 1, "Not enough products to verify sorting"
    assert actual_prices == sorted(actual_prices), (
        f"Product prices are not sorted: {actual_prices}"
    )


def test_products_sort_high_to_low(page: Page):

    # Initialize Page Objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Verify Products page
    products_page.verify_products_page()

    # Step 3: Sort products by price (High to Low)
    products_page.sort_products_high_to_low()

    # Step 4: Get displayed prices
    actual_prices = products_page.get_product_prices()

    # Step 5: Verify descending order
    assert len(actual_prices) > 1, "Not enough products to verify sorting"

    assert actual_prices == sorted(actual_prices, reverse=True), (
        f"Product prices are not sorted High to Low: {actual_prices}"
    )
