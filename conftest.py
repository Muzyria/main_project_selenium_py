import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up():
    print('Start test')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # url = 'https://www.saucedemo.com/'
    # self.driver.get(self.url)
    # self.driver.maximize_window()

    yield

    # driver.quit()
    print('Finish test')


@pytest.fixture(scope="module")
def set_group():
    print('Enter system')

    yield

    print('Exit system')

