import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page


class Users_page(Base_page):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # all clicks
        self.users_click_xpath = "//a[@routerlink='/manage-users']"

        # add user
        self.users_addUsr_click_xpath = "//body/app-root/div/app-manage-user-page/div/div/div/button[@type='button']/span[2]"
        self.usr_FN_click_xpath =  "//input[@placeholder='First Name']"
        self.usr_LN_click_xpath = "//input[@placeholder='Last Name']"
        self.usr_Email_click_xpath = "//input[@placeholder='Email']"
        self.usr_cntycode_click_xpath = "//span[@ng-reflect-ng-class='[object Object]']"
        self.usr_cntycode_search_click_xpath = "(//input[@autocomplete='off'])[1]"
        self.usr_cntycode_searchbox_xpath = "//ul[@role='listbox']"
        self.usr_Ph_no_click_xpath = "//input[@placeholder='1234567890']"
        self.usr_RemitCenter_click_xpath = "(//select[@formcontrolname='centerId'])[1]"
        self.usr_Role_click_xpath = "//select[@formcontrolname='role']"
        self.usr_Password_click_xpath = "//input[@placeholder='Password']"
        self.usr_save_button_click_xpath = "//button[@type='submit']"

        # small search bars
        self.usr_S_FN_xpath = "//th[1]//input[1]"
        self.usr_S_LN_xpath = "//th[2]//input[1]"
        self.usr_S_Phone_xpath = "//th[3]//input[1]"
        self.usr_S_Email_xpath = "//th[4]//input[1]"
        self.usr_S_Role_xpath = "//th[5]//input[1]"
        self.usr_S_Center_xpath = "//th[6]//input[1]"

        # Actions
        # Edit
        self.usr_edit_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/div[2]/" \
                                "div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[1]"
        # Delete
        self.usr_delete_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[2]/span[1]"
        # e/d ok
        self.usr_e_d_ok_button_xpath = "//ngb-modal-window[@role='dialog']//button[2]"

    # Clicks and Actions
    def user_click(self):
        self.driver.find_element(By.XPATH,  self.users_click_xpath).click()
        time.sleep(2)

    def adduser_click(self):
        self.driver.find_element(By.XPATH,   self.users_addUsr_click_xpath).click()
        time.sleep(2)

    def usr_FN(self, firstname):
        self.driver.find_element(By.XPATH, self.usr_FN_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_FN_click_xpath).send_keys(firstname)

    def usr_LN(self, lastname):
        self.driver.find_element(By.XPATH, self.usr_LN_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_LN_click_xpath).send_keys(lastname)

    def usr_Email(self, Email):
        self.driver.find_element(By.XPATH, self.usr_Email_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Email_click_xpath).send_keys(Email)

    # driver.find_element(By.XPATH, "//p-dropdownitem[@ng-reflect-option='[object Object]']")
    def usr_country_code(self):
        self.driver.find_element(By.XPATH, self.usr_cntycode_click_xpath).click()
        self.driver.find_element(By.XPATH,   self.usr_cntycode_search_click_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.usr_cntycode_search_click_xpath).send_keys("91")
        code_search_results = self.driver.find_elements(By.XPATH, self.usr_cntycode_searchbox_xpath)
        print(code_search_results)
        print(len(code_search_results))
        for results in code_search_results:
            if "+91" in results.text:
                results.click()
                break

    def usr_Phone_no(self, Ph_no):
        self.driver.find_element(By.XPATH, self.usr_Ph_no_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Ph_no_click_xpath).send_keys(Ph_no)

    def usr_RemitCenter_click(self):
        self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath))
        select.select_by_value("Newyork center")
        print("selected item - " + select.first_selected_option.text)
        assert "Newyork center" in select.first_selected_option.text

    def usr_Role_click(self):
        self.driver.find_element(By.XPATH, self.usr_Role_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_Role_click_xpath))
        select.select_by_value("MANAGER")
        print("selected item - " + select.first_selected_option.text)
        assert "MANAGER" in select.first_selected_option.text

    def usr_password(self, password):
        self.driver.find_element(By.XPATH, self.usr_Password_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Password_click_xpath).send_keys(password)

    def usr_save_button_click(self):
        self.driver.find_element(By.XPATH,  self.usr_save_button_click_xpath).click()
        time.sleep(2)

    # small searchbars
    def usr_FN_s_searchbars(self,usr_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(usr_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).get_attribute("value") == "Jack"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "Jack"
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def usr_v1_FN_s_searchbars(self, eusr_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(eusr_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).get_attribute("value") == "Jack"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "Jack"
        # self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    # def nr_v2acp_FN_s_searchbars(self, eacp_ss_FN_bar):
    #     self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(eacp_ss_FN_bar)
    #     assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "Robert1"
    #     time.sleep(3)
    #     ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
    #     assert ele == "Robert1"

    def usr_v2_eFN_s_searchbars(self, eusr_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(eusr_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).get_attribute("value") == "Jacky"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "Jacky"
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.usr_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def usr_LN_s_searchbars(self, usr_ss_LN_bar):
        self.driver.find_element(By.XPATH, self.usr_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_LN_xpath).send_keys(usr_ss_LN_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_LN_xpath).get_attribute("value") == "stark"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "stark"
        self.driver.find_element(By.XPATH, self.usr_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def usr_Email_s_searchbars(self, usr_ss_email_bar):
        self.driver.find_element(By.XPATH, self.usr_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_Email_xpath).send_keys(usr_ss_email_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_Email_xpath).get_attribute("value") == "rob@gmail.com"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        assert ele == "rob@gmail.com"
        self.driver.find_element(By.XPATH, self.usr_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def usr_Phone_s_searchbars(self, usr_ss_ph_bar):
        self.driver.find_element(By.XPATH, self.usr_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_S_Phone_xpath).send_keys(usr_ss_ph_bar)
        assert self.driver.find_element(By.XPATH, self.usr_S_Phone_xpath).get_attribute("value") == "7774446661"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele == "7774446661"
        self.driver.find_element(By.XPATH, self.usr_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def usr_Role_s_searchbars(self):
        self.driver.find_element(By.XPATH, self.usr_Role_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_Role_click_xpath))
        select.select_by_value("MANAGER")
        print("selected item - " + select.first_selected_option.text)
        assert "MANAGER" in select.first_selected_option.text

    def usr_RCenter_s_searchbars(self):
        self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath))
        select.select_by_value("Newyork")
        print("selected item - " + select.first_selected_option.text)
        assert "Newyork" in select.first_selected_option.text

    # Actions
    # Edit/Delete
    def usr_editbutton_click(self):
        self.driver.find_element(By.XPATH, self.usr_edit_xpath).click()

    def usr_eFN(self, efirstname):
        self.driver.find_element(By.XPATH, self.usr_FN_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_FN_click_xpath).send_keys(efirstname)

    def usr_eLN(self, elastname):
        self.driver.find_element(By.XPATH, self.usr_LN_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_LN_click_xpath).send_keys(elastname)

    def usr_eEmail(self, eEmail):
        self.driver.find_element(By.XPATH, self.usr_Email_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Email_click_xpath).send_keys(eEmail)

    def usr_ecountry_code(self):
        self.driver.find_element(By.XPATH, self.usr_cntycode_click_xpath).click()
        self.driver.find_element(By.XPATH,   self.usr_cntycode_search_click_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.usr_cntycode_search_click_xpath).send_keys("91")
        code_search_results = self.driver.find_elements(By.XPATH, self.usr_cntycode_searchbox_xpath)
        print(code_search_results)
        print(len(code_search_results))
        for results in code_search_results:
            if "+91" in results.text:
                results.click()
                break

    def usr_ePhone_no(self, ePh_no):
        self.driver.find_element(By.XPATH, self.usr_Ph_no_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Ph_no_click_xpath).send_keys(ePh_no)

    def usr_eRemitCenter_click(self):
        self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_RemitCenter_click_xpath))
        select.select_by_value("Newyork center")
        print("selected item - " + select.first_selected_option.text)
        assert "Newyork center" in select.first_selected_option.text

    def usr_eRole_click(self):
        self.driver.find_element(By.XPATH, self.usr_Role_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.usr_Role_click_xpath))
        select.select_by_value("ADMIN")
        print("selected item - " + select.first_selected_option.text)
        assert "ADMIN" in select.first_selected_option.text

    def usr_epassword(self, epassword):
        self.driver.find_element(By.XPATH, self.usr_Password_click_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.usr_Password_click_xpath).send_keys(epassword)

    def usr_esave_button_click(self):
        self.driver.find_element(By.XPATH,  self.usr_save_button_click_xpath).click()
        time.sleep(2)

    def usr_Del_ok_button_click(self):
        self.driver.find_element(By.XPATH, self.usr_delete_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.usr_e_d_ok_button_xpath).click()
        time.sleep(5)
