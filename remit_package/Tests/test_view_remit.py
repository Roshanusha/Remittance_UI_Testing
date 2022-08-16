import time

from remit_package.Pages.View_Remittance import View_remit_page
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

    def test_view_remittance_valid(self):
       # driver = self.driver
        v_remit = View_remit_page(self.driver)

       #clicks
        v_remit.remittance_nr_click()
        time.sleep(2)

        v_remit.vr_select_center_click()
        time.sleep(2)



