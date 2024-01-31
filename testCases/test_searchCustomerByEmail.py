import time
import pytest
from selenium import webdriver
from pagesObjects.LoginPage import Login
from pagesObjects.AddCustomerPage import AddCustomer
from pagesObjects.SearchCustomerPage import SearchCustomer
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********** Test_SearchCustomerByEmail_004 *************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        self.logger.info("************* Login Successful ***************")

        self.logger.info("************* Starting Search Customer By Email *************")\

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickONCustomerMenu()
        self.addcust.clickOnCustomerSubMenu()

        self.logger.info("*********** Searching Customer by emailID ************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()

        if status == True:
            assert True == status
            self.logger.info("********* Customer found ********")
            self.logger.info("*********** Test_SearchCustomerByEmail_004 Finished ************")
        else:
            self.logger.info("********* Customer not found ********")
            self.logger.info("*********** Test_SearchCustomerByEmail_004 Finished ************")
            assert False == status



