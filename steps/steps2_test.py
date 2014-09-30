from selenium import webdriver
from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not
from pages.homepage import Homepage
from pages.search import Search

@when('I fill de search and submit it')
def step(context):
    context.page.fill_search("cat")
    context.page.submit_search()
    
@then('I should see the results')
def step(context):
    context.page2 = Search(context.driver)
    assert_that(context.page2.is_article_displayed)
    