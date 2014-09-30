from selenium import webdriver
from behave   import given, when, then 
from hamcrest import assert_that, equal_to, is_not
from pages.animals import Animals

@when('I click in the animals tab')
def step(context):
    context.page.hover_animals_tab()
    context.page2 = Animals(context.driver)
    #context.page.click_animals_home_subtab()

@when("I click in domestic dogs")
def step(context):
    context.page2.fill_quick_search("dog")
    context.page2.click_domestic_dog_link()
    
@then('I wait')
def step(context):
    context.driver.implicitly_wait(10)
