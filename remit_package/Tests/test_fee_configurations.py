import self
from selenium.webdriver.common.keys import Keys

from remit_package.Pages.login_page import LoginPage
from remit_package.Pages.Fee_Configurations import Fee_Config_page
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

    def test_fee_configuration_valid(self):

        driver = self.driver
        fee_config = Fee_Config_page(self.driver)

    # add fee config(percentage
        fee_config.config_click()
        time.sleep(2)

        fee_config.fee_config_click()
        time.sleep(2)

        fee_config.fee_addconfig_click()
        time.sleep(5)

        fee_config.fee_config_fname("lordi")
        time.sleep(2)

        fee_config.feeconfig_ftype_click()
        time.sleep(2)

        fee_config.fee_config_fvalue("23")
        time.sleep(2)

        fee_config.addfeeconfig_savebutton_click()
        time.sleep(7)

        # small id searchbars
        # check whether added
        fee_config.Valid_fc_s_feename_sbars("lordi")
        time.sleep(5)

        # fee_config.Valid_fc_id_s_searchbars("62")
        # time.sleep(5)

        # fee_config.fc_s_feevalue_sbars("")
        # time.sleep(5)
        fee_config.Enable_button_click()
        time.sleep(5)

        fee_config.status_E_ss_bars_click()
        time.sleep(5)

        fee_config.Disble_button_click()
        time.sleep(5)

        fee_config.status_D_ss_bars_click()
        time.sleep(5)

        # Edit
        fee_config.fc_fee_edit_click()
        time.sleep(5)

        fee_config.fee_config_efname("lordi_1")
        time.sleep(5)

        fee_config.feeconfig_eftype_click()
        time.sleep(5)

        fee_config.fee_config_efvalue("25")
        time.sleep(5)

        fee_config.addfeeconfig_savebutton_click()
        time.sleep(7)

        fee_config.Valid1_fc_s_feename_sbars("lordi_1")
        time.sleep(5)

        fee_config.fc_fee_delete_click()
        time.sleep(5)