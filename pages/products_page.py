
from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.page_heading = page.locator(".title")
        self.product_items = page.locator(".inventory_item")

    def verify_products_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
        expect(self.page_heading).to_have_text("Products")

    def verify_products_displayed(self):
        expect(self.product_items.first).to_be_visible()
        expect(self.product_items).not_to_have_count(0)

    def add_backpack_to_cart(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        ).click()