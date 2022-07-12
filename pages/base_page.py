from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def input_text(self, locator: tuple, text: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator: tuple):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).click()

    def get_visible_element(self, locator: tuple):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return element

    def get_text_from_element(self, locator: tuple):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).text
        return text
