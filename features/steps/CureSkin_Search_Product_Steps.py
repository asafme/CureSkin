from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open CureSkin main page')
def open_cureskin_page(context):
    context.app.main_page.open_main_url()


# @when('Click on search button')
# def click_search_button(context):
#     context.app.header.click_search()


@when('Input text {text}')
def input_search_word(context, text):
    context.app.header.input_search_text(text)

@when("Close popup window")
def close_popup(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, ".popup-close").click()


@when('Click on search button')
def click_search_button(context):
    context.app.header.click_search()




