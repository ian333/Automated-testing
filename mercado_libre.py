from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common import by
from urllib3.packages.six import assertCountEqual
from selenium.common.exceptions import NoSuchElementException

class Mercado_libre_Test(unittest.TestCase):
    def setUp(self):
        print("""
 
        This test script makes a search in Mercado Libre Colombia for a Playstation 3
        and stablish the locacion in bogota then filter by new products
         and finally sets the view from the lower price to the higher price

        """)
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://mercadolibre.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_ps4(self):
        """
        Esta Funcion hace una busqueda en Mercado Libre Colombia y establece como ubicacion Bogota
        Filtra los productos nuevos y los ordena de mayor precio a menor precio

        """

        driver=self.driver
        country=driver.find_element_by_id('CO')
        country.click()
        search_field=driver.find_element_by_name('as_word')
        search_field.clear()
        search_field.send_keys('Playstation 4')
        search_field.submit()
        sleep(3)

        accept_cookies= driver.find_element_by_id('newCookieDisclaimerButton')
        accept_cookies.click()
        sleep(1)

        ###location=driver.find_element_by_partial_link_text('Bogotá D.C.')
        location=driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section/dl[18]/dd[1]/a/span[1]')
        location.click()
        sleep(3)
        condition=driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)
        order_menu=driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        sleep(3)
        higher_price=driver.find_element_by_partial_link_text('Mayor precio')
        higher_price.click()
        sleep(3)
        articles=[]
        prices=[]
        
        for i in range(5):
            articles_name=driver.find_elements_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            articles.append(articles_name)
            article_prices=driver.find_elements_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            article_prices.append(prices)
        print(articles,article_prices)
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Mercado_libre'))
