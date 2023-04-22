from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on the product from search results')
def click_product(context):
    sleep(5)
    context.app.header.click_product()


@then('Verify image is present')
def verify_image(context):
    context.driver.find_element(By.ID, "Slide-template--17185951023421__main-33409574699325")


@then('Verify price is present')
def verify_price(context):
    context.driver.find_element(By.CSS_SELECTOR, ".price--large")


@then('Verify reviews are present')
def verify_reviews(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.jdgm-prev-badge__text")


@then('Verify add to cart is present')
def verify_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".product-form__submit")


@then('Verify buy it now button is present')
def verify_buy_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".shopify-payment-button")
