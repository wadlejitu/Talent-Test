from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'niveditakhoche'

import unittest
from selenium import webdriver
import ConfigParser

my_var = 1

USERNAME = "nivedita.khoche@dice.com"
PASSWORD = "password"


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        print 'setup'
        self.browser = None
        self.login()

    def tearDown(self):
        print 'tearing down'
        #self.browser.quit()

    def login(self):
        print 'test_login'
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.cfg'))
        browsers = config.get("Default", "browsers").split(',')

        browser = self.browser = webdriver.Chrome()
        browser.get("https://gettalent.com/web")
        email_input = browser.find_element_by_id("user_email")
        email_input.send_keys(USERNAME)
        password_input = browser.find_element_by_id("user_password")
        password_input.send_keys(PASSWORD)
        login_buttons = browser.find_elements_by_class_name("loginButton")
        self.assertEquals(1, len(login_buttons), "There should be one login button")
        login_buttons[0].click()
        browser.find_elements_by_class_name("flash")

        # self.driver = WebDriver("chrome",
        #                         desired_capabilities={'browserName': 'chrome',
        #                                               'javascriptEnabled': True,
        #                                               'platform': 'ANY',
        #                                               'version': ''},
        #                         reuse_browser=True,
        #                         wait=30)
        # self.assertEqual(True, True)
        # self.driver.get("http://www.gettalent.com/web")


class NegativeLoginTests(unittest.TestCase):
    def setUp(self):
        print 'setup'
        self.browser = webdriver.Chrome()

    def tearDown(self):
        print 'tearing down'
        self.browser.quit()

    def test_invalid_username(self):
        print 'test_login'
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.cfg'))
        browsers = config.get("Default", "browsers").split(',')

        browser = self.browser
        browser.get("http://gettalent.com/web")
        email_input = browser.find_element_by_id("user_email")
        #email_input.send_keys("invalid_username@gmail.com")
        email_input.send_keys("nivedita.khoche@dice.com")
        password_input = browser.find_element_by_id("user_password")
        password_input.send_keys("password")
        login_buttons = browser.find_elements_by_class_name("loginButton")
        # self.assertEquals(1, len(login_buttons), "There should be one login button")
        login_buttons[0].click()
       #self.assertEquals( invalid Login)
        #alert_block = browser.find_elements_by_class_name("talent_flash")[0]
        #self.assertEquals(alert_block.text, 'Invalid login')


        # TODO assert that we get an Invalid Login

        # self.driver = WebDriver("chrome",
        #                         desired_capabilities={'browserName': 'chrome',
        #                                               'javascriptEnabled': True,
        #                                               'platform': 'ANY',
        #                                               'version': ''},
        #                         reuse_browser=True,
        #                         wait=30)
        # self.assertEqual(True, True)
        # self.driver.get("http://www.gettalent.com/web")



if __name__ == '__main__':
    unittest.main()
