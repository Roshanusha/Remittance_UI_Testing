import self
from selenium.webdriver.common.keys import Keys

from remit_package.Pages.login_page import LoginPage
from remit_package.Pages.Customers_payer import Customers_payer_page
from remit_package.Utilities.BaseClass import BaseClass
from remit_package.Pages.base_page import Base_page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


class Testmain(BaseClass):

    def test_login_valid(self):

        driver = self.driver
        # wait = WebDriverWait(self.driver, 10)
        login = LoginPage(self.driver)  # class name
        login.enter_username("demo@gmail.com")
        login.enter_password("Password@1234")
        login.click_login()
        driver.implicitly_wait(10)

    def test_Cust_payer_valid(self):
        driver = self.driver
        cust_ACP = Customers_payer_page(self.driver)

    # goto/click customers
        time.sleep(3)

        cust_ACP.add_customer_click()
        time.sleep(3)

        cust_ACP.acp_title_click()
        time.sleep(3)

        cust_ACP.acp_FN("Robert")
        time.sleep(3)

        cust_ACP.acp_MN("william")
        time.sleep(3)

        cust_ACP.acp_LN("stark")
        time.sleep(3)

        cust_ACP.acp_Nationality_click()
        time.sleep(3)

        cust_ACP.acp_DOB_click("24-04-1995")
        time.sleep(3)

        cust_ACP.acp_Email("rob@gmail.com")
        time.sleep(3)

        cust_ACP.acp_Phone_No("7774446661")
        time.sleep(3)

        cust_ACP.acp_Passort("AME456je")
        time.sleep(3)

        cust_ACP.acp_SSN("654654")
        time.sleep(3)

        cust_ACP.acp_ZIP("679102")
        time.sleep(3)

        cust_ACP.acp_City("Houston")
        time.sleep(3)

        cust_ACP.acp_Addr1("villa mount park st")
        time.sleep(3)

        cust_ACP.acp_Addr2("kings garden road")
        time.sleep(3)

        cust_ACP.acp_State_click()
        time.sleep(3)

        cust_ACP.acp_savebutton_click()
        time.sleep(5)

        # Small search bars
        # cust_ACP.acp_id_s_searchbars("")
        # time.sleep(5)

        cust_ACP.acp_FN_s_searchbars("Robert")
        time.sleep(5)

        cust_ACP.acp_MN_s_searchbars("william")
        time.sleep(5)

        cust_ACP.acp_LN_s_searchbars("stark")
        time.sleep(5)

        cust_ACP.acp_Email_s_searchbars("rob@gmail.com")
        time.sleep(5)

        cust_ACP.acp_Phone_s_searchbars("7774446661")
        time.sleep(5)

        # Edit
        cust_ACP.v1acp_FN_s_searchbars("Robert")
        time.sleep(5)

        cust_ACP.editbutton_customer_click()
        time.sleep(3)

        cust_ACP.acp_etitle_click()
        time.sleep(3)

        cust_ACP.acp_eFN("Robert1")
        time.sleep(3)

        cust_ACP.acp_eMN("william1")
        time.sleep(3)

        cust_ACP.acp_eLN("stark1")
        time.sleep(3)

        cust_ACP.acp_eNationality_click()
        time.sleep(3)

        cust_ACP.acp_eDOB_click("20-04-1995")
        time.sleep(3)

        cust_ACP.acp_eEmail("robby@gmail.com")
        time.sleep(3)

        cust_ACP.acp_ePhone_No("7774446665")
        time.sleep(3)

        cust_ACP.acp_ePassort("AME456je")
        time.sleep(3)

        cust_ACP.acp_eSSN("656633")
        time.sleep(3)

        cust_ACP.acp_eZIP("673104")
        time.sleep(3)

        cust_ACP.acp_eCity("Houston1")
        time.sleep(3)

        cust_ACP.acp_eAddr1("villa mount park st1")
        time.sleep(3)

        cust_ACP.acp_eAddr2("kings garden road1")
        time.sleep(3)

        cust_ACP.acp_eState_click()
        time.sleep(3)

        cust_ACP.acp_esavebutton_click()
        time.sleep(5)

        #validate
        cust_ACP.v2acp_FN_s_searchbars("Robert1")
        time.sleep(5)

        #Delete
        cust_ACP.acp_DElbutton_click()
        time.sleep(2)
