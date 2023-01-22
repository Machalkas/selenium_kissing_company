import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest

# class TestStringMethods(unittest.TestCase):
# #     def setUp(self) -> None:
# #         EXE_PATH =  r'D:\program files\PProject\selent5\GoogleDriver\chromedriver.exe'
# #         self.driver = webdriver.Chrome(executable_path=EXE_PATH)
# #         self.driver.get("http://localhost:33770/")
# #
# #     def testInputFieldCount(self):
# #         auth_elements = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
# #         assert len(auth_elements) == 2, f"Found {len(auth_elements)}, but 2 was preferred"
# #
# #
# #     def testLogin(self):
# #         username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
# #         button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
# #         button = button_span.find_element(By.XPATH, "..")
# #         username.send_keys("user")
# #         password.send_keys('123')
# #         button.click()
# #         assert self.driver.current_url == 'http://localhost:33770/user', "Fail to login"

class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        EXE_PATH = f'{os.getcwd()}\GoogleDriver\chromedriver.exe'
        #EXE_PATH = r'D:\program files\PProject\selent5\GoogleDriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.driver.get("http://localhost:33770/")
    
    # def tearDown(self) -> None:
    #     self.driver.close()

    def testfirst(self):
        try:
            self.driver.find_element(By.XPATH, "//label[contains(text(), 'Логин')]")
        except Exception as ex:
            print(ex)

    def testInputFieldCount(self):
        ##понять на какой странице
        auth_elements = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        assert len(auth_elements) == 2, f"Found {len(auth_elements)}, but 2 was preferred"

    def testLogin(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        time.sleep(5)
        assert self.driver.current_url == 'http://localhost:33770/user', "Fail to login"

    def testCatalog(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        time.sleep(2)
        #button2 = self.driver.find_element(By.XPATH, "//button[contains(@class, 'v-app-bar__nav-icon v-btn v-btn--icon v-btn--round theme--dark v-size--default')]")
        button2 = self.driver.find_element(By.CLASS_NAME, "v-btn__content")
        button22 = button2.find_element(By.XPATH, "..")
        button22.click()
        time.sleep(2)
        catalog = self.driver.find_element(By.XPATH, "//div[contains (@class, 'v-list-item__title') and text() = 'Все дефки']")
        catalog.click()
        time.sleep(2)
        filter = self.driver.find_element(By.XPATH, "//span[contains (@class, 'v-btn__content') and text() = ' Показать фильтр ']")
        filterDaddy = filter.find_element(By.XPATH, "..")
        filterDaddy.click()
        time.sleep(1)
        hideFilter = self.driver.find_element(By.XPATH, "//span[contains (@class, 'v-btn__content') and text() = ' Скрыть фильтр ']")
        assert hideFilter.is_displayed(), "Filter is not displayed"
        assert self.driver.current_url == 'http://localhost:33770/user/girls', "Fail to login"

    def testServiceHistory(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        time.sleep(2)
        #button2 = self.driver.find_element(By.XPATH, "//button[contains(@class, 'v-app-bar__nav-icon v-btn v-btn--icon v-btn--round theme--dark v-size--default')]")
        button2 = self.driver.find_element(By.CLASS_NAME, "v-btn__content")
        button22 = button2.find_element(By.XPATH, "..")
        button22.click()
        time.sleep(2)
        catalog = self.driver.find_element(By.XPATH, "//div[contains (@class, 'v-list-item__title') and text() = 'История заказов']")
        catalog.click()
        time.sleep(2)
        serviceHistory = self.driver.find_element(By.XPATH, "//div[contains (@class, 'row row--dense')]")
        assert serviceHistory.is_displayed(), "history doesnt work"
        assert self.driver.current_url == 'http://localhost:33770/user/history', "Fail to login"

    def testFeedbacks(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        # button_span2 = self.driver.find_element(By.CLASS_NAME, 'v-btn__content')
        # button2 = button_span2.find_element(By.XPATH, "..")
        time.sleep(2)
        # button2 = self.driver.find_element(By.XPATH, "//button[contains(@class, 'v-app-bar__nav-icon v-btn v-btn--icon v-btn--round theme--dark v-size--default')]")
        button2 = self.driver.find_element(By.CLASS_NAME, "v-btn__content")
        button22 = button2.find_element(By.XPATH, "..")
        button22.click()
        time.sleep(2)
        catalog = self.driver.find_element(By.XPATH, "//div[contains (@class, 'v-list-item__title') and text() = 'Отзывы о приложении']")
        catalog.click()
        time.sleep(2)
        feedbacksList = self.driver.find_element(By.XPATH, "//div[contains (@class, 'user-comment')]")
        assert feedbacksList.is_displayed(), "Feedbackov NETY I BIT NE MOJET"
        assert self.driver.current_url == 'http://localhost:33770/user/appfeedback', "Fail to login"

    def testExit(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        time.sleep(2)
        # button2 = self.driver.find_element(By.XPATH, "//button[contains(@class, 'v-app-bar__nav-icon v-btn v-btn--icon v-btn--round theme--dark v-size--default')]")
        button2 = self.driver.find_element(By.CLASS_NAME, "v-btn__content")
        button22 = button2.find_element(By.XPATH, "..")
        button22.click()
        time.sleep(2)
        catalog = self.driver.find_element(By.XPATH, "//div[contains (@class, 'v-list-item__title') and text() = 'Выйти']")
        catalog.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://localhost:33770/', "Fail to login"