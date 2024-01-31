import time

import pytest
from selenium import webdriver
from pagesObjects.LoginPage import Login
from pagesObjects.AddCustomerPage import AddCustomer
from pagesObjects.SearchCustomerPage import SearchCustomer
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_searchCustomerByName_005():
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** Starting Test_SearchCustomerByName_005 ************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("************* Login Successful *************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickONCustomerMenu()
        self.addcust.clickOnCustomerSubMenu()

        self.logger.info("************ Starting Search Customer by Name *************")

        self.logger.info("*********** Searching Customer by Name ************")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName('Terces')
        self.searchcust.clickSearch()
        time.sleep(5)
        Name = "Victoria Terces"
        status = self.searchcust.searchCustomerByName(Name)
        self.driver.close()
        assert True == status
        self.logger.info("*********** Test_SearchCustomerByName_005 Finished ************")