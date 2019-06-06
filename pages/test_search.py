from HomePage import *
from SearchFilterView import *
import pytest, re

browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
browser.get('http://redfin.com/')
browser.set_page_load_timeout(20)
home = HomePage(browser)

def returnHome():
    home.browser.get('http://redfin.com/')

def test_setup():
    state = home.browser.execute_script('return document.readyState')
    print(state)
    if state == 'complete':
        assert True
    else:
        assert False
    
#get url and verify zip
def test_zip():
    sleep(3)
    home.setSearchZipResult('97123')
    if '97123' in home.browser.current_url:
        assert True
        

def test_search():
    search = SearchFilterView(home.browser)
    sleep(3)
    search.setFilter()
    sleep(3)
    search.setHomeType()
    search.setAddBath()
    search.setGarage()
    sleep(3)
    print(search.browser.page_source)
    if re.search(r'94 Homes', search.browser.page_source) != None:
        assert True
    else:
        assert False
        

"""def test_city():
    sleep(3)
    home.setSearchCityResult('Hillsboro')
    if 'Hillsboro' in home.browser.current_url:
        assert True"""
    
    
    
def test_teardown():
    sleep(3)
    browser.close()
    home.browser.close()
    sleep(3)
    if browser == None:
        assert True