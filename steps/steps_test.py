from selenium import webdriver
from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not
from pages.homepage import Homepage

@given('I am at the natgeo homepage')
def step(context):
    assert_that(context.driver.current_url, equal_to("http://www.nationalgeographic.com/"))

@then('the logo should be displayed')
def step(context):
    assert_that(context.page.is_logo_displayed)
