from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from remit_package.Pages.base_page import Base_page


class LoginPage(Base_page):

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = "//input[@placeholder='Email']"
        self.password_textbox_xpath = "//input[@placeholder='Password']"
        self.login_button_xpath = "//button[normalize-space()='Sign in']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
