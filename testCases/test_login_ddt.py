import time
import pytest
from selenium import webdriver
from pagesObjects.LoginPage import Login
from utilities.customlogger import LogGen
from utilities import XLUtils
from utilities.readproperties import ReadConfig

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********** Test_002_DDT_Login ********")
        self.logger.info("**** Started Login Test ****")
        self.driver = setup

        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = []

        #Write Data in Sheet 2
        XLUtils.writeData(self.path,'Sheet2',1,1,'Username')
        XLUtils.writeData(self.path, 'Sheet2', 1, 2, 'Password')
        XLUtils.writeData(self.path, 'Sheet2', 1, 3, 'Exp Result')
        XLUtils.writeData(self.path, 'Sheet2', 1, 4, 'Actual Result')



        for r in range(2,self.rows+1):
            time.sleep(2)
            #Read data from sheet 1
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)
            #Write data in sheet 2
            XLUtils.writeData(self.path,'Sheet2',r,1,self.user)
            XLUtils.writeData(self.path, 'Sheet2', r, 2, self.password)
            XLUtils.writeData(self.path, 'Sheet2', r, 3, self.exp)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(1)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if exp_title == act_title:
                if self.exp == "Pass":
                    self.logger.info("**** Test Passed ****")
                    self.lp.clickLogOutButton()
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet2', r, 4, "Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Test Failed ****")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet2', r, 4, "Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("**** Test Failed ****")
                    st_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet2', r, 4, "Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Test passed ****")
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet2', r, 4, "Pass")


        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test Failed ***")
            self.driver.close()
            assert False

        self.logger.info("**** End of Login DDT Test ****")
        self.logger.info("********** Completed TC_LoginDDT_002 ********")
