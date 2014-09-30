from selenium.webdriver.common.by import By

class Search(object):
    
    _article = (By.CLASS_NAME, "text_right")

    def __init__(self, driver):
        self.driver = driver
    
    def is_article_displayed(self):
        return self.driver.find_element(*self._article).is_displayed()