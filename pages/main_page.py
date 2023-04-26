from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    ADD_TO_CART = (By.CSS_SELECTOR, ".product-form__submit")
    INCREASE_QUANTITY = (By.XPATH, "//button[@class='quantity__button no-js-hidden']")
    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')


    def open_product_details_url(self):
        self.open_url('https://shop.cureskin.com/products/gentle-cleanse-face-foam?_pos=1&_sid=8aa60ef76&_ss=r')


    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)


