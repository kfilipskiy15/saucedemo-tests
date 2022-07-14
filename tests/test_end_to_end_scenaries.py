from pages.cart import ShopingCartPage
from pages.checkout import CheckOutStepOne, CheckOutStepTwo, \
    CheckOutCompletePage
from pages.inventory import InventoryPage, Products
from pages.login_page import LoginPage


class TestProductCheckout:

    def test_user_can_buy_product(self, base_url, driver):
        self.login_with_valid_credential(driver,
                                         "standard_user",
                                         "secret_sauce")
        self.add_product_to_cart(driver)
        self.proceed_to_checkout(driver)
        self.fill_checkout_user_info(driver, 'John', 'Doe', '43000')
        self.complete_checkout(driver)

        assert driver.current_url == f'{base_url}/checkout-complete.html'

        elements = self.checkout_complete_page(driver)
        assert elements.title() == 'CHECKOUT: COMPLETE!'
        assert elements.pony_picture().is_displayed()

    @classmethod
    def login_with_valid_credential(cls, driver, user_name, password):
        login_page = LoginPage(driver)
        login_page.input_name(user_name)
        login_page.input_password(password)
        login_page.click_login_button()

    @classmethod
    def add_product_to_cart(cls, driver):
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(Products.sauce_lab_backpack)
        inventory_page.proceed_to_cart()

    @classmethod
    def proceed_to_checkout(cls, driver):
        cart_page = ShopingCartPage(driver)
        cart_page.click_checkout_button()

    @classmethod
    def fill_checkout_user_info(cls, driver, first_name, second_name,
                                zip_code):
        checkout_step_one = CheckOutStepOne(driver)
        checkout_step_one.input_first_name(first_name)
        checkout_step_one.input_second_name(second_name)
        checkout_step_one.input_zip_postal_code(zip_code)
        checkout_step_one.click_continue_button()

    @classmethod
    def complete_checkout(cls, driver):
        checkout_step_two = CheckOutStepTwo(driver)
        checkout_step_two.click_finish_button()

    @classmethod
    def checkout_complete_page(cls, driver):
        elements = CheckOutCompletePage(driver)
        return elements
