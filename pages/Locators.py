
class Locator(object):
    #Home Page
    login = "//button[contains(.,'Log In')]"
    sign_up = "//span[contains(.,'Sign Up')]"
    search_button = "//button[@value='']"
    search_bar = "//input[@id='search-box-input']"
    
    #Search page
    filters = "//*[@id='wideSidepaneFilterButtonContainer']/button"
    home_type = "//*[@id='propertyTypeFilter']/div[1]/button[1]"
    add_bath = '//*[@id="filterContent"]/div/div[1]/div[1]/div[2]/div[2]/span/span/span[3]'
    garage = '//*[@id="filterContent"]/div/div[4]/div[2]/div[1]/div[1]/div[1]/span/label/input'
    apply_filter = '//*[@id="searchForm"]/form/div[2]/div/div/button'