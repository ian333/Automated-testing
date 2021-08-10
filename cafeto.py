from os import close
from time import sleep
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common import by
from urllib3.packages.six import assertCountEqual
from selenium.common.exceptions import NoSuchElementException

class Mercado_libre_Test(unittest.TestCase):
    def setUp(self):
        
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave-browser'
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver', options=options)
        driver = self.driver
        driver.get('http://cafeto.co/')
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    def test_cafeto_web(self):
        """
        docstring
        """
        driver=self.driver
        accept_cookies=driver.find_element_by_id('cookie_action_close_header')
        accept_cookies.click()
        sleep(1)
        for _ in range(1):
            roll_front_images_right=driver.find_element_by_xpath('//*[@id="cafeto-home-section"]/section/div[3]')
            roll_front_images_right.click()
            
        for _ in range(1):
            roll_front_images_left=driver.find_element_by_xpath('//*[@id="cafeto-home-section"]/section/div[4]')
            roll_front_images_left.click()


        sleep(1)
        blog=driver.find_element_by_partial_link_text('Blog')
        blog.click()
        sleep(1)
        for i in range(60):
            driver.execute_script(f"window.scrollTo(0, {i*14})")
        sleep(2)     

        blog_topic=driver.find_element_by_xpath('//*[@id="cafeto-archive-blog"]/div[3]/div/div[2]/div/div[2]/a')
        blog_topic.click()
        for i in range(120):
            driver.execute_script(f"window.scrollTo(0, {i*100})")
            sleep(0.01)
        sleep(0.2)   
        for i in range(120,0,-1):
            driver.execute_script(f"window.scrollTo(0, {i*100})")
            sleep(0.01)
        sleep(2)   
         

        about_us=driver.find_element_by_partial_link_text('About Us')
        about_us.click()
        sleep(1) 
        for i in range(60):
            driver.execute_script(f"window.scrollTo(0, {i*17})")
        join_our_team=driver.find_element_by_xpath('//*[@id="cafeto-about-us"]/div[3]/div/div[1]/div[2]/a')
        join_our_team.click()
        sleep(0.1) 
        for i in range(60):
            driver.execute_script(f"window.scrollTo(0, {i*14})")


        qa_tester=driver.find_element_by_xpath('//*[@id="JazzHrJobs"]/div[4]/div/div[2]/a')
        qa_tester.click()

        window_after = driver.window_handles[1]
        
        driver.switch_to_window(driver.window_handles[1])
        apply=driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/input')
        apply.click()
        
        sleep(2)

        first_name=driver.find_element_by_name('CandidateFirstName')
        first_name.clear()
        first_name.send_keys('Sebastian')
        last_name=driver.find_element_by_name('CandidateLastName')
        last_name.clear()
        last_name.send_keys('Vazquez')
        email=driver.find_element_by_name('CandidateEmail')
        email.clear()
        email.send_keys('sebastianvaz123@hotmail.com')

        write_now=driver.find_element_by_xpath('//*[@id="form"]/div[6]/div[1]/span/label[2]')
        write_now.click()
        sleep(1)

        cover_note=driver.find_element_by_id('CandidateCoverNote')
        cover_note.clear()
        text='Hi ✌️😁 this is an example of my skills, i hope you enjoyed 🧐🧐'
        driver.execute_script("arguments[0].innerHTML = '{}'".format(text),cover_note)
        cover_note.send_keys('.')
        
        sleep(10)

        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=3, testRunner=HTMLTestRunner(
        output='reportes', report_name='Mercado_libre'))
