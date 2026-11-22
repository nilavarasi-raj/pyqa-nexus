
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_empty_first_name(page: Page):
    # Initialize Page Objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add a product
    products_page.add_backpack_to_cart()

    # Step 3: Open cart
    cart_page.open_cart()
    cart_page.verify_backpack_in_cart()

    # Step 4: Proceed to checkout
    checkout_page.start_checkout()

    # Step 5: Leave First Name empty
    checkout_page.enter_customer_details("", "Raj", "600001")

    # Step 6: Click Continue
    checkout_page.continue_checkout()

    # Step 7: Verify validation error
    checkout_page.verify_required_first_name_error()

    # Step 8: Verify user stays on checkout information page
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )


def test_successful_checkout(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    products_page.add_backpack_to_cart()
    cart_page.verify_cart_count("1")

    # Step 3: Open cart
    cart_page.open_cart()
    cart_page.verify_backpack_in_cart()

    # Step 4: Start checkout
    checkout_page.start_checkout()

    # Step 5: Enter valid customer information
    checkout_page.enter_customer_details(
        "Nilavarasi", "Raj", "600001"
    )

    # Step 6: Continue to order overview
    checkout_page.continue_checkout()
    checkout_page.verify_checkout_overview()

    # Step 7: Finish checkout
    checkout_page.finish_checkout()

    # Step 8: Verify order confirmation
    checkout_page.verify_order_confirmation()
