from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopingCartPage(BasePage):

    checkout_button = (By.CSS_SELECTOR, '#checkout')
    product_quantity = (By.CSS_SELECTOR, '.cart_quantity')

    def click_checkout_button(self):
        self.click(self.checkout_button)

    def get_product_quantity(self):
        text = self.get_text_from_element(self.product_quantity)
        return text
