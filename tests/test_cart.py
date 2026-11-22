from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(page: Page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Verify Products page
    products_page.verify_products_page()

    # Add product
    products_page.add_backpack_to_cart()

    # Verify cart badge
    cart_page.verify_cart_count("1")

    # Open cart
    cart_page.open_cart()

    # Verify product in cart
    cart_page.verify_backpack_in_cart()



def test_remove_product_from_cart(page: Page):

    # Initialize page objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Step 1: Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Verify Products page
    products_page.verify_products_page()

    # Step 3: Add Backpack to cart
    products_page.add_backpack_to_cart()

    # Step 4: Verify cart count is 1
    cart_page.verify_cart_count("1")

    # Step 5: Open cart
    cart_page.open_cart()

    # Step 6: Verify Backpack is present
    cart_page.verify_backpack_in_cart()

    # Step 7: Remove Backpack
    cart_page.remove_backpack()

    # Step 8: Verify cart is empty
    cart_page.verify_cart_empty()

