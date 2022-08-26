import time

from appium import webdriver
import pytest
from time import sleep


class TestLogin:
    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities={
                                           "platformName": "android",
                                           "appium:platformVersion": "13",
                                           "appium:deviceName": "Pixel-4",
                                           "appium:appPackage": "com.enthuziastic.mobileapp.staging",
                                           "appium:appActivity": "com.enthuziastic.mobileapp.MainActivity"
                                       })

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        time.sleep(5)
        self.driver.find_element("accessibility id", "I'll do it later").click()
        # self.driver.find_element("accessibility id", "Sign In").click()
