from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.error_message = page.locator('[data-test="error"]')
        self.complete_header = page.locator('.complete-header')
        self.summary_total = page.locator('.summary_total_label')

    def fill_customer_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        return self

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def verify_order_complete(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")

    def get_total_price(self):
        total_text = self.summary_total.text_content()
        return float(total_text.replace("Total: $", ""))

    def verify_error(self, message: str):
        expect(self.error_message).to_contain_text(message)

