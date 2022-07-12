import pytest
from pages.login_page import LoginPage


class TestLoginPageElements:

    def test_is_logo_visible(self, driver):
        login_page = LoginPage(driver)
        logo = login_page.logo()

        assert logo.is_displayed() is True

    def test_is_bot_picture_visible(self, driver):
        login_page = LoginPage(driver)
        bot_picture = login_page.bot_picture()

        assert bot_picture.is_displayed() is True

    def test_is_credentials_section_visible(self, driver):
        login_page = LoginPage(driver)
        creds_section = login_page.credentials_section()

        assert creds_section.is_displayed() is True

    def test_is_credential_section_contains_text(self, driver):
        login_page = LoginPage(driver)
        available_names_block = login_page.credentials_section_text()

        available_names_list = ["Accepted usernames are:",
                                "standard_user",
                                "locked_out_user",
                                "problem_user",
                                "performance_glitch_user"]
        for name in available_names_list:
            assert name in available_names_block, 'f{name} not in list'

    def test_is_password_section_visible(self, driver):
        login_page = LoginPage(driver)
        pass_section = login_page.password_section()

        assert pass_section.is_displayed() is True

    def test_is_password_section_contains_text(self, driver):
        login_page = LoginPage(driver)
        text = login_page.password_session_text()

        assert 'Password for all users:' in text
        assert 'secret_sauce' in text


class TestLoginPageActions:

    @pytest.mark.parametrize("login, password", [
        ("standard_user", "secret_sauce"),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce')
    ])
    def test_successfully_login(self, driver, base_url, login, password):
        login_page = LoginPage(driver)
        login_page.input_name(login)
        login_page.input_password(password)
        login_page.click_login_button()

        assert driver.current_url == f'{base_url}/inventory.html'

    def test_locked_user_cant_login(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.input_name('locked_out_user')
        login_page.input_password('secret_sauce')
        login_page.click_login_button()

        assert driver.current_url == f'{base_url}/'
