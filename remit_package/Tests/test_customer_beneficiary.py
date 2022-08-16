import self
from selenium.webdriver.common.keys import Keys

from remit_package.Pages.login_page import LoginPage
from remit_package.Pages.Customers_beneficiary import Customers_Beneficiary_page
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

    def test_Cust_beneficiary_valid(self):
        driver = self.driver
        cust_ACB = Customers_Beneficiary_page(self.driver)

    # goto/click customers
        cust_ACB.customers_click()
        time.sleep(3)

        cust_ACB.add_customer_click()
        time.sleep(3)

        cust_ACB.benef_radiobutton_click()
        time.sleep(3)

        cust_ACB.acb_title_click()
        time.sleep(3)

        cust_ACB.acb_FN("Alicia")
        time.sleep(3)

        cust_ACB.acb_MN("Tom")
        time.sleep(3)

        cust_ACB.acb_LN("Gonzalez")
        time.sleep(3)

        cust_ACB.acb_Nationality_click()
        time.sleep(3)

        cust_ACB.acb_DOB_click("11-07-2000")
        time.sleep(3)

        cust_ACB.acb_Email("ally@gmail.com")
        time.sleep(3)

        cust_ACB.acb_Phone_No("7775559991")
        time.sleep(3)

        cust_ACB.acb_Passort("Gb786hf")
        time.sleep(3)

        cust_ACB.acb_Cuban_no("458796")
        time.sleep(3)

        cust_ACB.acb_ZIP("675002")
        time.sleep(3)

        cust_ACB.acb_City("cuba")
        time.sleep(3)

        cust_ACB.acb_Muncipality()
        time.sleep(3)

        cust_ACB.acb_Addr1("cahala str")
        time.sleep(3)

        cust_ACB.acb_Addr2("vintage wines road")
        time.sleep(3)

        # cust_ACB.acb_State_click()
        # time.sleep(3)

        cust_ACB.acb_savebutton_click()
        time.sleep(5)

        # Small search bars
        # cust_ACP.acp_id_s_searchbars("")
        # time.sleep(5)

        cust_ACB.acb_FN_s_searchbars("Alicia")
        time.sleep(5)

        cust_ACB.acb_MN_s_searchbars("Tom")
        time.sleep(5)

        cust_ACB.acb_LN_s_searchbars("Gonzalez")
        time.sleep(5)

        cust_ACB.acb_Email_s_searchbars("ally@gmail.com")
        time.sleep(5)

        cust_ACB.acb_Phone_s_searchbars("7775559991")
        time.sleep(5)

        # Edit
        cust_ACB.v1acb_FN_s_searchbars("Alicia")
        time.sleep(5)

        cust_ACB.editbutton_customer_click()
        time.sleep(3)

        cust_ACB.acb_etitle_click()
        time.sleep(3)

        cust_ACB.acb_eFN("Alicia1")
        time.sleep(3)

        cust_ACB.acb_eMN("Tom1")
        time.sleep(3)

        cust_ACB.acb_eLN("Gonzalez1")
        time.sleep(3)

        cust_ACB.acb_eNationality_click()
        time.sleep(3)

        cust_ACB.acb_eDOB_click("08-07-2000")
        time.sleep(3)

        cust_ACB.acb_eEmail("allie@gmail.com")
        time.sleep(3)

        cust_ACB.acb_ePhone_No("7774446665")
        time.sleep(3)

        cust_ACB.acb_ePassort("Gb786kl")
        time.sleep(3)

        cust_ACB.acb_eCuban_no("656633")
        time.sleep(3)

        cust_ACB.acb_eZIP("673104")
        time.sleep(3)

        cust_ACB.acb_eCity("cuba1")
        time.sleep(3)

        cust_ACB.acb_eMuncipality()
        time.sleep(3)

        cust_ACB.acb_eAddr1("villa mount park st1")
        time.sleep(3)

        cust_ACB.acb_eAddr2("kings garden road1")
        time.sleep(3)

        # cust_ACB.acb_eState_click()
        # time.sleep(3)

        cust_ACB.acb_esavebutton_click()
        time.sleep(5)

        #validate
        cust_ACB.v2acb_FN_s_searchbars("Alicia1")
        time.sleep(5)

        #Delete
        cust_ACB.acb_DElbutton_click()
        time.sleep(2)
