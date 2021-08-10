from time import sleep
from typing import Text
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import Select

class CompareProducts (unittest.TestCase):
    def setUp(self):
        
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_compare_products_removal_alert(self):
        driver=self.driver
        search_field=driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Tee')
        search_field.submit()
        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        alert=driver.switch_to_alert()
        alert_text=alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
        alert.accept()
    



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Alerts'))
