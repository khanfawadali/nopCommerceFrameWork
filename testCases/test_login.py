import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readproperties import ReadConfig
from pagesObjects.LoginPage import Login
from utilities.customlogger import LogGen

class Test_001_LoginTest():
    # baseUrl = "http://admin-demo.nopcommerce.com"
    baseUrl = ReadConfig.getApplicationURL()
    print(baseUrl)
    # username = "admin@yourstore.com"
    username = ReadConfig.getUserEmail()
    print(username)
    # password = "admin"
    password = ReadConfig.getPassword()
    print(password)
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("******* Test_001_Login ********")
        self.logger.info("********** Start Home Page Title test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        a_title = self.driver.title
        actual_title = "Your store. Login"
        print(a_title)
        time.sleep(2)
        if a_title == actual_title:
            self.logger.info("****** Home Page Title test Passed ******")
            print("Test Passed")
        else:
            self.logger.info(("****** Home Page Title test Failed ******"))
            print("Test Failed")

        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginPage(self,setup):
        self.logger.info("********** Started Login Test *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        # time.sleep(3)
        # self.driver.find_element(By.ID, "Email").clear()
        # self.driver.find_element(By.ID, "Email").send_keys(self.username)
        self.lp.setPassword(self.password)
        # time.sleep(2)
        # self.driver.find_element(By.ID, "Password").clear()
        # self.driver.find_element(By.ID,"Password").send_keys(self.password)
        self.lp.clickLoginButton()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(3)
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            self.logger.info("******* Login Test Passed ********")
            print("Test Passed")
            self.lp.clickLogOutButton()
        else:
            self.logger.info("******* Login Test Failed *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "LoginTestTitle1.png")
            print("Test Failed")

        self.driver.close()