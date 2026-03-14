from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator('.cart_item')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def get_item_names(self) -> list:
        return self.page.locator('.inventory_item_name').all_inner_texts()

    def proceed_to_checkout(self):
        self.checkout_button.click()
        return self

    def continue_shopping(self):
        self.continue_shopping_button.click()
        return self

    def remove_item(self, item_name: str):
        item_id = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.locator(f'[data-test="remove-{item_id}"]').click()
        return self
