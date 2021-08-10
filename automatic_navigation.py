from time import sleep
from typing import Text
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import Select

class automatic_navigation (unittest.TestCase):
    def setUp(self):
        
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://google.com')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_browser_navigation(self):
        driver=self.driver
        search_field=driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        platzi_select=driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
        platzi_select.click()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()


    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Automatic Navigation'))
