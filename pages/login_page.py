from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')
        self.error_close_button = page.locator('[data-test="error-button"]')

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def dismiss_error(self):
        self.error_close_button.click()
        return self

    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()
