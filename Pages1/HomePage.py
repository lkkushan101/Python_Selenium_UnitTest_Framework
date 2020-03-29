from selenium.webdriver.common.by import By

from Pages1.Locators import Locator


class Home(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.sign_on = driver.find_element(By.XPATH, Locator.sign_on)
        self.contact = driver.find_element(By.XPATH, Locator.contact)
        self.support = driver.find_element(By.XPATH, Locator.support)
        self.register = driver.find_element(By.XPATH, Locator.register)

    def getLogo(self):
        return self.logo

    def getSignOn(self):
        return self.sign_on

    def getContact(self):
        return self.contact

    def getSupport(self):
        return self.support

    def getRegister(self):
        return self.register