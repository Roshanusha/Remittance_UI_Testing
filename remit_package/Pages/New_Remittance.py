import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page


class New_remittace_page(Base_page):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    # all clicks
        self.remittance_click_xpath = "//a[@id='navbarDropdownRemit']"
        self.nr_click_xpath = "//a[@routerlink='remit']"        # New Remittance
        self.nr_payer_AL_click_xpath = "//body//app-root//div//div//div//div//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//button[1]"
        self.nr_benef_AL_click_xpath = "//body[1]/app-root[1]/div[1]/app-remitance-page[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"

    # Add Customer(PAYER) - ACP
        self.nr_addcustP_click_xpath = "//body/ngb-modal-window[@role='dialog']/div[@role='document']/div/app-customer-page/div/div/div/button[@type='button']/span[1]"
        self.nr_addcustB_click_xpath = "//span[2]"
        self.nr_cust_ACP_Title_xpath = "//select[@aria-label='Default select example']"  # From Currency
        self.nr_cust_ACP_FN_xpath = "//input[@placeholder='First name']"  # fist name
        self.nr_cust_ACP_MN_xpath = "//input[@placeholder='Middle name']"
        self.nr_cust_ACP_LN_xpath = "//input[@placeholder='Last name']"
        self.nr_cust_ACP_Nationality_xpath = "//p-dropdown[@id='ddNationality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.nr_cust_ACP_Nationality_search_xpath = "//input[@autocomplete='off']"
        self.nr_cust_ACP_Nationality_searchbox_xpath = "//ul[@role='listbox']"
        self.nr_cust_ACP_DOB_xpath = "//input[@placeholder='DOB']"
        self.nr_cust_ACP_Email_xpath = "//input[@placeholder='Email']"
        self.nr_cust_ACP_Ph_no_xpath = "//input[@placeholder='Phone Number']"
        self.nr_cust_ACP_Passport_xpath = "//input[@placeholder='Passport']"
        self.nr_cust_ACP_SSN_xpath = "//input[@placeholder='SSN']"
        self.nr_cust_ACP_ZIP_xpath = "//input[@placeholder='Zip']"
        self.nr_cust_ACP_city_xpath = "//input[@placeholder='City']"
        self.nr_cust_ACP_Addr1_xpath = "//input[@placeholder='Line 1']"
        self.nr_cust_ACP_Addr2_xpath = "//input[@placeholder='Line 2']"
        self.nr_cust_ACP_state_xpath = "//p-dropdown[@formcontrolname='state']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.nr_cust_ACP_state_search_xpath = "(//input[@autocomplete='off'])[1]"
        self.nr_cust_ACP_state_searchbox_xpath = "(//ul[@role='listbox'])[1]"
        self.nr_cust_ACP_savebutton_click_xpath = "//span[normalize-space()='Save']"

    # Add Customer(BENEFICIARY) - ACB
        self.nr_addcustB_click_xpath = "//body/ngb-modal-window[@role='dialog']/div[@role='document']/div/app-customer-page/div/div/div/button[@type='button']/span[1]"
        self.nr_cust_ACB_Title_xpath = "//select[@aria-label='Default select example']"  # From Currency
        self.nr_cust_ACB_FN_xpath = "//input[@placeholder='First name']"  # fist name
        self.nr_cust_ACB_MN_xpath = "//input[@placeholder='Middle name']"
        self.nr_cust_ACB_LN_xpath = "//input[@placeholder='Last name']"
        self.nr_cust_ACB_Nationality_xpath = "//p-dropdown[@id='ddNationality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.nr_cust_ACB_Nationality_search_xpath = "//input[@autocomplete='off']"
        self.nr_cust_ACB_Nationality_searchbox_xpath = "//ul[@role='listbox']"
        self.nr_cust_ACB_DOB_xpath = "//input[@placeholder='DOB']"
        self.nr_cust_ACB_Email_xpath = "//input[@placeholder='Email']"
        self.nr_cust_ACB_Ph_no_xpath = "//input[@placeholder='Phone Number']"
        self.nr_cust_ACB_Passport_xpath = "//input[@placeholder='Passport']"
        self.nr_cust_ACB_ecubanid_xpath = "//input[@placeholder='Cuban ID']"
        self.nr_cust_ACB_ZIP_xpath = "//input[@placeholder='Zip']"
        self.nr_cust_ACB_city_xpath = "//input[@placeholder='City']"
        self.cust_ACB_muncipality_xpath = "//p-dropdown[@formcontrolname='municipality']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.cust_ACB_muncipality_search_xpath = "//input[@autocomplete='off'][1]"
        self.cust_ACB_muncipality_searchBOX_xpath = "(//ul[@role='listbox'])[1]"
        self.nr_cust_ACB_Addr1_xpath = "//input[@placeholder='Line 1']"
        self.nr_cust_ACB_Addr2_xpath = "//input[@placeholder='Line 2']"
        self.nr_cust_ACB_state_xpath = "//p-dropdown[@formcontrolname='state']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='[object Object]']"
        self.nr_cust_ACB_state_search_xpath = "(//input[@autocomplete='off'])[1]"
        self.nr_cust_ACB_state_searchbox_xpath = "(//ul[@role='listbox'])[1]"
        self.nr_cust_ACB_savebutton_click_xpath = "//span[normalize-space()='Save']"

    # Add/link Payer Customer
    # #Global search bar
        self.nr_cust_gsearchbar_xpath = "//body[1]/app-root[1]/div[1]/app-customer-page[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
        # small search bars
        self.nr_cust_S_id_xpath = "//th[1]//input[1]"
        self.nr_cust_S_FN_xpath = "//th[2]//input[1]"
        self.nr_cust_S_MN_xpath = "//th[3]//input[1]"
        self.nr_cust_S_LN_xpath = "//th[4]//input[1]"
        self.nr_cust_S_Phone_xpath = "//th[5]//input[1]"
        self.nr_cust_S_Email_xpath = "//th[6]//input[1]"
        #link button
        self.nr_cust_link_button_xpath = "//tbody/tr[1]/td[7]/button[1]"

        #remittance part
        self.nr_Tr_deposit_xpath = "//select[@title='Select account']"
        self.nr_send_currency_xpath = "//select[@title='Send Currency']"
        self.nr_receive_currency_xpath = "//select[@title='Receive Currency']"
        self.nr_amt_paid_xpath = "//input[@title='Amount paid to the Beneficiary']"
        #send funds button
        self.nr_send_funds_xpath = "//app-remitance-details[@ng-reflect-beneficiary='[object Object]']//div//div//div//div/" \
                                   "/form//div//div//button[@type='button']"

        # Clicks and Actions
    def remittance_nr_click(self):
        self.driver.find_element(By.XPATH, self.remittance_click_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.nr_click_xpath).click()

    def nr_al_customerP_click(self):
        self.driver.find_element(By.XPATH, self.nr_payer_AL_click_xpath).click()

    def nr_add_customerP_click(self):
        self.driver.find_element(By.XPATH,  self.nr_addcustP_click_xpath).click()

    def nr_acp_title_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.nr_cust_ACP_Title_xpath))
        select.select_by_value("Mrs")
        print("selected item - " + select.first_selected_option.text)
        assert "Mrs" in select.first_selected_option.text

    def nr_acp_FN(self, firstname):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_FN_xpath).send_keys(firstname)

    def nr_acp_MN(self, middlename):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_MN_xpath).send_keys(middlename)

    def nr_acp_LN(self, lastname):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_LN_xpath).send_keys(lastname)

    def nr_acp_Nationality_click(self):
        # self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_xpath).click()
        # self.driver.find_elements(By.XPATH, self.cust_ACP_Nationality_search_xpath).click()
        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        # assert "American - US" in select.first_selected_option.text

        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Nationality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Nationality_search_xpath).send_keys("American")
        nationality_search_results = self.driver.find_elements(By.XPATH, self.nr_cust_ACP_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "American - US" in results.text:
                results.click()
                break
        # nationality_search_results.send_keys()

        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        # assert self.driver.find_element(By.XPATH, self.cust_ACP_Nationality_xpath).get_attribute("value") == "American - US"

    def nr_acp_DOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_DOB_xpath).send_keys(dob)

    def nr_acp_Email(self, emailid):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Email_xpath).send_keys(emailid)

    def nr_acp_Phone_No(self, phone):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Ph_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Ph_no_xpath).send_keys(phone)

    def nr_acp_Passort(self, passport_no):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Passport_xpath).send_keys(passport_no)

    def nr_acp_SSN(self, ssn_no):  # social security no
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_SSN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_SSN_xpath).send_keys(ssn_no)

    def nr_acp_ZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_ZIP_xpath).send_keys(zipcode)

    def nr_acp_City(self, city):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_city_xpath).send_keys(city)

    def nr_acp_Addr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Addr1_xpath).send_keys(Addrline1)

    def nr_acp_Addr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_Addr2_xpath).send_keys(Addrline2)

    def nr_acp_State_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_state_xpath).click()
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_state_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_state_search_xpath).send_keys("California")
        state_search_results = self.driver.find_elements(By.XPATH, self.nr_cust_ACP_state_searchbox_xpath)
        print(state_search_results)
        print(len(state_search_results))
        for results in state_search_results:
            if "California" in results.text:
                results.click()
                break

    def nr_acp_savebutton_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_ACP_savebutton_click_xpath).click()

    # small searchbars
    def nr_acp_id_s_searchbars(self, acp_ss_id_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(acp_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acp_FN_s_searchbars(self, acp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(acp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "Robert"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert"
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_v1acp_FN_s_searchbars(self, eacp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(eacp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "lizzy"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "lizzy"
        # self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_v2acp_FN_s_searchbars(self, eacp_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(eacp_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "Robert1"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert1"

    def nr_acp_MN_s_searchbars(self, acp_ss_MN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(acp_ss_MN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).get_attribute("value") == "william"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        # assert ele == "william"
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acp_LN_s_searchbars(self, acp_ss_LN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(acp_ss_LN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).get_attribute("value") == "stark"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele == "stark"
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acp_Email_s_searchbars(self, acp_ss_email_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(acp_ss_email_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).get_attribute("value") == "rob@gmail.com"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[6]")).text
        assert ele == "rob@gmail.com"
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acp_Phone_s_searchbars(self, acp_ss_ph_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(acp_ss_ph_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).get_attribute("value") == "7774446661"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "7774446661"
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acp_link_button_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_link_button_xpath).click()

    # BENEFICIARY part
    # def remittance_nr_click(self):
    #     self.driver.find_element(By.XPATH, self.remittance_click_xpath).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, self.nr_click_xpath).click()

    def nr_al_customerB_click(self):
        self.driver.find_element(By.XPATH, self.nr_benef_AL_click_xpath).click()

    def nr_add_customerB_click(self):
        self.driver.find_element(By.XPATH, self.nr_addcustB_click_xpath).click()

    def nr_acb_title_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Title_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.nr_cust_ACB_Title_xpath))
        select.select_by_value("Mr")
        print("selected item - " + select.first_selected_option.text)
        assert "Mr" in select.first_selected_option.text

    def nr_acb_FN(self, firstname):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_FN_xpath).send_keys(firstname)

    def nr_acb_MN(self, middlename):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_MN_xpath).send_keys(middlename)

    def nr_acb_LN(self, lastname):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_LN_xpath).send_keys(lastname)

    def nr_acb_Nationality_click(self):
        # self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_xpath).click()
        # self.driver.find_elements(By.XPATH, self.cust_ACB_Nationality_search_xpath).click()
        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        # assert "American - US" in select.first_selected_option.text

        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Nationality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Nationality_search_xpath).send_keys("Cuban")
        nationality_search_results = self.driver.find_elements(By.XPATH, self.nr_cust_ACB_Nationality_searchbox_xpath)
        print(nationality_search_results)
        print(len(nationality_search_results))
        for results in nationality_search_results:
            if "Cuban" in results.text:
                results.click()
                break
        # nationality_search_results.send_keys()

        # select = Select(self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_search_xpath))
        # select.select_by_value("American - US")
        # print("selected item - " + select.first_selected_option.text)
        # assert self.driver.find_element(By.XPATH, self.cust_ACB_Nationality_xpath).get_attribute("value") == "American - US"

    def nr_acb_DOB_click(self, dob):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_DOB_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_DOB_xpath).send_keys(dob)

    def nr_acb_Email(self, emailid):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Email_xpath).send_keys(emailid)

    def nr_acb_Phone_No(self, phone):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Ph_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Ph_no_xpath).send_keys(phone)

    def nr_acb_Passort(self, passport_no):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Passport_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Passport_xpath).send_keys(passport_no)

    def nr_acb_ecuban(self, cuban_id_no):  # social security no
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_ecubanid_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_ecubanid_xpath).send_keys(cuban_id_no)

    def nr_acb_ZIP(self, zipcode):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_ZIP_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_ZIP_xpath).send_keys(zipcode)

    def nr_acb_City(self, city):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_city_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_city_xpath).send_keys(city)

    def nr_acb_Muncipality(self):
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_xpath).click()
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).click()
        # print
        self.driver.find_element(By.XPATH, self.cust_ACB_muncipality_search_xpath).send_keys("BAUTA")
        muncipality_search_results = self.driver.find_elements(By.XPATH,  self.cust_ACB_muncipality_searchBOX_xpath)
        print(muncipality_search_results)
        print(len(muncipality_search_results))
        for results in muncipality_search_results:
            if "BAUTA" in results.text:
                results.click()
                break

    def nr_acb_Addr1(self, Addrline1):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Addr1_xpath).send_keys(Addrline1)

    def nr_acb_Addr2(self, Addrline2):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_Addr2_xpath).send_keys(Addrline2)

    # def nr_acb_State_click(self):
    #     self.driver.find_element(By.XPATH, self.nr_cust_ACB_state_xpath).click()
    #     self.driver.find_element(By.XPATH, self.nr_cust_ACB_state_search_xpath).click()
    #     # print
    #     self.driver.find_element(By.XPATH, self.nr_cust_ACB_state_search_xpath).send_keys("BAUTA")
    #     state_search_results = self.driver.find_elements(By.XPATH, self.nr_cust_ACB_state_searchbox_xpath)
    #     print(state_search_results)
    #     print(len(state_search_results))
    #     for results in state_search_results:
    #         if "BAUTA" in results.text:
    #             results.click()
    #             break

    def nr_acb_savebutton_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_ACB_savebutton_click_xpath).click()

    # small searchbars
    def nr_acb_id_s_searchbars(self, ACB_ss_id_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(ACB_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.nr_cust_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acb_FN_s_searchbars(self, ACB_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(ACB_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == ""
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert"
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_v1ACB_FN_s_searchbars(self, eACB_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(eACB_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "Dawn"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Dawn"
        # self.driver.find_element(By.XPATH, self.cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_v2ACB_FN_s_searchbars(self, eACB_ss_FN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).send_keys(eACB_ss_FN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_FN_xpath).get_attribute("value") == "Robert1"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele == "Robert1"

    def nr_acb_MN_s_searchbars(self, ACB_ss_MN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(ACB_ss_MN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).get_attribute("value") == "raul"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        # assert ele == "william"
        self.driver.find_element(By.XPATH, self.nr_cust_S_MN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acb_LN_s_searchbars(self, ACB_ss_LN_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(ACB_ss_LN_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).get_attribute("value") == "stark"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele == "stark"
        self.driver.find_element(By.XPATH, self.nr_cust_S_LN_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acb_Email_s_searchbars(self, ACB_ss_email_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(ACB_ss_email_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).get_attribute("value") == "dawn@gmail.com"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[6]")).text
        assert ele == "dawn@gmail.com"
        self.driver.find_element(By.XPATH, self.nr_cust_S_Email_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acb_Phone_s_searchbars(self, ACB_ss_ph_bar):
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(ACB_ss_ph_bar)
        assert self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).get_attribute("value") == "8889994445"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "8889994445"
        self.driver.find_element(By.XPATH, self.nr_cust_S_Phone_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def nr_acb_link_button_click(self):
        self.driver.find_element(By.XPATH, self.nr_cust_link_button_xpath).click()

    def nr_Tr_Deposit_click(self):
        self.driver.find_element(By.XPATH,  self.nr_Tr_deposit_xpath).click()
        select = Select(self.driver.find_element(By.XPATH,  self.nr_Tr_deposit_xpath))
        select.select_by_visible_text("New AIS Card")
        print("selected item - " + select.first_selected_option.text)
        assert "New AIS Card" in select.first_selected_option.text

    def nr_send_currency_click(self):
        self.driver.find_element(By.XPATH,  self.nr_send_currency_xpath).click()
        select = Select(self.driver.find_element(By.XPATH,  self.nr_send_currency_xpath))
        select.select_by_value("USD")
        print("selected item - " + select.first_selected_option.text)
        assert "USD" in select.first_selected_option.text

    def nr_Receive_currency_click(self):
        self.driver.find_element(By.XPATH,  self.nr_receive_currency_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.nr_receive_currency_xpath))
        select.select_by_value("MLC")
        print("selected item - " + select.first_selected_option.text)
        assert "MLC" in select.first_selected_option.text

    def nr_amt_paid(self,amtpaid):
        self.driver.find_element(By.XPATH, self.nr_amt_paid_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.nr_amt_paid_xpath).send_keys(amtpaid)

    def nr_sendfunds_button_click(self):
        self.driver.find_element(By.XPATH, self.nr_send_funds_xpath).click()