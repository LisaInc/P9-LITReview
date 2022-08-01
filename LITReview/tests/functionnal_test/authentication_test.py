from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class TestAuthentification(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox("tests/functionnal_test")
        self.browser.get(self.live_server_url + reverse("signup"))

        fname = self.browser.find_element_by_id("fname")
        fname.send_keys("Ranga")
        lname = self.browser.find_element_by_id("lname")
        lname.send_keys("Gonnage")
        username = self.browser.find_element_by_id("username")
        username.send_keys("rgonnage")
        email = self.browser.find_element_by_id("email")
        email.send_keys("test@test.com")
        password1 = self.browser.find_element_by_id("pass")
        password1.send_keys("ranga12345")
        password2 = self.browser.find_element_by_id("re_pass")
        password2.send_keys("ranga12345")
        agree_term = self.browser.find_element_by_id("agree-term")
        agree_term.click()
        signup = self.browser.find_element_by_id("signup")
        signup.click()

    def tearDown(self):
        self.browser.close()
