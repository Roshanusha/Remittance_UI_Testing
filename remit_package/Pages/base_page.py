from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


class Base_page:

    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        # self driver
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, value):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute ('innerText')

    def wait_for(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def wait_for1(self):
        self.wait.until(EC.visibility_of_element_located(()))

    def wait_for2(self):
         self.wait.until(EC.presence_of_element_located(()))