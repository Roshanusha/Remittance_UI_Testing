import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page


class Customers_Beneficiary_page(Base_page):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # All clicks
        self.cust_click_xpath = "//a[normalize-space()='Customers']"

        # Add Customer(BENEFICIARY)
        # self.nfig_click_xpath = "//a[@routerlink='/xchange-config']"
        self.cust_addconfig_click_xpath = "//span[normalize-space()='Add Customer']"
        self.cust_benef_radioB_click_xpath = "//p-radiobutton[@value='Beneficiary']//div[@ng-reflect-ng-class='[object Object]']//div[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACB_Title_xpath = "//select[@aria-label='Default select example']"  # From Currency
        self.cust_ACB_FN_xpath = "//input[@placeholder='First name']"  # fist name
        self.cust_ACB_MN_xpath = "//input[@placeholder='Middle name']"
        self.cust_ACB_LN_xpath = "//input[@placeholder='Last name']"
        self.cust_ACB_Nationality_xpath = "//p-dropdown[@id='ddNationality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACB_Nationality_search_xpath = "//input[@autocomplete='off']"
        self.cust_ACB_Nationality_searchbox_xpath = "//ul[@role='listbox']"
        self.cust_ACB_DOB_xpath = "//input[@placeholder='DOB']"
        self.cust_ACB_Email_xpath = "//input[@placeholder='Email']"
        self.cust_ACB_Ph_no_xpath = "//input[@placeholder='Phone Number']"
        self.cust_ACB_Passport_xpath = "//input[@placeholder='Passport']"
        self.cust_ACB_CUBAN_ID_xpath = "//input[@placeholder='Cuban ID']"
        self.cust_ACB_ZIP_xpath = "//input[@placeholder='Zip']"
        self.cust_ACB_city_xpath = "//input[@placeholder='City']"
        self.cust_ACB_muncipality_xpath = "//p-dropdown[@formcontrolname='municipality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACB_muncipality_search_xpath = "//input[@autocomplete='off'][1]"
        self.cust_ACB_muncipality_searchBOX_xpath = "(//ul[@role='listbox'])[1]"
        self.cust_ACB_Addr1_xpath = "//input[@placeholder='Line 1']"
        self.cust_ACB_Addr2_xpath = "//input[@placeholder='Line 2']"
        self.cust_ACB_state_xpath = "//p-dropdown[@formcontrolname='state']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACB_state_search_xpath = "(//input[@autocomplete='off'])[1]"
        self.cust_ACB_state_searchbox_xpath = "(//ul[@role='listbox'])[1]"
        self.cust_ACB_savebutton_click_xpath = "//span[normalize-space()='Save']"

        # Customers
        # #Global search bar
        self.cust_gsearchbar_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/" \
                                     "div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
        # small search bars
        self.cust_S_id_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                               "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[1]/input[1]"
        self.cust_S_FN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                               "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[2]/input[1]"
        self.cust_S_MN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                               "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[3]/input[1]"
        self.cust_S_LN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]" \
                               "/div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[4]/input[1]"
        self.cust_S_Phone_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[5]/input[1]"
        self.cust_S_Email_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[6]/input[1]"

        # Actions
        # Edit
        self.cust_editB_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/div[2]/" \
                                "div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[1]"
        # self.setDefault_button_xpath =  "//tbody/tr[1]/td[5]/button[3]/span[1]"

        # Delete
        self.cust_deleteB_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[2]/span[1]"
        # e/d ok
        self.cust_e_d_ok_button_xpath = "//ngb-modal-window[@role='dialog']//button[2]"

    # Clicks and Actions
    def customers_click(self):
        self.driver.find_element(By.XPATH, self.cust_click_xpath).click()

    def add_customer_click(self):
        self.driver.find_element(By.XPATH, self.cust_addconfig_click_xpath).click()

    def benef_radiobutton_click(self):
        radioB_button = self.driver.find_element(By.XPATH, self.cust_benef_radioB_click_xpath)
        radioB_button.click()

    def acb_title_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.cust_ACB_Title_xpath))
        select.select_by_value("Mrs")
        print("selected item - " + select.first_selected_option.text)
        assert "Mrs" in select.first_selected_option.text

    def acb_FN(self, firstname):
        self.driver.find_element(By.XPATH, self.cust_ACB_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_FN_xpath).send_keys(firstname)

    def acb_MN(self, middlename):
        self.driver.find_element(By.XPATH, self.cust_ACB_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_MN_xpath).send_keys(middlename)

    def acb_LN(self, lastname):
        self.driver.find_element(By.XPATH, self.cust_ACB_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_LN_xpath).send_keys(lastname)

    def acb_Nationality_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath).send_keys("Cuban")
        nationality_search_results = self.driver.find_elements(By.XPATH, self.cust_ACB_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "Cuban" in results.text:
                results.click()
                break

    def acb_DOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.cust_ACB_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_DOB_xpath).send_keys(dob)

    def acb_Email(self, emailid):
        self.driver.find_element(By.XPATH, self.cust_ACB_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Email_xpath).send_keys(emailid)

    def acb_Phone_No(self, phone):
        self.driver.find_element(By.XPATH,  self.cust_ACB_Ph_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,  self.cust_ACB_Ph_no_xpath).send_keys(phone)

    def acb_Passort(self, passport_no):
        self.driver.find_element(By.XPATH, self.cust_ACB_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Passport_xpath).send_keys(passport_no)

    def acb_Cuban_no(self, CUBAN_no):  # social security no
        self.driver.find_element(By.XPATH,  self.cust_ACB_CUBAN_ID_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,  self.cust_ACB_CUBAN_ID_xpath).send_keys(CUBAN_no)

    def acb_ZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.cust_ACB_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_ZIP_xpath).send_keys(zipcode)

    def acb_City(self, city):
        self.driver.find_element(By.XPATH, self.cust_ACB_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_city_xpath).send_keys(city)

    def acb_Muncipality(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).send_keys("CAIMITO")
        muncipality_search_results = self.driver.find_elements(By.XPATH,  self.cust_ACB_muncipality_searchBOX_xpath)
        print(muncipality_search_results)
        print(len(muncipality_search_results))
        for results in muncipality_search_results:
            if "CAIMITO" in results.text:
                results.click()
                break

    def acb_Addr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr1_xpath).send_keys(Addrline1)

    def acb_Addr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr2_xpath).send_keys(Addrline2)

    def acb_State_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_state_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_state_search_xpath).click()
            # print
        self.driver.find_element(By.XPATH, self.cust_ACB_state_search_xpath).send_keys("Texas")
        state_search_results = self.driver.find_elements(By.XPATH, self.cust_ACB_state_searchbox_xpath)
        print(state_search_results)
        print(len(state_search_results))
        for results in state_search_results:
            if "Texas" in results.text:
                results.click()
                break

    def acb_savebutton_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_savebutton_click_xpath).click()

    # small searchbars
    def acb_id_s_searchbars(self, acb_ss_id_bar):
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(acb_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acb_FN_s_searchbars(self, acb_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(acb_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Alicia"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Alicia"
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def v1acb_FN_s_searchbars(self, eacb_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(eacb_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Alicia"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Alicia"
        # self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def v2acb_FN_s_searchbars(self, eacb_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(eacb_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Alicia1"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Alicia1"

    def acb_MN_s_searchbars(self, acb_ss_MN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(acb_ss_MN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).get_attribute("value") == "Tom"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        #assert ele == "Tom1"
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acb_LN_s_searchbars(self, acb_ss_LN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(acb_ss_LN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).get_attribute("value") == "Gonzalez"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele == "Gonzalez"
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acb_Email_s_searchbars(self, acb_ss_email_bar):
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(acb_ss_email_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).get_attribute("value") == "ally@gmail.com"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[6]")).text
        assert ele == "ally@gmail.com"
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acb_Phone_s_searchbars(self, acb_ss_ph_bar):
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(acb_ss_ph_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).get_attribute("value") == "7775559991"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "7775559991"
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    # Edit
    def editbutton_customer_click(self):
        self.driver.find_element(By.XPATH, self.cust_editB_xpath).click()

    def acb_etitle_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.cust_ACB_Title_xpath))
        select.select_by_value("Mrs")
        print("selected item - " + select.first_selected_option.text)
        assert "Mrs" in select.first_selected_option.text

    def acb_eFN(self, firstname):
        self.driver.find_element(By.XPATH, self.cust_ACB_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_FN_xpath).send_keys(firstname)

    def acb_eMN(self, middlename):
        self.driver.find_element(By.XPATH, self.cust_ACB_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_MN_xpath).send_keys(middlename)

    def acb_eLN(self, lastname):
        self.driver.find_element(By.XPATH, self.cust_ACB_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_LN_xpath).send_keys(lastname)

    def acb_eNationality_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath).click()
            # print
        self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath).send_keys("Cuban")
        nationality_search_results = self.driver.find_elements(By.XPATH, self.cust_ACB_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "Cuban" in results.text:
                results.click()
                break

    def acb_eDOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.cust_ACB_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_DOB_xpath).send_keys(dob)

    def acb_eEmail(self, emailid):
        self.driver.find_element(By.XPATH, self.cust_ACB_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Email_xpath).send_keys(emailid)

    def acb_ePhone_No(self, phone):
        self.driver.find_element(By.XPATH, self.cust_ACB_Ph_no_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Ph_no_xpath).send_keys(phone)

    def acb_ePassort(self, passport_no):
        self.driver.find_element(By.XPATH, self.cust_ACB_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Passport_xpath).send_keys(passport_no)

    def acb_eCuban_no(self, ssn_no):  # social security no
        self.driver.find_element(By.XPATH, self.cust_ACB_CUBAN_ID_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_CUBAN_ID_xpath).send_keys(ssn_no)

    def acb_eZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.cust_ACB_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_ZIP_xpath).send_keys(zipcode)

    def acb_eCity(self, city):
        self.driver.find_element(By.XPATH, self.cust_ACB_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_city_xpath).send_keys(city)

    def acb_eMuncipality(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).send_keys("BAUTA")
        muncipality_search_results = self.driver.find_elements(By.XPATH, self.cust_ACB_muncipality_searchBOX_xpath)
        print(muncipality_search_results)
        print(len(muncipality_search_results))
        for results in muncipality_search_results:
            if "BAUTA" in results.text:
                results.click()
                break

    def acb_eAddr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr1_xpath).send_keys(Keys.CONTROL, 'a' , Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr1_xpath).send_keys(Addrline1)

    def acb_eAddr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr2_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACB_Addr2_xpath).send_keys(Addrline2)

    # def acb_eState_click(self):
    #     self.driver.find_element(By.XPATH, self.cust_ACB_state_xpath).click()
    #     self.driver.find_element(By.XPATH, self.cust_ACB_state_search_xpath).click()
    #         # print
    #     self.driver.find_element(By.XPATH, self.cust_ACB_state_search_xpath).send_keys("Texas")
    #     state_search_results = self.driver.find_elements(By.XPATH, self.cust_ACB_state_searchbox_xpath)
    #     print(state_search_results)
    #     print(len(state_search_results))
    #     for results in state_search_results:
    #         if "Texas" in results.text:
    #             results.click()
    #             break

    def acb_esavebutton_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_savebutton_click_xpath).click()

    # Delete
    def acb_DElbutton_click(self):
        self.driver.find_element(By.XPATH, self.cust_deleteB_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.cust_e_d_ok_button_xpath).click()
