import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common import by
from urllib3.packages.six import assertCountEqual
from selenium.common.exceptions import NoSuchElementException

class AssertionsTest(unittest.TestCase):
    def setUp(self):
        
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(by.By.NAME,'q'))
    
    def test_language_selector(self):
        self.assertTrue(self.is_element_present(by.By.ID,'select-language'))
    

    def tearDown(self):
        self.driver.close()

    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how,value=what)

        except NoSuchElementException as variable:
            return False
        return True
            

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Assertions'))
