from selenium import webdriver
from selenium.webdriver import Chrome
from Library import ConfigReader
def startBrowser():

    global driver
    if(ConfigReader.configRead('Details','Browser')=="Chrome"):
        path = "./Drivers/chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get(ConfigReader.configRead('Details', 'url'))

        driver.maximize_window()
        return driver


def closeBrowser():
    driver.close()