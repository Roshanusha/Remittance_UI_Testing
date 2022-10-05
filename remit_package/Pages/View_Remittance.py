import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page

class View_remit_page(Base_page):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # all clicks
        self.remittance_click_xpath = "//body/app-root/nav/div/ul/li[2]/a[1]"
        self.vr_click_xpath = "//a[@routerlink='view-remitances']" # view Remittance
        self.vr_select_center_xpath = "//div[@ng-reflect-tooltip-position='right']//div[@ng-reflect-ng-class='[object Object]']"
        self.vr_from_date_xpath = "//input[@placeholder='Start']"
        self.vr_till_date_xpath = "//body//app-root//input[2]"

        # small searches
        self.vr_Trans_id_xpath = "//th[1]//input[1]"
        self.vr_benef_name_xpath = "//th[2]//input[1]"
        self.vr_payer_name_xpath = "//th[3]//input[1]"
        self.vr_phone_no_xpath = "//th[4]//input[1]"
        self.vr_send_amt_xpath = "//th[5]//input[1]"
        self.vr_receive_amt_xpath = "//th[6]//input[1]"
        self.vr_Total_xpath = "//th[7]//input[1]"

    def remittance_nr_click(self):
        self.driver.find_element(By.XPATH, self.remittance_click_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.vr_click_xpath).click()

    def vr_select_center_click(self):
        self.driver.find_element(By.XPATH,  self.vr_select_center_xpath).click()
        select = Select(self.driver.find_element(By.XPATH,  self.vr_select_center_xpath))
        select.select_by_value("")
        print("selected item - " + select.first_selected_option.text)
        assert "" in select.first_selected_option.text

    def vr_from_date_click(self, FD):
        self.driver.find_element(By.XPATH, self.vr_from_date_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_from_date_xpath).send_keys(FD)

    def vr_till_date_click(self, TD):
        self.driver.find_element(By.XPATH, self.vr_till_date_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_till_date_xpath).send_keys(TD)

    # small searches
    def vr_trans_id_click(self, TransiD):
        self.driver.find_element(By.XPATH, self.vr_Trans_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_Trans_id_xpath).send_keys(TransiD)
        assert self.driver.find_element(By.XPATH, self.vr_Trans_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_Trans_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_benef_name_click(self, BN):
        self.driver.find_element(By.XPATH, self.vr_benef_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_benef_name_xpath).send_keys(BN)
        assert self.driver.find_element(By.XPATH, self.vr_benef_name_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_benef_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_payer_name_click(self, PN):
        self.driver.find_element(By.XPATH, self.vr_payer_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_payer_name_xpath).send_keys(PN)
        assert self.driver.find_element(By.XPATH, self.vr_payer_name_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_payer_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_phone_no_click(self, PhN):
        self.driver.find_element(By.XPATH, self.vr_phone_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_phone_no_xpath).send_keys(PhN)
        assert self.driver.find_element(By.XPATH, self.vr_phone_no_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_phone_no_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_send_amt_click(self, S_amt):
        self.driver.find_element(By.XPATH, self.vr_send_amt_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_send_amt_xpath).send_keys(S_amt)
        assert self.driver.find_element(By.XPATH, self.vr_send_amt_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_send_amt_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_receive_amt_click(self, R_amt):
        self.driver.find_element(By.XPATH, self.vr_receive_amt_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_receive_amt_xpath).send_keys(R_amt)
        assert self.driver.find_element(By.XPATH, self.vr_receive_amt_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_receive_amt_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def vr_total_amt_click(self, T_amt):
        self.driver.find_element(By.XPATH, self.vr_Total_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.vr_Total_xpath).send_keys(T_amt)
        assert self.driver.find_element(By.XPATH, self.vr_Total_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.vr_Total_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)