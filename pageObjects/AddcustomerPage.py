import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class AddCustomer:

    lnkCustomers_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    txtCustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administartors')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgeOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
         self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgeOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_id(self.txtDob_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()








