import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import Login_page


def test_select_product():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests')

    login = Login_page(driver)
    login.authorization()


    enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]')))
    enter_shopping_cart.click()
    print('Click Enter Shopping Cart')

    time.sleep(5)



