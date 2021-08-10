import unittest
import os
from pyunitreport import HTMLTestRunner
from selenium import webdriver



class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUp(cls):
        options=webdriver.ChromeOptions()
        options.binary_location='/usr/bin/brave-browser'
        driver_path = os.path.join(os.getcwd(), "chromedriver")
        cls.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)
        driver=cls.driver
        driver.implicitly_wait(10)

    def test_new_user(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button=driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Custommer Account',driver.title)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


