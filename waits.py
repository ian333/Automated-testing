import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import Select



class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):

        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable((By.NAME, 'q')))
        account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

        pass

    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains('Create New Customer Account'))
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Waits'))
