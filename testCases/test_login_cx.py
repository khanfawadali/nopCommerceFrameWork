import pytest
import time
from selenium import webdriver
from pagesObjects.LoginPage import Login
from pagesObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
from selenium.webdriver.common.by import By
import string
import random

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("*********** Login Successful **********")

        self.logger.info("*********** Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickONCustomerMenu()
        self.addcust.clickOnCustomerSubMenu()

        self.addcust.clickOnAddnew()

        self.logger.info("********* Providing Customer info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Fawad")
        self.addcust.setLastName("Khan")
        self.addcust.setGender("Male")
        self.addcust.setDOB("9/30/1990")
        self.addcust.setCompanyName("Khan's QA")
        self.addcust.setTaxExempt(False)
        self.addcust.setNewsLetter("Test store 2")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setActive(False)
        self.addcust.setAdminComment("This is for testing........")
        self.addcust.clickOnSave()

        self.logger.info("********** Saving Customer info ***********")

        self.logger.info("*********** Add Customer validation started **********")

        # self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        self.msg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            self.logger.info("******** Add Customer Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_screen.png")
            self.logger.info("********* Add Customer Test Failed *********")
            assert False

        self.driver.close()
        self.logger.info("******** Ending Add Customer Test *********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
