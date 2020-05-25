# coding: utf-8
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage(object):
	def __init__(self, driver):
		self.driver = driver

	def get_textbox_email(self):
		return self.driver.find_element_by_xpath("//input[@id='formHorizontalEmail']")
		
	def get_textbox_password(self):
		return self.driver.find_element_by_xpath("//input[@id='formHorizontalPassword']")

	def get_btn_login(self):
		return self.driver.find_element_by_xpath("//a[@class='col-login__btn']")

	def get_header_label(self):
		return self.driver.find_element_by_xpath("//a[@class='navbar-brand']")

	def login(self, username, password):
		self.get_textbox_email().send_keys(username)
		self.get_textbox_password().send_keys(password)
		self.get_btn_login().click()
		sleep(3)


