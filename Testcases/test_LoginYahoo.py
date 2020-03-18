from Base import Initialise_Browser
from Library import ConfigReader

import time

def test_Loginpage():

    driver =Initialise_Browser.startBrowser()
    driver.find_element_by_xpath(ConfigReader.Login('Login', 'login')).click()
    driver.find_element_by_xpath(ConfigReader.Login('Login', 'username')).send_keys("raghavan8007")
    driver.find_element_by_xpath(ConfigReader.Login('Login', 'password')).send_keys("Akhil@007")
    #driver.find_element_by_xpath("//input[@type='checkbox']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(ConfigReader.Login('Login', 'signin')).click()
    #time.sleep(5)
    #elem = driver.find_element_by_xpath(ConfigReader.Login('Login', 'view me'))



