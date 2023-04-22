from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResult(Page):
    SEARCH_RESULT = (By.ID, "ProductCount")
    IMAGE = (By.ID, "Slide-template--17185951023421__main-33409574699325")
    PRICE = (By.CSS_SELECTOR, ".price--large")

    def verify_results_shown(self):
        self.wait_for_element_appear(*self.SEARCH_RESULT)


    def verify_image(self):
        self.find_element(*self.IMAGE)


    def verify_price(self):
        self.find_element(*self.PRICE)