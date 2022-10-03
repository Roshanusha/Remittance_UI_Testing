import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from remit_package.Pages.base_page import Base_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Remittance_center(Base_page):

    # Global Search

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.GS_Tagname_xpath = "//a[@class='nav-link active']"
        # self.GS_id_xpath = "//input[@class='p-inputtext p-component']"
        self.GS_box_xpath = "/html[1]/body[1]/app-root[1]/div[1]/app-remitance-centers-page[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
        # self.GS_cityname_xpath = "//input[@class='p-inputtext p-component']"

        # Small search Bars
        # Id search
        self.S_id_xpath = "//th[1]//input[1]"

        # center name
        self.S_centername_xpath = "//th[2]//input[1]"

        # city name
        self.S_cityname_xpath =  "//th[3]//input[1]"


        # Add New Center
        self.Addnewcntr_button_xpath = "//span[normalize-space()='Add New Center']"
        self.Cntrname_xpath = "//input[@id='avalidationCustomUsernamea']"
        self.cityname_xpath = "//input[@id='validationCustom0a5']"
        self.statename_xpath = "//div[@class='form-row mt-3']//input[@id='validationCustom05']"
        self.pincode_xpath = "//div[@class='form-row mt-3']//input[@id='validationCustom07']"
        self.addr1_xpath = "//div[@class='form-row']//input[@id='validationCustom05']"
        self.addr2_xpath = "//div[@class='form-row']//input[@id='validationCustom07']"
        self.save_button_xpath = "//button[normalize-space()='Save']"

    # Actions
    # Edit
        self.eAddnewcntr_button_xpath ="//body[1]/app-root[1]/div[1]/app-remitance-centers-page[1]/div[1]/p-table[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/button[1]/span[1]"
        self.eCntrname_xpath = "//input[@id='avalidationCustomUsernamea']"
        self.ecityname_xpath = "//input[@id='validationCustom0a5']"
        self.estatename_xpath = "//div[@class='form-row mt-3']//input[@id='validationCustom05']"
        self.epincode_xpath =  "//div[@class='form-row mt-3']//input[@id='validationCustom07']"
        self.eaddr1_xpath = "//div[@class='form-row']//input[@id='validationCustom05']"
        self.eaddr2_xpath = "//div[@class='form-row']//input[@id='validationCustom07']"
        self.esave_button_xpath = "//button[normalize-space()='Save']"

    # Delete
        self.del_button_xpath = "//body[1]/app-root[1]/div[1]/app-remitance-centers-page[1]/div[1]/p-table[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/button[2]/span[1]"
        self.del_ok_button_xpath = "//ngb-modal-window[@role='dialog']//button[2]"

    # SearchBars
    def g_searchbars(self, gs_centrename_bar):
        #i = 0 # ["gs_centrename_bar"]
        # gs_centrename_bar = ["Austin Center", "Chicago"]
        #for i in gs_centrename_bar:
        self.driver.find_element(By.XPATH, self.GS_box_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.GS_box_xpath).send_keys(gs_centrename_bar)
        # print(self.driver.find_element(By.XPATH, self.GS_box_xpath).get_attribute("value"))
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.GS_box_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        # i = i+1
        #print(i)
        # self.wait.until(EC.visibility_of_element_located(()))
        # self.driver.find_element(By.XPATH, self.GS_box_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def s_searchbars(self, ss_id_bar):
        self.driver.find_element(By.XPATH,self.S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,self.S_id_xpath).send_keys(ss_id_bar)
        assert self.driver.find_element(By.XPATH,self.S_id_xpath).get_attribute("value") == "28"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00020"
        self.driver.find_element(By.XPATH, self.S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def s_searchbars1(self, ss_centername_bar):
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(ss_centername_bar)
        assert self.driver.find_element(By.XPATH, self.S_centername_xpath).get_attribute("value") == "Boston"
        time.sleep(5)
        ele1 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele1 == "Boston office"
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def valid_s_searchbars1(self, v_ss_centername_bar):
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(v_ss_centername_bar)
        assert self.driver.find_element(By.XPATH, self.S_centername_xpath).get_attribute("value") == "Texas Center"
        time.sleep(5)
        ele_v = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele_v == "Texas Center"

    def s_searchbars2(self, ss_cityname_bar):
        self.driver.find_element(By.XPATH,self.S_cityname_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH,self.S_cityname_xpath).send_keys(ss_cityname_bar)
        assert self.driver.find_element(By.XPATH,self.S_cityname_xpath).get_attribute("value") == "Chicago"
        time.sleep(3)
        ele2 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[3]")).text
        assert ele2 == "Chicago"
        self.driver.find_element(By.XPATH, self.S_cityname_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def add_new_cntr(self, add_n_center_centername):
        self.driver.find_element(By.XPATH, self.Cntrname_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.Cntrname_xpath).send_keys(add_n_center_centername)
        assert self.driver.find_element(By.XPATH, self.Cntrname_xpath).get_attribute("value") == "Texas Center"
        time.sleep(3)

    def add_new_cntr1(self,  add_n_center_cityname):
        self.driver.find_element(By.XPATH, self.cityname_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.cityname_xpath).send_keys(add_n_center_cityname)
        assert self.driver.find_element(By.XPATH, self.cityname_xpath).get_attribute("value") == "Tex City"
        time.sleep(3)

    def add_new_cntr2(self, add_n_center_statename):
        self.driver.find_element(By.XPATH, self.statename_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.statename_xpath).send_keys(add_n_center_statename)
        assert self.driver.find_element(By.XPATH, self.statename_xpath).get_attribute("value") == "texas"
        time.sleep(3)

    def add_new_cntr3(self,add_n_center_pincode):
        self.driver.find_element(By.XPATH, self.pincode_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.pincode_xpath).send_keys(add_n_center_pincode)
        assert self.driver.find_element(By.XPATH, self.pincode_xpath).get_attribute("value") == "673102"
        time.sleep(3)


    def add_new_cntr4(self,  add_n_center_addr1):
        self.driver.find_element(By.XPATH, self.addr1_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.addr1_xpath) .send_keys(add_n_center_addr1)
        assert self.driver.find_element(By.XPATH, self.addr1_xpath).get_attribute("value") == "main street 123"
        time.sleep(3)

    def add_new_cntr5(self, add_n_center_addr2):
        self.driver.find_element(By.XPATH, self.addr2_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.addr2_xpath).send_keys(add_n_center_addr2)
        assert self.driver.find_element(By.XPATH, self.addr2_xpath).get_attribute("value") == "hollywood street"
        time.sleep(3)

    # Edit
    def ed_actions(self, e_centrename):
        self.driver.find_element(By.XPATH, self.eCntrname_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)  # center name
        self.driver.find_element(By.XPATH, self.eCntrname_xpath).send_keys(e_centrename)

    def valid_ed_actions(self, v_e_centrename):
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.S_centername_xpath).send_keys(v_e_centrename)
        assert self.driver.find_element(By.XPATH, self.S_centername_xpath).get_attribute("value") == "Texas Center_1"
        time.sleep(5)
        ele_v = self.wait_for((By.XPATH, "//tbody/tr[1]/td[2]")).text
        assert ele_v == "Texas Center_1"

    def ed_actions1(self, e_cityname):
        self.driver.find_element(By.XPATH, self.ecityname_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.ecityname_xpath).send_keys(e_cityname)

    def ed_actions2(self, e_statename):
        self.driver.find_element(By.XPATH, self.estatename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.estatename_xpath).send_keys(e_statename)

    def ed_actions3(self, e_pincode):
        self.driver.find_element(By.XPATH, self.epincode_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.epincode_xpath).send_keys(e_pincode)

    def ed_actions4(self, e_addr1):
        self.driver.find_element(By.XPATH, self.eaddr1_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.eaddr1_xpath).send_keys(e_addr1)

    def ed_actions5(self, e_addr2):
        self.driver.find_element(By.XPATH, self.eaddr2_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.eaddr2_xpath).send_keys(e_addr2)

    # Clicks
    def all_clicks(self):
        self.driver.find_element(By.XPATH, self.GS_Tagname_xpath).click()

    def all_clicks1(self):
        self.driver.find_element(By.XPATH, self.Addnewcntr_button_xpath).click()

    def all_clicks2(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def all_clicks3(self):
        self.driver.find_element(By.XPATH, self.eAddnewcntr_button_xpath).click()

    def all_clicks4(self):
        self.driver.find_element(By.XPATH, self.esave_button_xpath).click()

    def all_clicks5(self):
        self.driver.find_element(By.XPATH, self.del_button_xpath).click()

    def all_clicks6(self):
        self.driver.find_element(By.XPATH, self.del_ok_button_xpath).click()




