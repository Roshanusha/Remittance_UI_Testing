import self
from selenium.webdriver.common.keys import Keys

from remit_package.Pages.login_page import LoginPage
from remit_package.Pages.Xchange_Configurations import Xchange_config_page
from remit_package.Utilities.BaseClass import BaseClass
from remit_package.Pages.base_page import Base_page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


class Testmain(BaseClass):

    # wait = WebDriverWait(self.driver, 10)

    def test_login_valid(self):

        driver = self.driver
        # wait = WebDriverWait(self.driver, 10)
        login = LoginPage(self.driver)  # class name
        login.enter_username("demo@gmail.com")
        login.enter_password("Password@1234")
        login.click_login()
        driver.implicitly_wait(10)

    def test_XC_configuration_valid(self):

        driver = self.driver
        XC_config = Xchange_config_page(self.driver)

    # add XC config
        XC_config.XC_config_click()
        time.sleep(2)

        XC_config.XC_addconfig_click()
        time.sleep(2)

        XC_config.XC_FC_click()
        time.sleep(5)

        XC_config.XC_TC_click()
        time.sleep(2)

        XC_config.XC_config_Rate("20")
        time.sleep(2)

        # fee_config.fee_config_fvalue("23")
        # time.sleep(2)

        XC_config.XC_addconfig_save_click()
        time.sleep(7)

        # small id searchbars
        # check whether added
        XC_config.Valid_XC_s_rate_sbars("20")
        time.sleep(5)

        # Edit/Delete
        XC_config.XC_Edit_click()
        time.sleep(5)

        XC_config.XC_eFC_click()
        time.sleep(5)

        XC_config.XC_eTC_click()
        time.sleep(5)

        XC_config.XC_config_eRate("30")
        time.sleep(5)

        XC_config.XC_addconfig_save_click()
        time.sleep(7)

        XC_config.eValid_XC_s_rate_sbars("30")
        time.sleep(5)

        XC_config.XC_SetDefault_click()
        time.sleep(5)

        driver.refresh()
        time.sleep(7)

        XC_config.eValid_XC_s_rate_sbars("30")
        time.sleep(5)

        #XC_config.Valid_XC_SetDefault()
        #time.sleep(5)

        XC_config.XC_Delete_click()
        time.sleep(3)

        XC_config.XC_E_D_ok_click()
        time.sleep(3)
        # fee_config.Valid_fc_id_s_searchbars("62")
        # time.sleep(5)

        # fee_config.fc_s_feevalue_sbars("")
        # time.sleep(5)
        # fee_config.Enable_button_click()
        # time.sleep(5)
        #
        # fee_config.status_E_ss_bars_click()
        # time.sleep(5)
        #
        # fee_config.Disble_button_click()
        # time.sleep(5)
        #
        # fee_config.status_D_ss_bars_click()
        # time.sleep(5)
        #
        # # Edit
        # fee_config.fc_fee_edit_click()
        # time.sleep(5)
        #
        # fee_config.fee_config_efname("lordi_1")
        # time.sleep(5)
        #
        # fee_config.feeconfig_eftype_click()
        # time.sleep(5)
        #
        # fee_config.fee_config_efvalue("25")
        # time.sleep(5)
        #
        # fee_config.addfeeconfig_savebutton_click()
        # time.sleep(7)
        #
        # fee_config.Valid1_fc_s_feename_sbars("lordi_1")
        # time.sleep(5)
        #
        # fee_config.fc_fee_delete_click()
        # time.sleep(5)