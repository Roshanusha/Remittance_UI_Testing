import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from remit_package.Pages.base_page import Base_page


class Fee_Config_page(Base_page):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # All clicks
        self.config_click_xpath = "//a[@id='navbarDropdowna']"
        # Add fee config
        self.fee_config_click_xpath = "//a[normalize-space()='Fee Config']"
        self.fee_addconfig_click_xpath = "//span[normalize-space()='Add Config']"
        self.fee_id_xpath = "//input[@id='validationCustomUsernamea']"
        self.feename_xpath = "//input[@placeholder='Fee Name']"
        self.feetype_click_xpath = "//select[@aria-label='Default select example']"
        # (By.XPATH, "//p-multiselect[@defaultlabel='Select Type']//div[@ng-reflect-ng-class='[object Object]']//div[@ng-reflect-ng-class='[object Object]']//span[@ng-reflect-ng-class='pi pi-chevron-down']")
        self.feetype1_click_xpath = "//select[@aria-label='Default select example']"
        self.feetype2_click_xpath = "//select[@aria-label='Default select example']"
        self.feevalue_click_xpath = "//input[@id='validationCustomUsername']"
        self.addslabrange_click_xpath = "//button[normalize-space()='Add Slab Range']"
        self.slab_fromvalue_click_xpath = "//input[@id='from']"
        self.slab_tovalue_click_xpath = "//input[@placeholder='To']"
        self.asr_savebutton_click_xpath = "//button[normalize-space()='Save']"
        self.addfeeconfig_savebutton_click_xpath = "//button[normalize-space()='Save']"
        # fee config Global search bar
        self.fc_gsearchbar_xpath = "//body[1]/app-root[1]/div[1]/app-fee-config-page[1]/div[1]/div[2]/p-table[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
        # small search bars
        self.fc_S_id_xpath = "//th[1]//input[1]"
        self.fc_S_feename_xpath = "//th[2]//input[1]"
        self.fc_S_feevalue_xpath = "//th[4]//input[1]"
        # Actions
        # Edit
        self.fc_fedit_xpath = "//body[1]/app-root[1]/div[1]/app-fee-config-page[1]/div[1]/div[2]/p-table[1]/" \
                              "/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[6]/button[1]/span[1]"
        self.Enable_button_xpath = "//tbody/tr[1]/td[6]/button[3]/span[1]"
        self.Disable_button_xpath = "//tbody/tr[1]/td[6]/button[3]/span[1]"
        # Delete
        self.fc_fdelete_xpath = "//tbody//button[2]//span[1]"
        #e/d ok
        self.fc_e_d_ok_button_xpath = "//ngb-modal-window[@role='dialog']//button[2]"
# Clicks
    def config_click(self):
        self.driver.find_element(By.XPATH, self.config_click_xpath).click()

    def fee_config_click(self):
        self.driver.find_element(By.XPATH, self.fee_config_click_xpath).click()


    def fee_addconfig_click(self):
        self.driver.find_element(By.XPATH, self.fee_addconfig_click_xpath).click()


    def feeconfig_ftype_click(self):    # percentage
        self.driver.find_element(By.XPATH, self.feetype_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.feetype_click_xpath))
        select.select_by_visible_text("PERCENTAGE-%")
        print("selected item - " + select.first_selected_option.text)
        assert "PERCENTAGE-%" in select.first_selected_option.text

    def feeconfig_eftype_click(self):    # percentage,flat,slab
        self.driver.find_element(By.XPATH, self.feetype_click_xpath).click()
        select = Select(self.driver.find_element(By.XPATH, self.feetype_click_xpath))
        select.select_by_value("FLAT")
        print("selected item - " + select.first_selected_option.text)
        assert "FLAT" in select.first_selected_option.text

    def feeconfig_ftype1_click(self):      # flat
        self.driver.find_element(By.XPATH, self.feetype1_click_xpath).click()

    def feeconfig_ftype2_click(self):    # slab
        self.driver.find_element(By.XPATH, self.feetype2_click_xpath).click()

    def addslabrange_ftype2_click(self):
        self.driver.find_element(By.XPATH, self.addslabrange_click_xpath).click()

    def addslabrange_savebutton_click(self):
        self.driver.find_element(By.XPATH, self.asr_savebutton_click_xpath).click()

    def addfeeconfig_savebutton_click(self):
        self.driver.find_element(By.XPATH, self.addfeeconfig_savebutton_click_xpath).click()

    def status_E_ss_bars_click(self):
        #self.driver.find_element(By.XPATH, "//p-multiselect[@defaultlabel='Select']//div[@ng-reflect-ng-class='[object Object]']//div[@ng-reflect-ng-class='[object Object]']/"
                                          # "/span[@ng-reflect-ng-class='pi pi-chevron-down']").click()
        #self.driver.find_element(By.XPATH, "//li[@aria-label='Enabled']//div//div[@ng-reflect-ng-class='[object Object]']").click()
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "Enabled"
        print(ele)
        time.sleep(5)

    def status_D_ss_bars_click(self):
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[5]")).text
        assert ele == "Disabled"
        print(ele)
        time.sleep(5)

    def Enable_button_click(self):
        self.driver.find_element(By.XPATH, self.Enable_button_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.fc_e_d_ok_button_xpath).click()

    def Disble_button_click(self):
        self.driver.find_element(By.XPATH, self.Disable_button_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.fc_e_d_ok_button_xpath).click()

    # Fee Edit/Delete
    def fc_fee_edit_click(self):
        self.driver.find_element(By.XPATH, self.fc_fedit_xpath).click()

    def fc_fee_delete_click(self):
        self.driver.find_element(By.XPATH, self.fc_fdelete_xpath).click()
        self.driver.find_element(By.XPATH,  self.fc_e_d_ok_button_xpath).click()

    # Add Fee_config
    def fee_config_fname(self, feeconfig_feename):
        self.driver.find_element(By.XPATH, self.feename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.feename_xpath).send_keys(feeconfig_feename)

    def fee_config_efname(self, feeconfig_efeename):
        self.driver.find_element(By.XPATH, self.feename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.feename_xpath).send_keys(feeconfig_efeename)


    def fee_config_fvalue(self, feeconfig_feevalue):
        self.driver.find_element(By.XPATH, self.feevalue_click_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.feevalue_click_xpath).send_keys(feeconfig_feevalue)


    def fee_config_efvalue(self, feeconfig_efeevalue):
        self.driver.find_element(By.XPATH, self.feevalue_click_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.feevalue_click_xpath).send_keys(feeconfig_efeevalue)


    def slab_from_value(self,fromvalue):
        self.driver.find_element(By.XPATH, self.slab_fromvalue_click_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.slab_fromvalue_click_xpath).send_keys(fromvalue)


    def slab_to_value(self,tovalue):
        self.driver.find_element(By.XPATH, self.slab_fromvalue_click_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.slab_fromvalue_click_xpath).send_keys(tovalue)

        # fee config searchbars
    def fc_g_searchbars(self, fc_gs_centrename_bar):       # fc_g-fee config global

        self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(fc_gs_centrename_bar)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.fc_gsearchbar_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def fc_id_s_searchbars(self, fc_ss_id_bar):
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(fc_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def fc_s_feename_sbars(self, fc_ss_feename_bar):   # same for validation
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(fc_ss_feename_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).get_attribute("value") == "lordi"
        time.sleep(5)
        ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[2]")).text
        assert ele1 == "lordi"
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def fc_s_feevalue_sbars(self, fc_ss_feevalue_bar):
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(fc_ss_feevalue_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).get_attribute("value") == "12"
        time.sleep(5)
        ele2 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele2 == "12"
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    #  for validation
    def Valid_fc_id_s_searchbars(self, vfc_ss_id_bar):
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(vfc_ss_id_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_id_xpath).get_attribute("value") == "62"
        time.sleep(3)
        ele = self.wait_for((By.XPATH, "//tbody/tr[1]/td[1]")).text
        assert ele == "00062"
        self.driver.find_element(By.XPATH, self.fc_S_id_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def Valid_fc_s_feename_sbars(self, vfc_ss_feename_bar):   # same for validation
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(vfc_ss_feename_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).get_attribute("value") == "lordi"
        time.sleep(5)
        ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[2]")).text
        assert ele1 == "lordi"
        #self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def Valid1_fc_s_feename_sbars(self, vfc_ss_feename_bar):   # same for validation
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a',Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(vfc_ss_feename_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).get_attribute("value") == "lordi_1"
        time.sleep(5)
        ele1 = self.wait_for((By.XPATH,"//tbody/tr[1]/td[2]")).text
        assert ele1 == "lordi_1"
        #self.driver.find_element(By.XPATH, self.fc_S_feename_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    def Valid_fc_s_feevalue_sbars(self, vfc_ss_feevalue_bar):
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(vfc_ss_feevalue_bar)
        assert self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).get_attribute("value") == "12"
        time.sleep(5)
        ele2 = self.wait_for((By.XPATH, "//tbody/tr[1]/td[4]")).text
        assert ele2 == "12"
        self.driver.find_element(By.XPATH, self.fc_S_feevalue_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

