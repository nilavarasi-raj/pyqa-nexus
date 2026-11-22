
from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_link = page.locator(
            "[data-test='shopping-cart-link']"
        )
        self.cart_badge = page.locator(
            "[data-test='shopping-cart-badge']"
        )
        self.product_name = page.locator(
            "[data-test='inventory-item-name']"
        )
        self.cart_items = page.locator(".cart_item")
        self.remove_backpack_button = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )

    def open_cart(self):
        self.cart_link.click()

    def verify_cart_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)

    
    def verify_backpack_in_cart(self):
        backpack = self.page.locator(
            ".cart_item [data-test='inventory-item-name']"
        ).filter(has_text="Sauce Labs Backpack")

        expect(backpack).to_have_count(1)
        expect(backpack).to_have_text("Sauce Labs Backpack")

    def remove_backpack(self):
        self.remove_backpack_button.click()

    def verify_cart_empty(self):
        expect(self.cart_badge).to_have_count(0)
        expect(self.cart_items).to_have_count(0)
        expect(self.cart_link).to_have_attribute(
            "aria-label", "Cart, empty"
        )

    def verify_multiple_products_in_cart(self):
        expect(self.cart_items).to_have_count(2)

        expect(self.product_name).to_have_text([
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light"
        ])