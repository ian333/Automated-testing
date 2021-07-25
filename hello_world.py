import unittest
import os
from pyunitreport import HTMLTestRunner
from selenium import webdriver



class HelloWorld(unittest.TestCase):
    @classmethod
    def setUp(cls):
        options=webdriver.ChromeOptions()
        options.binary_location='/usr/bin/brave-browser'
        driver_path = os.path.join(os.getcwd(), "chromedriver")
        cls.driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)
        driver=cls.driver
        driver.implicitly_wait(10)
        
    def test_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        self.driver.get('https://en.wikipedia.org')

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output ='reportes',report_name='Hello_world'))

