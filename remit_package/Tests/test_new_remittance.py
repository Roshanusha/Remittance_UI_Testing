import time

from remit_package.Pages.New_Remittance import New_remittace_page
from remit_package.Pages.login_page import LoginPage
from remit_package.Utilities.BaseClass import BaseClass


class Testmain(BaseClass):

    def test_login_valid(self):
        driver = self.driver
        # wait = WebDriverWait(self.driver, 10)
        login = LoginPage(self.driver)  # class name
        login.enter_username("demo@gmail.com")
        login.enter_password("Password@1234")
        login.click_login()
        driver.implicitly_wait(10)

    def test_nr_PB_valid(self):
        driver = self.driver
        New_remit = New_remittace_page(self.driver)

    # goto/click new remittances
        New_remit.remittance_nr_click()
        time.sleep(2)

        New_remit.nr_al_customerP_click()
        time.sleep(2)

        New_remit.nr_add_customerP_click()
        time.sleep(2)

        New_remit.nr_acp_title_click()
        time.sleep(2)

        New_remit.nr_acp_FN("lizzy")
        time.sleep(2)

        New_remit.nr_acp_MN("von")
        time.sleep(2)

        New_remit.nr_acp_LN("briton")
        time.sleep(2)

        New_remit.nr_acp_Nationality_click()
        time.sleep(2)

        New_remit.nr_acp_DOB_click("04-05-1999")
        time.sleep(2)

        New_remit.nr_acp_Email("lissy@gmail.com")
        time.sleep(2)

        New_remit.nr_acp_Phone_No("8889994445")
        time.sleep(2)

        New_remit.nr_acp_Passort("AME663fe")
        time.sleep(2)

        New_remit.nr_acp_SSN("676549")
        time.sleep(2)

        New_remit.nr_acp_ZIP("252526")
        time.sleep(2)

        New_remit.nr_acp_City("Los Angeles")
        time.sleep(2)

        New_remit.nr_acp_Addr1("hollywood st")
        time.sleep(2)

        New_remit.nr_acp_Addr2("herald lawn field")
        time.sleep(2)

        New_remit.nr_acp_State_click()
        time.sleep(2)

        New_remit.nr_acp_savebutton_click()
        time.sleep(5)

        New_remit.nr_v1acp_FN_s_searchbars("lizzy")
        time.sleep(5)

        New_remit.nr_acp_link_button_click()
        time.sleep(5)

        #beneficary part

        New_remit.nr_al_customerB_click()
        time.sleep(2)

        New_remit.nr_add_customerB_click()
        time.sleep(2)

        New_remit.nr_acb_title_click()
        time.sleep(2)

        New_remit.nr_acb_FN("Dawn")
        time.sleep(2)

        New_remit.nr_acb_MN("raul")
        time.sleep(2)

        New_remit.nr_acb_LN("carlos")
        time.sleep(2)

        New_remit.nr_acb_Nationality_click()
        time.sleep(2)

        New_remit.nr_acb_DOB_click("17-05-1998")
        time.sleep(2)

        New_remit.nr_acb_Email("dawn@gmail.com")
        time.sleep(2)

        New_remit.nr_acb_Phone_No("8889994445")
        time.sleep(2)

        New_remit.nr_acb_Passort("CU453ksd")
        time.sleep(2)

        New_remit.nr_acb_ecuban("682463")
        time.sleep(2)

        New_remit.nr_acb_ZIP("232363")
        time.sleep(2)

        New_remit.nr_acb_City("calico")
        time.sleep(2)

        New_remit.nr_acb_Muncipality()
        time.sleep(2)

        New_remit.nr_acb_Addr1("slicia st")
        time.sleep(2)

        New_remit.nr_acb_Addr2("first avenue road")
        time.sleep(2)

        # New_remit.nr_acb_State_click()
        # time.sleep(2)

        New_remit.nr_acb_savebutton_click()
        time.sleep(5)

        New_remit.nr_v1ACB_FN_s_searchbars("Dawn")
        time.sleep(2)

        New_remit.nr_acb_link_button_click()
        time.sleep(2)

        New_remit.nr_Tr_Deposit_click()
        time.sleep(2)

        New_remit.nr_send_currency_click()
        time.sleep(2)

        New_remit.nr_Receive_currency_click()
        time.sleep(2)

        New_remit.nr_amt_paid("10")
        time.sleep(2)