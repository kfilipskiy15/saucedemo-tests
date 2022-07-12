from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

    first_product_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    shoping_cart_icon = (By.CSS_SELECTOR, '.shopping_cart_link')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def add_first_product_to_cart(self):
        self.click(self.first_product_button)

    def proceed_to_cart(self):
        self.click(self.shoping_cart_icon)
