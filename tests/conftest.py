from pages.base_page import BasePage
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@fixture(scope='function', autouse=True)
def driver(request):
    if request.config.getoption("--browser") == "firefox":
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
        browser.get(request.config.getoption("--url"))
    else:
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        browser.get(request.config.getoption("--url"))
    yield browser
    browser.quit()


@fixture(scope="session", autouse=True)
def base_url(request):
    return request.config.getoption("--url")
