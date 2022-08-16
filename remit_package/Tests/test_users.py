import time

from remit_package.Pages.Users import Users_page
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
        User = Users_page(self.driver)

    # goto/click new remittances
        User.user_click()
        time.sleep(2)

        User.adduser_click()
        time.sleep(2)

        User.usr_FN("Jack")
        time.sleep(2)

        User.usr_LN("Reacher")
        time.sleep(2)

        User.usr_Email("jack@gmail.com")
        time.sleep(2)

        User.usr_country_code()
        time.sleep(2)

        User.usr_Phone_no("8887776665")
        time.sleep(2)

        User.usr_RemitCenter_click()
        time.sleep(2)

        User.usr_Role_click()
        time.sleep(2)

        User.usr_password("password@9876")
        time.sleep(2)

        User.usr_save_button_click()
        time.sleep(5)

        User.usr_v1_FN_s_searchbars("jack")
        time.sleep(2)

        # edit

        User.usr_editbutton_click()
        time.sleep(2)

        User.usr_eFN("Jacky")
        time.sleep(2)

        User.usr_eLN("Preacher")
        time.sleep(2)

        User.usr_eEmail("jacky@gmail.com")
        time.sleep(2)

        User.usr_ecountry_code()
        time.sleep(2)

        User.usr_ePhone_no("8882223334")
        time.sleep(2)

        User.usr_eRemitCenter_click()
        time.sleep(2)

        User.usr_eRole_click()
        time.sleep(2)

        # User.usr_epassword("pass")
        # time.sleep(2)

        User.usr_esave_button_click()
        time.sleep(5)

        User.usr_v2_eFN_s_searchbars("Jacky")
        time.sleep(2)

        User.usr_Del_ok_button_click()
        time.sleep(2)
