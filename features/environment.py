import allure
from allure_commons.types import AttachmentType
from behave.configuration import options

from app.application import Application

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.chrome.service import Service

from support.logger import logger, MyListener


def browser_init(context):
    """
    :param context: Behave context
    """
    # ############# CHROME ############
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(executable_path="../chromedriver", options=options)
    # #################################

    ######### FIREFOX ##############
    # options = FirefoxOptions()
    # options.headless = True
    # context.driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    # ################################

    service = Service('/Users/jessicamenashe/asafme/CureSkin/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # # options.add_argument("--window-size=1920,1080")
    # # options.add_argument("--sta
    #
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=Service('/Users/jessicamenashe/asafme/CureSkin/chromedriver')
    # )

    ###### for browserstack ########
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     # 'name': test_name
    # }
    # bs_user = 'jessicamenashe_zDS1Ke'
    # bs_key = 'HFiUD7M9VxyaRXsHEfkS'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # Mobile-Web Emulator
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    # browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')



def after_step(context, step):
    logger.error(f'Step failed: {step}')
    print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
