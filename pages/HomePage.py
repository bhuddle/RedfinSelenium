from Locators import Locator
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class HomePage(object):

    def __init__(self, driver):
        #setting driver
        self.browser = driver
        
        #setting locators
        self.login = driver.find_element(By.XPATH, Locator.login)
        self.sign_up = driver.find_element(By.XPATH, Locator.sign_up)
        self.search_button = driver.find_element(By.XPATH, Locator.search_button)
        self.search_bar = driver.find_element(By.XPATH, Locator.search_bar)
        
    
    def getLogin(self):
        return self.login
        
        
    def getSignUp(self):
        return self.sign_up
        
        
    def getSearchButton(self):
        return self.search_button
        
        
    def getSearchBar(self):
        return self.search_bar
    
    
    def getLoginPage(self):
        # Not implementing past a click
        self.login.click()
    
    
    def getSignUpPage(self):
        # Not implementing past a click
        self.sign_up.click()
        
        
    def setSearchZipResult(self, zip):
        self.search_bar.clear()
        self.search_bar.send_keys(zip)
        self.search_button.click()
        return self.browser
        
    
    def setSearchCityResult(self, city):
        self.search_bar.clear()
        self.search_bar.send_keys(city)
        self.search_button.click()
        return self.browser


        
"""
browser = webdriver.Chrome('C:\Chromedriver\chromedriver.exe')
browser.get('http://redfin.com/')
browser.set_page_load_timeout(20)
home = HomePage(browser)
home.getSearchZipResult('97123')
sleep(2)
home.clickSearchButton()"""