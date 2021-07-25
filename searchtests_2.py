import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from urllib3.packages.six import assertCountEqual


class SearchTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_tee(self):
        driver=self.driver
        search_field = driver.find_element_by_id("search")
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
        products = driver.find_elements_by_class_name('item last')
        self.assertTrue(5,len(products))
        self.assertGreater(1,len(products))

    def test_search_salt_shaker(self):
        driver=self.driver
        search_field = driver.find_element_by_id("search")
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()
        products = driver.find_elements_by_class_name('item last')
        self.assertTrue(1,len(products))


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Search__test_2'))
