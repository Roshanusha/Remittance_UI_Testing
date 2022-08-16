import self
from selenium.webdriver.common.keys import Keys

from remit_package.Pages.login_page import LoginPage
from remit_package.Pages.Remit_center import Remittance_center
from remit_package.Utilities.BaseClass import BaseClass
from remit_package.Pages.base_page import Base_page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


class Test_1_main(BaseClass):

    # wait = WebDriverWait(self.driver, 10)

    def test_login_valid(self):

        driver = self.driver
        # wait = WebDriverWait(self.driver, 10)
        login = LoginPage(self.driver)  # class name
        login.enter_username("demo@gmail.com")
        login.enter_password("Password@1234")
        login.click_login()
        driver.implicitly_wait(10)

    def test_remittance_center_valid(self):
        driver = self.driver

        # Global Search
        remit = Remittance_center(self.driver)

        remit.g_searchbars("Austin Center")
        time.sleep(5)
        remit.g_searchbars("Chicago")
        time.sleep(5)

        # Small search Bars
        remit.s_searchbars("28")
        time.sleep(5)

        remit.s_searchbars1("Boston")
        time.sleep(5)

        remit.s_searchbars2("Chicago")
        time.sleep(5)

        # Add New Center
        remit.all_clicks1()
        driver.implicitly_wait(5)
        remit.add_new_cntr("Texas Center")
        time.sleep(5)

        remit.add_new_cntr1("Tex City")
        time.sleep(5)

        remit.add_new_cntr2("texas")
        time.sleep(5)

        remit.add_new_cntr3("673102")
        time.sleep(5)

        remit.add_new_cntr4("main street 123")
        time.sleep(5)

        remit.add_new_cntr5("hollywood street")
        time.sleep(5)

        remit.all_clicks2()
        time.sleep(5)

        # Check newly added one
        remit.valid_s_searchbars1("Texas Center")
        time.sleep(5)

        # Edit/Delete fn
        remit.all_clicks3()
        time.sleep(5)
        remit.ed_actions("Texas Center_1")
        time.sleep(5)

        remit.ed_actions1("Tex City_1")
        time.sleep(5)

        remit.ed_actions2("texas_1")
        time.sleep(5)

        remit.ed_actions3("673102_1")
        time.sleep(5)

        remit.ed_actions4("main street 123_1")
        time.sleep(5)

        remit.ed_actions5("hollywood street_1")
        time.sleep(5)

        remit.all_clicks4()
        time.sleep(5)

        remit.valid_ed_actions("Texas Center_1")
        time.sleep(5)

        remit.all_clicks5()
        time.sleep(5)

        remit.all_clicks6()
        time.sleep(5)
