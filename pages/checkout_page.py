from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.error_message = page.locator('[data-test="error"]')
        self.complete_header = page.locator('.complete-header')
        self.item_total = page.locator('.summary_subtotal_label')
        self.tax = page.locator('.summary_tax_label')
        self.total = page.locator('.summary_total_label')

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        return self

    def continue_to_overview(self):
        self.continue_button.click()
        return self

    def finish_order(self):
        self.finish_button.click()
        return self

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def get_total_price(self) -> float:
        total_text = self.total.inner_text()
        return float(total_text.replace('Total: $', ''))

    def is_order_complete(self) -> bool:
        return self.complete_header.is_visible()
