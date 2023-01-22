from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class TestStringMethods(unittest.TestCase):
    def testfirst(self):
        EXE_PATH = r'D:\program files\PProject\TestingSelenium\GoogleDriver\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=EXE_PATH)
        driver.get("http://localhost:33770/")
        try:
            driver.find_element(by = 'id', value ="input-35").is_displayed()
        except Exception as ex:
            print(ex)
        # assert "Логин" in driver.label

