import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer():
    #Locators
    search_email_xpath = "//input[@id='SearchEmail']"
    search_fname_xpath = "//input[@id='SearchFirstName']"
    search_lname_xpath = "//input[@id='SearchLastName']"
    search_button_xpath = "//button[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver


    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.search_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_email_xpath).send_keys(email)
        time.sleep(1)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.search_fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_fname_xpath).send_keys(fname)
        time.sleep(1)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.search_lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_lname_xpath).send_keys(lname)
        time.sleep(1)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        time.sleep(1)


    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))


    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag