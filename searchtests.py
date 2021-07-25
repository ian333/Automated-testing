import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from urllib3.packages.six import assertCountEqual


class HomePageTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', chrome_options=options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
        pass

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        search_field=self.driver.find_element_by_class_name("input-text required-entry")

    def test_search_button_enabled(self):
        search_field=self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list= self.driver.find_element_by_class_name("promos")
        banners=banner_list.find_element_by_tag_name("img")
        self.assertEqual(3,len(banners))

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='Hello_world'))
