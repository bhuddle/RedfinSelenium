from Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import re
#SearchFilterView

class SearchFilterView(object):

    def __init__(self, driver):
        self.browser = driver
    
        self.filters = driver.find_element(By.XPATH, Locator.filters)
        
    def setFilter(self):
        self.filters.click()
        
        
    def setHomeType(self):
        self.home_type = self.browser.find_element(By.XPATH, Locator.home_type)
        self.browser.execute_script('arguments[0].click();', self.home_type)
        
        
    def setAddBath(self):
        self.add_bath = self.browser.find_element(By.XPATH, Locator.add_bath)
        self.browser.execute_script('arguments[0].click();', self.add_bath)
        
        
    def setGarage(self):
        self.garage = self.browser.find_element(By.XPATH, Locator.garage)
        self.browser.execute_script('arguments[0].click();', self.garage)
        
        
        
    def setApplyFilter(self):
        self.apply_filter = self.browser.find_element(By.XPATH, Locator.garage)
        self.browser.execute_script('arguments[0].click();', self.apply_filter)
        

    
    
"""browser = webdriver.Chrome('C:\Chromedriver\chromedriver.exe')
browser.get('http://redfin.com/zipcode/97123/')
browser.set_page_load_timeout(20)
search = SearchFilterView(browser)
state = search.browser.execute_script('return document.readyState')
print(state)
search.setFilter()
sleep(5)
search.setHomeType()
search.setAddBath()
search.setGarage()
sleep(5)
print(re.search(r'94 Homes', search.browser.page_source))

sleep(20)
browser.close()"""