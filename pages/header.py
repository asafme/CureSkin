from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.common.keys import Keys


class Header(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, ".icon.icon-search.modal__toggle-open")
    CURESKIN_SEARCH_FIELD = (By.ID, "Search-In-Modal")
    PRODUCT = (By.CSS_SELECTOR, ".full-unstyled-link")



    def click_search(self):
        self.click(*self.SEARCH_ICON)


    def input_search_text(self, text):
        self.input_text(text, *self.CURESKIN_SEARCH_FIELD)
        self.input_text(Keys.ENTER, *self.CURESKIN_SEARCH_FIELD)

    def click_product(self):
        self.click(*self.PRODUCT)