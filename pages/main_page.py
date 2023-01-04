import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//a[@class="shopping_cart_link"]'
    menu = '//button[@id="react-burger-menu-btn"]'
    link_about = '//a[@id="about_sidebar_link"]'

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_lint_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Click select product_1')

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print('Click select product_2')

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print('Click select product_3')


    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    def click_menu(self):
        self.get_menu().click()
        print('Click menu')

    def click_link_about(self):
        self.get_lint_about().click()
        print('Click link about')

    # Methods

    def select_products_1(self):
        with allure.step("Select products_1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')
