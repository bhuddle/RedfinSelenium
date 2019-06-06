from HomePage import *
from SearchFilterView import *
import pytest, re

#Setting up initial browser for testing
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
browser.get('http://redfin.com/')
browser.set_page_load_timeout(20)
home = HomePage(browser)


# Checking for page load
def test_setup():
    state = home.browser.execute_script('return document.readyState')
    print(state)
    if state == 'complete':
        assert True
    else:
        assert False
    

# Search zip and check if URL has changed
def test_zip():
    sleep(3)
    home.setSearchZipResult('97123')
    if '97123' in home.browser.current_url:
        assert True
        
        
# Apply filters and check if page has changed number of homes available
def test_search():
    search = SearchFilterView(home.browser)
    sleep(3)
    search.setFilter()
    sleep(3)
    search.setHomeType()
    search.setAddBath()
    search.setGarage()
    sleep(3)
    if re.search(r'94 Homes', search.browser.page_source) != None:
        assert True
    else:
        assert False
       
       
# Close session gracefully   
def test_teardown():
    sleep(3)
    browser.close()
    sleep(3)
    if browser == None:
        assert True