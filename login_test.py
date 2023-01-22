import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        EXE_PATH = f'{os.getcwd()}\GoogleDriver\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.driver.get("http://localhost:33770/")

    def testInputFieldCount(self):
        auth_elements = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        assert len(auth_elements) == 2, f"Found {len(auth_elements)}, but 2 was preferred"

    
    def testLogin(self):
        username, password = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'input-')]")
        button_span = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
        button = button_span.find_element(By.XPATH, "..")
        username.send_keys("user")
        password.send_keys('123')
        button.click()
        assert self.driver.current_url == 'http://localhost:33770/user', "Fail to login"
