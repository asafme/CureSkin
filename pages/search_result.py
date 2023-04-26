from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResult(Page):
    SEARCH_RESULT = (By.ID, "ProductCount")
    IMAGE = (By.ID, "Slide-template--17185951023421__main-33409574699325")
    PRICE = (By.CSS_SELECTOR, ".price--large")
    ORIGINAL_PRICE = (By.XPATH, "//span[@class='price-item price-item--sale']/price-money/bdi")
    INCREASE_QUANTITY = (By.XPATH, "//button[@class='quantity__button no-js-hidden'][@name='plus']")
    DOUBLE_PRICE = (By.ID, "mini-cart-subtotal")
    VERIFY_SUBTOTAL = (By.ID, "Quantity-1")

    def verify_results_shown(self):
        self.wait_for_element_appear(*self.SEARCH_RESULT)


    def verify_image(self):
        self.find_element(*self.IMAGE)


    def verify_price(self):
        self.find_element(*self.PRICE)


    def verify_original_price(self):
       self.driver.original_price = self.wait_for_element_appear(*self.ORIGINAL_PRICE).text

    def click_increase_quantity(self):
        self.click(*self.INCREASE_QUANTITY)


    def verify_doubled_price(self):
        double_expected_price = float(self.driver.original_price.replace('Rs.','')) * 2
        actual_price = self.find_element(*self.DOUBLE_PRICE).text.replace('Rs.','')
        assert double_expected_price == float(actual_price), f'Expected {double_expected_price} but got  {actual_price}'


    def verify_subtotal(self,expected_amount):
        actual_text = self.find_element(*self.VERIFY_SUBTOTAL).text
        expected_text = f"Subtotal ({expected_amount} item):"



