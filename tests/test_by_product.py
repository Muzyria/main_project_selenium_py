import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_by_product_1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # cip = Client_infomation_page(driver)
    # cip.input_information()
    #
    # pp = Payment_page(driver)
    # pp.payment()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)


def test_by_product_2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 2')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    time.sleep(5)


def test_by_product_3():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 3')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.product_confirmation()


    time.sleep(5)
