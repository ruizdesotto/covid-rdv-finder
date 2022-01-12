from selenium import webdriver

def getChromeDriver(path):
    mobile_emulation = { "deviceName": "Pixel 2" }
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_argument("window-size=400,800")

    driver = webdriver.Chrome(executable_path = path, options=opts)
    return driver
