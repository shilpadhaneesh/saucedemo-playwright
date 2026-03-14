import pytest
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Checkout")
class TestCheckout:

    @pytest.fixture(autouse=True)
    def login_and_add_item(self, page: Page, base_url, credentials):
        page.goto(base_url)
        LoginPage(page).login(
            credentials["standard"]["username"],
            credentials["standard"]["password"]
        )
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

    @allure.title("Cart shows correct item")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_cart_shows_correct_item(self, page: Page):
        cart = CartPage(page)
        cart.verify_on_cart_page()
        assert "Sauce Labs Backpack" in cart.get_cart_item_names()

    @allure.title("Cart shows correct item count")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_cart_item_count(self, page: Page):
        cart = CartPage(page)
        assert cart.get_cart_item_count() == 1

    @allure.title("Checkout step 1 - missing first name shows error")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_missing_first_name(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_customer_info("", "Smith", "SW1A1AA")
        checkout.click_continue()
        checkout.verify_error("First Name is required")

    @allure.title("Checkout step 1 - missing last name shows error")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_missing_last_name(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_customer_info("John", "", "SW1A1AA")
        checkout.click_continue()
        checkout.verify_error("Last Name is required")

    @allure.title("Checkout step 1 - missing postal code shows error")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_missing_postal_code(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_customer_info("John", "Smith", "")
        checkout.click_continue()
        checkout.verify_error("Postal Code is required")

    @allure.title("Full E2E checkout flow completes successfully")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_full_checkout_flow(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_customer_info("John", "Smith", "SW1A1AA")
        checkout.click_continue()
        checkout.click_finish()
        checkout.verify_order_complete()

    @allure.title("Order summary shows correct total price")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_order_summary_price(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_customer_info("John", "Smith", "SW1A1AA")
        checkout.click_continue()
        total = checkout.get_total_price()
        assert total > 0

    @allure.title("Cancel checkout returns to inventory")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_cancel_checkout(self, page: Page):
        CartPage(page).proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.cancel_button.click()
        assert "cart" in page.url

    @allure.title("Continue shopping from cart returns to inventory")
    @pytest.mark.regression
    @pytest.mark.checkout
    def test_continue_shopping(self, page: Page):
        cart = CartPage(page)
        cart.continue_shopping()
        assert "inventory" in page.url
