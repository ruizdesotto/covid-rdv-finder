import time
from env.variables import URL_LOG

wait_time = 0.05

def login(driver, user, password):
    # Login page
    driver.get(URL_LOG)

    # Cookies 
    while driver.find_element_by_id("didomi-notice-agree-button") == None:
        time.sleep(wait_time)
    driver.find_element_by_id("didomi-notice-agree-button").click()

    # Login credentials
    while driver.find_elements_by_id("username") == []:
        time.sleep(wait_time)
    driver.find_elements_by_id("username")[0].send_keys(user)
    driver.find_elements_by_id("password")[1].send_keys(password)
 
    # Login submit
    driver.find_elements_by_css_selector(
        ".Tappable-inactive.dl-button-DEPRECATED_yellow.dl-toggleable-form-button.dl-button.dl-button-block.dl-button-size-normal"
        )[0].click()
    
    # Wait success
    while driver.find_elements_by_css_selector(".dl-view.account-appointments") == []:
        time.sleep(wait_time)
        
    return driver
    