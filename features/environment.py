from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.application import Application


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

    # service = Service('/Users/jessicamenashe/asafme/CureSkin/chromedriver')

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

    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
