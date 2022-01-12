import time
from beeping import beep
from login import login

WAIT_TIME = 0.5
def rdvVacFinder(driver, url, user, password): 
    driver = login(driver, user, password)
    driver.get(url)
    while True:
        isRdVMess = driver.find_elements_by_css_selector(".booking-error-title")  
        isVac = driver.find_elements_by_css_selector(".dl-mobile-availabilities")  
        
        if len(isVac) > 0 :
            print(isVac)
            print(isVac[0].get_attribute("innerHTML"))
            #beep()
            break
        elif len(isRdVMess) > 0 : 
            driver.refresh()
        else:
            time.sleep(WAIT_TIME)
