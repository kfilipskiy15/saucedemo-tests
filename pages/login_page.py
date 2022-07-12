from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    name_input = (By.CSS_SELECTOR, '#user-name')
    password_input = (By.CSS_SELECTOR, '#password')
    login_logo = (By.CSS_SELECTOR, '.login_logo')
    robot_picture = (By.CSS_SELECTOR, '.bot_column')
    login_button = (By.CSS_SELECTOR, '#login-button')
    credentials_div = (By.CSS_SELECTOR, "#login_credentials")
    password_div = (By.CSS_SELECTOR, ".login_password")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def logo(self):
        logo = self.get_visible_element(locator=self.login_logo)
        return logo

    def bot_picture(self):
        bot_picture = self.get_visible_element(locator=self.robot_picture)
        return bot_picture

    def credentials_section(self):
        section = self.get_visible_element(locator=self.credentials_div)
        return section

    def credentials_section_text(self):
        section = self.get_text_from_element(locator=self.credentials_div)
        return section

    def password_section(self):
        section = self.get_visible_element(locator=self.password_div)
        return section

    def password_session_text(self):
        section = self.get_text_from_element(locator=self.password_div)
        return section

    def input_name(self, text: str):
        self.input_text(locator=self.name_input, text=text)

    def input_password(self, text: str):
        self.input_text(locator=self.password_input, text=text)

    def click_login_button(self):
        self.click(locator=self.login_button)
