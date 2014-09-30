from selenium import webdriver
from pages.homepage import Homepage 

def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.page = Homepage(context.driver)
    context.page.navigate()

def after_scenario(context, scenario):
    context.driver.implicitly_wait(10)
    context.driver.quit()