from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Animals(object):
    
    _quick_search = (By.ID, "q")
    _domestic_dog_link = (By.LINK_TEXT, "Domestic Dog")
    
    def __init__(self, driver):
        self.driver = driver
    
    def fill_quick_search(self, text):
        self.driver.find_element(*self._quick_search).send_keys(text)
    
    def click_domestic_dog_link(self):
        self.driver.find_element(*self._domestic_dog_link).click()
    
    
    