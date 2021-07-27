import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_03_AddCustomer:
    baseURL  = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):

        self.logger.info("*************** Test_013_AddCustomer ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*************** Login Succesful ***************")
        self.logger.info("*************** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("*************** Providing Customer Info ***************")

        self.email = random_generator()+ "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Akhil")
        self.addcust.setLastName("Siri")
        self.addcust.setDob("08/03/1996")
        self.addcust.setCompanyName("Oasis")
        self.addcust.setAdminContent("Testing World")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving Customer Info ***************")
        self.logger.info("*************** Add Customer Validation Started ***************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************** Add Customer Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("*************** Add Customer Test Failed ***************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending Home Page Title Test ***************")


def random_generator(size=8, chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



