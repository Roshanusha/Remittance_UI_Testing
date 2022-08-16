import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page


class Customers_payer_page(Base_page):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # All clicks
        self.cust_click_xpath = "//a[normalize-space()='Customers']"

        # Add Customer(PAYER) - ACP
        # self.nfig_click_xpath = "//a[@routerlink='/xchange-config']"
        self.cust_addconfig_click_xpath = "//span[normalize-space()='Add Customer']"
        self.cust_ACP_Title_xpath = "//select[@aria-label='Default select example']"# From Currency
        self.cust_ACP_FN_xpath = "//input[@placeholder='First name']"  # fist name
        self.cust_ACP_MN_xpath = "//input[@placeholder='Middle name']"
        self.cust_ACP_LN_xpath = "//input[@placeholder='Last name']"
        self.cust_ACP_Nationality_xpath = "//p-dropdown[@id='ddNationality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACP_Nationality_search_xpath = "//input[@autocomplete='off']"
        self.cust_ACP_Nationality_searchbox_xpath = "//ul[@role='listbox']"
        self.cust_ACP_DOB_xpath = "//input[@placeholder='DOB']"
        self.cust_ACP_Email_xpath = "//input[@placeholder='Email']"
        self.cust_ACP_Ph_no_xpath = "//input[@placeholder='Phone Number']"
        self.cust_ACP_Passport_xpath = "//input[@placeholder='Passport']"
        self.cust_ACP_SSN_xpath = "//input[@placeholder='SSN']"
        self.cust_ACP_ZIP_xpath = "//input[@placeholder='Zip']"
        self.cust_ACP_city_xpath = "//input[@placeholder='City']"
        self.cust_ACP_Addr1_xpath = "//input[@placeholder='Line 1']"
        self.cust_ACP_Addr2_xpath = "//input[@placeholder='Line 2']"
        self.cust_ACP_state_xpath = "//p-dropdown[@formcontrolname='state']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACP_state_search_xpath = "(//input[@autocomplete='off'])[1]"
        self.cust_ACP_state_searchbox_xpath = "(//ul[@role='listbox'])[1]"
        self.cust_ACP_savebutton_click_xpath = "//span[normalize-space()='Save']"



        # self.XC_rate_xpath = "//input[@id='validationCustomUsername']"
        #self.cust_savebutton_click_xpath = "//button[@type='submit']"
        # (By.XPATH, "//p-multiselect[@defaultlabel='Select Type']//div[@ng-reflect-ng-class='[object Object]']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='pi pi-chevron-down']")
        # self.feetype1_click_xpath = "//select[@aria-label='Default select example']"
        # self.feetype2_click_xpath = "//select[@aria-label='Default select example']"
        # self.feevalue_click_xpath = "//input[@id='validationCustomUsername']"
        # self.addslabrange_click_xpath = "//button[normalize-space()='Add Slab Range']"
        # self.slab_fromvalue_click_xpath = "//input[@id='from']"
        # self.slab_tovalue_click_xpath = "//input[@placeholder='To']"
        # self.asr_savebutton_click_xpath = "//button[normalize-space()='Save']"

        # Customers
        # #Global search bar
        self.cust_gsearchbar_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
        # small search bars
        self.cust_S_id_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/" \
                               "div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[1]/input[1]"
        self.cust_S_FN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/" \
                               "div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[2]/input[1]"
        self.cust_S_MN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                               "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[3]/input[1]"
        self.cust_S_LN_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                               "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[4]/input[1]"
        self.cust_S_Phone_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[5]/input[1]"
        self.cust_S_Email_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                  "div[2]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[2]/th[6]/input[1]"

        # Actions
        # Edit
        self.cust_editB_xpath =  "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/div[2]/" \
                                 "div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[1]"

        #self.cust_ACP_esavebutton_click_xpath = "//span[normalize-space()='Save']"
        #self.setDefault_button_xpath =  "//tbody/tr[1]/td[5]/button[3]/span[1]"

        # Delete
        self.cust_deleteB_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/" \
                                "div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/button[2]/span[1]"
        #e/d ok
        self.cust_e_d_ok_button_xpath = "//ngb-modal-window[@role='dialog']//button[2]"




# Clicks and Actions
    def customers_click(self):
        self.driver.find_element(By.XPATH, self.cust_click_xpath).click()

    def add_customer_click(self):
        self.driver.find_element(By.XPATH, self.cust_addconfig_click_xpath).click()

    def acp_title_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACP_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Title_xpath))
        select.select_by_value("Mr")
        print("selected item - " + select.first_selected_option.text)
        assert "Mr" in select.first_selected_option.text

    def acp_FN(self, firstname):
        self.driver.find_element(By.XPATH, self.cust_ACP_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_FN_xpath).send_keys(firstname)

    def acp_MN(self, middlename):
        self.driver.find_element(By.XPATH, self.cust_ACP_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_MN_xpath).send_keys(middlename)

    def acp_LN(self, lastname):
        self.driver.find_element(By.XPATH, self.cust_ACP_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_LN_xpath).send_keys(lastname)

    def acp_Nationality_click(self):
        # self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_xpath).click()
        # self.driver.find_elements(By.XPATH, self.cust_ACP_Nationality_search_xpath).click()
        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        # assert "American - US" in select.first_selected_option.text

        self.driver.find_element(By.XPATH,  self.cust_ACP_Nationality_xpath).click()
        self.driver.find_element(By.XPATH,  self.cust_ACP_Nationality_search_xpath).click()
        #print
        self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath).send_keys("American")
        nationality_search_results = self.driver.find_elements(By.XPATH,  self.cust_ACP_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "American - US" in results.text:
                results.click()
                break
        #nationality_search_results.send_keys()

        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        #assert self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_xpath).get_attribute("value") == "American - US"

    def acp_DOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.cust_ACP_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_DOB_xpath).send_keys(dob)

    def acp_Email(self, emailid):
        self.driver.find_element(By.XPATH,   self.cust_ACP_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,   self.cust_ACP_Email_xpath).send_keys(emailid)

    def acp_Phone_No(self, phone):
        self.driver.find_element(By.XPATH,  self.cust_ACP_Ph_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,  self.cust_ACP_Ph_no_xpath).send_keys(phone)

    def acp_Passort(self, passport_no):
        self.driver.find_element(By.XPATH, self.cust_ACP_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Passport_xpath).send_keys(passport_no)

    def acp_SSN(self, ssn_no): # social security no
        self.driver.find_element(By.XPATH, self.cust_ACP_SSN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_SSN_xpath).send_keys(ssn_no)

    def acp_ZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.cust_ACP_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_ZIP_xpath).send_keys(zipcode)

    def acp_City(self, city):
        self.driver.find_element(By.XPATH, self.cust_ACP_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_city_xpath).send_keys(city)

    def acp_Addr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr1_xpath).send_keys(Addrline1)

    def acp_Addr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr2_xpath).send_keys(Addrline2)

    def acp_State_click(self):
        self.driver.find_element(By.XPATH,  self.cust_ACP_state_xpath).click()
        self.driver.find_element(By.XPATH,  self.cust_ACP_state_search_xpath).click()
        #print
        self.driver.find_element(By.XPATH, self.cust_ACP_state_search_xpath).send_keys("Texas")
        state_search_results = self.driver.find_elements(By.XPATH, self.cust_ACP_state_searchbox_xpath)
        print(state_search_results)
        print(len(state_search_results))
        for results in state_search_results:
            if "Texas" in results.text:
                results.click()
                break

    def acp_savebutton_click(self):
        self.driver.find_element(By.XPATH,  self.cust_ACP_savebutton_click_xpath).click()

    # small searchbars
    def acp_id_s_searchbars(self, acp_ss_id_bar):
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(acp_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acp_FN_s_searchbars(self, acp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(acp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Robert"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert"
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def v1acp_FN_s_searchbars(self, eacp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(eacp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Robert"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert"
        #self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def v2acp_FN_s_searchbars(self, eacp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(eacp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).get_attribute("value") == "Robert1"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert1"


    def acp_MN_s_searchbars(self, acp_ss_MN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(acp_ss_MN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).get_attribute("value") == "william"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        # assert ele == "william"
        self.driver.find_element(By.XPATH, self.cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acp_LN_s_searchbars(self, acp_ss_LN_bar):
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(acp_ss_LN_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).get_attribute("value") == "stark"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele == "stark"
        self.driver.find_element(By.XPATH, self.cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acp_Email_s_searchbars(self, acp_ss_email_bar):
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(acp_ss_email_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).get_attribute("value") == "rob@gmail.com"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[6]")).text
        assert ele == "rob@gmail.com"
        self.driver.find_element(By.XPATH, self.cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def acp_Phone_s_searchbars(self, acp_ss_ph_bar):
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(acp_ss_ph_bar)
        assert self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).get_attribute("value") == "7774446661"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "7774446661"
        self.driver.find_element(By.XPATH, self.cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    # global search
    # def fc_g_searchbars(self, fc_gs_centrename_bar):       # fc_g-fee config global
    #
    #     self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(fc_gs_centrename_bar)
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    # Edit
    def editbutton_customer_click(self):
        self.driver.find_element(By.XPATH, self.cust_editB_xpath).click()

    def acp_etitle_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACP_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Title_xpath))
        select.select_by_value("Mr")
        print("selected item - " + select.first_selected_option.text)
        assert "Mr" in select.first_selected_option.text

    def acp_eFN(self, firstname):
        self.driver.find_element(By.XPATH, self.cust_ACP_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_FN_xpath).send_keys(firstname)

    def acp_eMN(self, middlename):
        self.driver.find_element(By.XPATH, self.cust_ACP_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_MN_xpath).send_keys(middlename)

    def acp_eLN(self, lastname):
        self.driver.find_element(By.XPATH, self.cust_ACP_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_LN_xpath).send_keys(lastname)

    def acp_eNationality_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath).send_keys("American")
        nationality_search_results = self.driver.find_elements(By.XPATH, self.cust_ACP_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "American - US" in results.text:
                results.click()
                break

    def acp_eDOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.cust_ACP_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_DOB_xpath).send_keys(dob)

    def acp_eEmail(self, emailid):
        self.driver.find_element(By.XPATH, self.cust_ACP_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Email_xpath).send_keys(emailid)

    def acp_ePhone_No(self, phone):
        self.driver.find_element(By.XPATH, self.cust_ACP_Ph_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Ph_no_xpath).send_keys(phone)

    def acp_ePassort(self, passport_no):
        self.driver.find_element(By.XPATH, self.cust_ACP_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Passport_xpath).send_keys(passport_no)

    def acp_eSSN(self, ssn_no): # social security no
        self.driver.find_element(By.XPATH, self.cust_ACP_SSN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_SSN_xpath).send_keys(ssn_no)

    def acp_eZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.cust_ACP_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_ZIP_xpath).send_keys(zipcode)

    def acp_eCity(self, city):
        self.driver.find_element(By.XPATH, self.cust_ACP_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_city_xpath).send_keys(city)

    def acp_eAddr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr1_xpath).send_keys(Addrline1)

    def acp_eAddr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cust_ACP_Addr2_xpath).send_keys(Addrline2)

    def acp_eState_click(self):
        self.driver.find_element(By.XPATH, self.cust_ACP_state_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACP_state_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACP_state_search_xpath).send_keys("Texas")
        state_search_results = self.driver.find_elements(By.XPATH, self.cust_ACP_state_searchbox_xpath)
        print(state_search_results)
        print(len(state_search_results))
        for results in state_search_results:
            if "Texas" in results.text:
                results.click()
                break


    def acp_esavebutton_click(self):
        self.driver.find_element(By.XPATH,  self.cust_ACP_savebutton_click_xpath).click()

    # Delete
    def acp_DElbutton_click(self):
        self.driver.find_element(By.XPATH, self.cust_deleteB_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.cust_e_d_ok_button_xpath).click()

    # def XC_FC_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_FC_click_xpath).click()
    #     select = Select(self.driver.find_element(By.XPATH, self.XC_FC_click_xpath))
    #     select.select_by_visible_text("USD")
    #     print("selected item - " + select.first_selected_option.text)
    #     assert "USD" in select.first_selected_option.text
    #
    # def XC_TC_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_TC_click_xpath).click()
    #     select = Select(self.driver.find_element(By.XPATH, self.XC_TC_click_xpath))
    #     select.select_by_value("MLC")
    #     print("selected item - " + select.first_selected_option.text)
    #     assert "MLC" in select.first_selected_option.text
    #
    # # Add Xchange_Rate_config
    # def XC_config_Rate(self, XCconfig_Rate):
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(XCconfig_Rate)
    #
    # def XC_config_click(self):
    #     self.driver.find_element(By.XPATH, self.config_click_xpath).click()
    #     self.driver.find_element(By.XPATH, self.Xchange_config_click_xpath ).click()
    #
    # #driver.find_element(By.XPATH, "//input[@type='number']")
    # def XC_addconfig_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_rate_addconfig_click_xpath).click()
    #
    # def XC_addconfig_save_click(self):
    #     self.driver.find_element(By.XPATH,  self.addXCconfig_savebutton_click_xpath).click()
    #
    # # small searchbars
    # def XC_id_s_searchbars(self, XC_ss_id_bar):
    #     self.driver.find_element(By.XPATH, self.XC_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_S_id_xpath).send_keys(XC_ss_id_bar)
    #     assert self.driver.find_element(By.XPATH, self.XC_S_id_xpath).get_attribute("value") == "62"
    #     time.sleep(3)
    #     ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
    #     assert ele == "00062"
    #     self.driver.find_element(By.XPATH, self.XC_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # def XC_FCC_ssbars(self, XC_ss_Fcc_bar):
    #     self.driver.find_element(By.XPATH, self.XC_S_FCC_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_S_FCC_xpath).send_keys(XC_ss_Fcc_bar)
    #     assert self.driver.find_element(By.XPATH, self.XC_S_FCC_xpath).get_attribute("value") == "USD"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[2]")).text
    #     assert ele1 == "USD"
    #     self.driver.find_element(By.XPATH, self.XC_S_FCC_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # def XC_TCC_ssbars(self, XC_ss_Tcc_bar):
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(XC_ss_Tcc_bar)
    #     assert self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).get_attribute("value") == "MLC"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[3]")).text
    #     assert ele1 == "MLC"
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # def XC_Rate_ssbars(self, XC_ss_rate_bar):
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(XC_ss_rate_bar)
    #     assert self.driver.find_element(By.XPATH, self.XC_rate_xpath).get_attribute("value") == "20"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
    #     assert ele1 == "20"
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # # for validation
    # def Valid_XC_s_rate_sbars(self, vXC_ss_rate_bar):
    #     self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).send_keys(vXC_ss_rate_bar)
    #     assert self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).get_attribute("value") == "20"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[4]")).text
    #     assert ele1 == "20"
    #     #self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # def eValid_XC_s_rate_sbars(self, evXC_ss_rate_bar):
    #     self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_S_Rate_xpath).send_keys(evXC_ss_rate_bar)
    #     assert self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).get_attribute("value") == "30"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[4]")).text
    #     assert ele1 == "30"
    #     time.sleep(3)
    #     #self.driver.find_element(By.XPATH,  self.XC_S_Rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # def Valid_XC_TCC_ssbars(self, vXC_ss_Tcc_bar):
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(vXC_ss_Tcc_bar)
    #     assert self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).get_attribute("value") == "MLC"
    #     time.sleep(5)
    #     ele1 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
    #     assert ele1 == "MLC"
    #     self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #
    # # Edit/ Delete
    # def XC_eFC_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_FC_click_xpath).click()
    #     select = Select(self.driver.find_element(By.XPATH, self.XC_FC_click_xpath))
    #     select.select_by_visible_text("USD")
    #     print("selected item - " + select.first_selected_option.text)
    #     assert "USD" in select.first_selected_option.text
    #
    # def XC_eTC_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_TC_click_xpath).click()
    #     select = Select(self.driver.find_element(By.XPATH, self.XC_TC_click_xpath))
    #     select.select_by_value("CUP")
    #     print("selected item - " + select.first_selected_option.text)
    #     assert "CUP" in select.first_selected_option.text
    #
    # def XC_config_eRate(self, XCconfig_eRate):
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
    #     self.driver.find_element(By.XPATH, self.XC_rate_xpath).send_keys(XCconfig_eRate)
    #
    # def XC_Edit_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_editB_xpath).click()
    #     #self.driver.find_element(By.XPATH, self.XC_e_d_ok_button_xpath).click()
    #
    # def XC_Delete_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_deleteB_xpath).click()
    #     #self.driver.find_element(By.XPATH, self.XC_e_d_ok_button_xpath).click()
    #
    # def XC_E_D_ok_click(self):
    #     self.driver.find_element(By.XPATH, self.XC_e_d_ok_button_xpath).click()
    #
    # def XC_SetDefault_click(self):
    #     self.driver.find_element(By.XPATH, self.setDefault_button_xpath).click()
    #
    # def Valid_XC_SetDefault(self):
    #     ele1 = self.wait_for((By.XPATH, self.setDefault_button_xpath)).text
    #     assert ele1 == "Default"
    #     #self.driver.find_element(By.XPATH, self.XC_S_TCC_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)