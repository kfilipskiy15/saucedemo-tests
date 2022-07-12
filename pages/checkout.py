from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckOutStepOne(BasePage):
    first_name_input = (By.CSS_SELECTOR, '#first-name')
    second_name_input = (By.CSS_SELECTOR, '#last-name')
    zip_postal_input = (By.CSS_SELECTOR, '#postal-code')
    continue_button = (By.CSS_SELECTOR, '#continue')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def input_first_name(self, text: str):
        self.input_text(self.first_name_input, text)

    def input_second_name(self, text: str):
        self.input_text(self.second_name_input, text)

    def input_zip_postal_code(self, text: str):
        self.input_text(self.zip_postal_input, text)

    def click_continue_button(self):
        self.click(self.continue_button)


class CheckOutStepTwo(BasePage):
    finish_button = (By.CSS_SELECTOR, '#finish')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_finish_button(self):
        self.click(self.finish_button)


class CheckOutCompletePage(BasePage):
    title_element = (By.CSS_SELECTOR, '.title')
    pony_picture_element = (By.CSS_SELECTOR, "img[alt='Pony Express']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def title(self):
        text = self.get_text_from_element(self.title_element)
        return text

    def pony_picture(self):
        element = self.get_visible_element(self.pony_picture_element)
        return element
