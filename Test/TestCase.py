from Pages1.HomePage import Home
from Pages1.RegistrationPage import Register
from Utility.ReadExcel import readExcel
import unittest
import json
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class RegistrationTest(unittest.TestCase):

    def setUp(self):

        if readExcel('../Data/data.xlsx', 'Browser_Conf', 'A2') == "Yes":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):


        driver = self.driver
        with open('../Data/data.json') as json_file:
            data = json.load(json_file)
            driver.get('http://demo.guru99.com/test/newtours/')
            driver.save_screenshot('./ScreenShots/sc1.png')
            driver.set_page_load_timeout(20)
            m = Home(driver)
            m.getRegister().click()
            r = Register(driver)
            r.setFirstName(data['firstname'])
            r.setLastName(data['lastname'])
            r.setPhone(data['mobileno'])
            r.setCountry(data['country'])
            r.setEmail(data['emailid'])
            r.setUserName(data['lastname'])
            r.setPassword(data['password'])
            r.setConfirmPassword(data['password'])
            r.submitRegistration()

