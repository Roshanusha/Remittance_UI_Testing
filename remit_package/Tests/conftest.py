import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        serv_obj = Service("G:/chromedriver_win32/chromedriver.exe")

        website = 'https://remitui-staging.azurewebsites.net/'
        # webdriver_path = 'G:/chromedriver_win32/chromedriver.exe'
        driver = webdriver.Chrome(service=serv_obj)

        wait = WebDriverWait(driver, 10)

        driver.get(website)
        print(driver.title)  # Actual title of 1st page

        driver.maximize_window()
    # elif browser_name == "firefox":
    #         # browser invocation (driver)
    #
    # elif browser_name == "IE":
    #         # IE browser invocation (driver)

    driver.get(website)
    print(driver.title)  # Actual title of 1st page

    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
