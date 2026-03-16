from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_list = page.locator('.inventory_item')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.cart_icon = page.locator('.shopping_cart_link')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.menu_button = page.locator('#react-burger-menu-btn')
        self.logout_link = page.locator('#logout_sidebar_link')
        self.page_title = page.locator('.title')
        self.inventory_items = self.product_list

    def get_product_count(self) -> int:
        return self.product_list.count()

    def add_item_to_cart(self, item_name: str):
        item_id = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.locator(f'[data-test="add-to-cart-{item_id}"]').click()
        return self

    def remove_item_from_cart(self, item_name: str):
        item_id = item_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.locator(f'[data-test="remove-{item_id}"]').click()
        return self

    def get_cart_count(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_icon.click()
        return self

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)
        return self

    def get_all_product_names(self) -> list:
        return self.page.locator('.inventory_item_name').all_inner_texts()

    def get_all_product_prices(self) -> list:
        prices = self.page.locator('.inventory_item_price').all_inner_texts()
        return [float(p.replace('$', '')) for p in prices]

    def logout(self):
        self.menu_button.click()
        self.page.wait_for_selector('#logout_sidebar_link', state='visible')
        self.logout_link.click()

    def get_product_names(self):
        return self.get_all_product_names()

    def get_product_prices(self):
        return self.get_all_product_prices()
