import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Inventory")
class TestInventory:

    @pytest.fixture(autouse=True)
    def login(self, page: Page, base_url, credentials):
        page.goto(base_url)
        LoginPage(page).login(
            credentials["standard"]["username"],
            credentials["standard"]["password"]
        )

    @allure.title("Inventory page shows 6 products")
    @pytest.mark.smoke
    @pytest.mark.inventory
    def test_product_count(self, page: Page):
        inventory = InventoryPage(page)
        assert inventory.inventory_items.count() == 6

    @allure.title("Add single item to cart")
    @pytest.mark.smoke
    @pytest.mark.inventory
    def test_add_item_to_cart(self, page: Page):
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        assert inventory.get_cart_count() == 1

    @allure.title("Add multiple items to cart")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_add_multiple_items(self, page: Page):
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")
        assert inventory.get_cart_count() == 2

    @allure.title("Remove item from cart")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_remove_item_from_cart(self, page: Page):
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.remove_item_from_cart("Sauce Labs Backpack")
        assert inventory.get_cart_count() == 0

    @allure.title("Sort products A to Z")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_az(self, page: Page):
        inventory = InventoryPage(page)
        inventory.sort_by("az")
        names = inventory.get_product_names()
        assert names == sorted(names)

    @allure.title("Sort products Z to A")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_za(self, page: Page):
        inventory = InventoryPage(page)
        inventory.sort_by("za")
        names = inventory.get_product_names()
        assert names == sorted(names, reverse=True)

    @allure.title("Sort products by price low to high")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_price_low_to_high(self, page: Page):
        inventory = InventoryPage(page)
        inventory.sort_by("lohi")
        prices = inventory.get_product_prices()
        assert prices == sorted(prices)

    @allure.title("Sort products by price high to low")
    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_price_high_to_low(self, page: Page):
        inventory = InventoryPage(page)
        inventory.sort_by("hilo")
        prices = inventory.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    @allure.title("Cart icon navigates to cart page")
    @pytest.mark.smoke
    @pytest.mark.inventory
    def test_navigate_to_cart(self, page: Page):
        inventory = InventoryPage(page)
        inventory.go_to_cart()
        assert "cart" in page.url
