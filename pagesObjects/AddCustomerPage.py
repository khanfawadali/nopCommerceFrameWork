import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    #Add Customer
    customersMenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customersSubMenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addNew_Xpath = "//a[normalize-space()='Add new']"
    email_Textbox_xpath = "//input[@id='Email']"
    password_textbox_xpath = "//input[@id='Password']"
    firstname_textbox_xpath = "//input[@id='FirstName']"
    lastname_textbox_xpath = "//input[@id='LastName']"
    maleGender_id = "Gender_Male"
    femaleGender_id = "Gender_Female"
    dob_textbox_xapth = "//input[@id='DateOfBirth']"
    companyName_textbox_xpath = "//input[@id='Company']"
    isTaxExempt_checkbox_id = "IsTaxExempt"
    newsLetter_textbox_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    newsLetter_yourstore_xpath = "//li[normalize-space()='Your store name']"
    newsLetter_TestStore_xpath = "//li[normalize-space()='Test store 2']"
    customerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    customerRoles_Registered_xpath = "//li[normalize-space()='Registered']"
    customerRoles_Administrators_xpath = "//li[normalize-space()='Administrators']"
    customerRoles_Guests_xpath = "//li[normalize-space()='Guests']"
    customerRoles_Vendors_xpath ="//li[contains(text(),'Vendors')]"
    customerRoles_ForumModerators_xpath ="//li[normalize-space()='Forum Moderators']"
    manager_of_vendor_xpath = "//select[@id='VendorId']"
    active_checkbox_xpath = "Active"
    admin_commnet_xpath = "//textarea[@id='AdminComment']"
    saveButton_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickONCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customersMenu_xpath).click()
        time.sleep(1)

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.customersSubMenu_xpath).click()
        time.sleep(1)

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.addNew_Xpath).click()
        time.sleep(1)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_Textbox_xpath).send_keys(email)
        time.sleep(1)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)
        time.sleep(1)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(fname)
        time.sleep(1)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(lname)
        time.sleep(1)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.maleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.femaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.maleGender_id).click()
        time.sleep(1)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.dob_textbox_xapth).send_keys(dob)
        time.sleep(1)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH, self.companyName_textbox_xpath).send_keys(comname)
        time.sleep(1)

    def setTaxExempt(self, txempt):
        if txempt == True:
            self.driver.find_element(By.ID, self.isTaxExempt_checkbox_id).click()
            time.sleep(1)
        else:
            pass

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.newsLetter_textbox_xpath).click()
        time.sleep(1)
        if newsletter == "Test store 2":
            self.driver.find_element(By.XPATH, self.newsLetter_TestStore_xpath).click()
        elif newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.newsLetter_yourstore_xpath).click()
        else:
            pass
        time.sleep(1)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.customerRoles_xpath).click()
        time.sleep(1)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_Administrators_xpath)
        elif role == "Guests":
            #Here user can be registered (or) Guest, only one
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_Guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_Vendors_xpath)
        elif role == "Forum":
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_ForumModerators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.customerRoles_Guests_xpath)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.manager_of_vendor_xpath))
        drp.select_by_visible_text(value)
        time.sleep(1)

    def setActive(self, act):
        if act == True:
            self.driver.find_element(By.XPATH, self.active_checkbox_xpath).click()
        else:
            pass

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.admin_commnet_xpath).send_keys(comment)
        time.sleep(1)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.saveButton_xpath).click()
        time.sleep(1)