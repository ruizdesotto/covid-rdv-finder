from src.rdvBot import rdvVacFinder
from src.driver import getChromeDriver
from env.variables import URL_0, user, password, path

if __name__ == "__main__":
    driver = getChromeDriver(path)
    rdvVacFinder(driver, URL_0, user, password)
    