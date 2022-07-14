from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from dataclasses import dataclass


class InventoryPage(BasePage):

    shoping_cart_icon = (By.CSS_SELECTOR, '.shopping_cart_link')

    def add_product_to_cart(self, locator):
        self.click(locator)

    def proceed_to_cart(self):
        self.click(self.shoping_cart_icon)


@dataclass
class Products:
    sauce_lab_backpack = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
