import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_by_product():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests')

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_product()
    cp = Cart_page(driver)
    cp.product_confirmation()

    time.sleep(5)



