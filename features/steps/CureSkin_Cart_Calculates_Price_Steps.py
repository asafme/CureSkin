from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open product details page of CureSkin Gentle Cleanse Face Foam')
def open_product_details(context):
    context.app.main_page.open_product_details_url()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.main_page.click_add_to_cart()


@when('Store the current price')
def verify_original_price(context):
    context.app.search_result.verify_original_price()


@then('Click plus icon to increase product quantity')
def click_increase_quantity(context):
    sleep(5)
    context.app.search_result.click_increase_quantity()
    sleep(10)


@then('Verify price has doubled')
def verify_doubled_price(context):
    context.app.search_result.verify_doubled_price()


@then('Verify cart has {expected_amount} items')
def verify_subtotal(context, expected_amount):
    context.app.search_result.verify_subtotal(expected_amount)