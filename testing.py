from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

__author__ = 'niveditakhoche'

import unittest
from selenium import webdriver
import ConfigParser
import login


class DashboardTestCase(login.LoginTestCase):
    # def setUp(self):
    # super(DashboardTestCase, self).setUp()
    # print 'Logging in now'
    # config = ConfigParser.ConfigParser()
    # config.readfp(open('config.cfg'))
    # browsers = config.get("Default", "browsers").split(',')

    # browser = self.browser
    # browser.get("http://gettalent.com/web")
    # email_input = browser.find_element_by_id("user_email")
    # email_input.send_keys("nivedita.khoche@gmail.com")
    # password_input = browser.find_element_by_id("user_password")
    # password_input.send_keys("password")
    # login_buttons = browser.find_elements_by_class_name("loginButton")
    # # self.assertEquals(1, len(login_buttons), "There should be one login button")
    # login_buttons[0].click()

    # def tearDown(self):
    # super(DashboardTestCase, self).tearDown()
    # print 'tearing down the subclass'

    def test_enter_candidate(self):
        browser = self.browser

        browser.find_element_by_xpath("//div/div/ul[1]/li[2]/a").click()
        # browser.find_element_by_link_text("Talent").click()
        print 'got Talent'
        browser.find_element_by_link_text("Import").click()
        print 'got import'
        browser.find_element_by_xpath(".//*[@id='tab-createJob']/div/img").click()
        print 'got QuickAdd'
        #Todo =WebDriverWait(browser,30).until(find_element_by_xpath("//*[@id='quick-add-candidate-modal']"))
        wait = WebDriverWait(browser, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='requiredInput']")))
        #element.click()
        browser.find_element_by_xpath("//input[@name='firstName']").send_keys("Ahmed051")
        browser.find_element_by_xpath("//input[@name='lastName']").send_keys("Boy01")
        browser.find_element_by_xpath("//input[@name='emailAdd']").send_keys("aB01@gmail.com")
        browser.find_element_by_xpath("//input[@name='phoneNum']").send_keys("408-5178943")
        browser.find_element_by_xpath("//input[@name='currTitle']").send_keys("")
        select = Select(browser.find_element_by_id("gettalent_interest"))
        select.select_by_visible_text("Design")
        #browser.find_element_by_id("gettalent_interest").click()
        #browser.find_element_by_xpath("//select/option[@value='Design']").click()
        browser.find_element_by_id("btn-submit").click()
        browser.find_element_by_xpath("//div/div/ul[1]/li[2]/a").click()
        browser.find_element_by_link_text("Search").click()
        #.//*[@id='search_form']/div[1]/ul/li[2]/div[1]/div[2]/ul/li[2]/input
        #selectOption = browser.find_elements_by_class_name("facet usernameFacet")
        #selectOption.select_by_visible_text("nivedita.khoche@dice.com")
        browser.find_element_by_xpath("//*[@id='search_form']/div[1]/ul/li[2]/div[1]/div[1]/i").click()
        print 'clicked on Owner'
        #browser.find_element_by_xpath(".//*[@id='search_form']/div[1]/ul/li[2]/div[1]/div[2]/ul/li[2]/input").click()

        browser.find_element_by_xpath("(//input[@name='usernameFacet'])[2]").click()
        # browser.find_element_by_xpath("//*[@class='facet' and @value='nivedita.khoche@dice.com']").click()

        #[@value='nivedita.khoche@dice.com']").doubleClick()
        print 'verifying newly entered candidate.'
        import utilities
        utilities.verify_candidates_exist()
        #browser.find_element_by_
        #xpath("//input[@class='facet'']").click()

        # Alert(browser).accept()

        # browser.find_element_by_class_name("firepath-matching-node").click()
        # browser.find_element_by_class_name("gettalent import").click()

        # TODO add some dashboard test stuff here

    def test_verify_enteredCandidate(self):
        #browser = self.browser
        #browser.find_element_by_xpath("//div/div/ul[1]/li[2]/a").click()
        #browser.find_element_by_link_text("Search")
        #.//*[@id='search_form']/div[1]/ul/li[2]/div[1]/div[2]/ul/li[2]/input
        #selectOption = browser.find_elements_by_class_name("facet usernameFacet")
        #selectOption.select_by_visible_text("nivedita.khoche@dice.com")

        #browser.find_element_by_xpath("//*[@class='facet' and @value='nivedita.khoche@dice.com']").click()
        print 'verifying newly entered candidate.'

    def dashboard_graph(self):
        print 'running test_dashboard'
        #browser = self.browser
        #browser.quit()

        # TODO add some dashboard test stuff here


if __name__ == '__main__':
    unittest.main()
