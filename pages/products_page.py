
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
 
    def sort_products_low_to_high(self):
        self.page.locator(
            "[data-test='product-sort-container']"
        ).select_option("lohi")

    def get_product_prices(self):
        price_elements = self.page.locator(
            "[data-test='inventory-item-price']"
        ).all_text_contents()

        return [
            float(price.replace("$", ""))
            for price in price_elements
        ]

    def sort_products_high_to_low(self):
        self.page.locator(
            "[data-test='product-sort-container']"
        ).select_option("hilo")

    def add_bike_light_to_cart(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-bike-light']"
        ).click()

    
    def sort_products_name_a_to_z(self):
        self.page.locator(
            "[data-test='product-sort-container']"
        ).select_option("az")

    def get_product_names(self):
        return self.page.locator(
            "[data-test='inventory-item-name']"
        ).all_text_contents()
