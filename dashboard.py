__author__ = 'niveditakhoche'

import unittest
from selenium import webdriver
import ConfigParser
import login


class DashboardTestCase(login.LoginTestCase):

    def setUp(self):
        super(DashboardTestCase, self).setUp()
        print 'done setting up subclass'

    def tearDown(self):
        super(DashboardTestCase, self).tearDown()
        print 'tearing down the subclass'

    def dashboard_candidate_count(self):
        print 'running test_dashboard'
        browser = self.browser

        # TODO add some dashboard test stuff here

    def dashboard_graph(self):
        print 'running test_dashboard'
        browser = self.browser

        # TODO add some dashboard test stuff here


if __name__ == '__main__':
    unittest.main()
