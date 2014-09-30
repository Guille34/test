from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Homepage(object):
    
    _logo = (By.XPATH, "//a[@href = 'http://www.nationalgeographic.com/']")
    _search = (By.ID, "header_search_input")
    _animals_tab = (By.LINK_TEXT, "Animals")
    #_animals_home_subtab = (By.LINK_TEXT, "Animals Home")

    def __init__(self, driver):
        self.driver = driver
    
    def navigate(self):
        self.driver.get("http://www.nationalgeographic.com/")
    
    def is_logo_displayed(self):
        return self.driver.find_element(*self._logo).is_displayed()
    
    def fill_search(self, word):
        self.driver.find_element(*self._search).send_keys(word)

    def submit_search(self):
        self.driver.find_element(*self._search).send_keys(Keys.RETURN)
    
    def hover_animals_tab(self):
        elem = self.driver.find_element(*self._animals_tab)
        ActionChains(self.driver).move_to_element(elem)
        elem.click()
        
    def click_animals_home_subtab(self):
        self.driver.find_element_by_link_text('Animals Home').click()