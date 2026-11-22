
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )
        self.first_name = page.locator(
            "[data-test='firstName']"
        )
        self.last_name = page.locator(
            "[data-test='lastName']"
        )
        self.postal_code = page.locator(
            "[data-test='postalCode']"
        )
        self.continue_button = page.locator(
            "[data-test='continue']"
        )
        self.error_message = page.locator(
            "[data-test='error']"
        )

    def start_checkout(self):
        self.checkout_button.click()

    def enter_customer_details(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def verify_required_first_name_error(self):
        expect(self.error_message).to_contain_text(
            "First Name is required"
        )

    def verify_checkout_overview(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )
        expect(
            self.page.locator("[data-test='inventory-item-name']")
        ).to_have_text("Sauce Labs Backpack")

    def finish_checkout(self):
        self.page.locator("[data-test='finish']").click()

    def verify_order_confirmation(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-complete.html"
        )
        expect(
            self.page.locator("[data-test='complete-header']")
        ).to_have_text("Thank you for your order!")
