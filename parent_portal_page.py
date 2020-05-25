# coding: utf-8
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

class ParentPortalPage(object):
	def __init__(self, driver):
		self.driver = driver

	def get_filter_button(self):
		return self.driver.find_element_by_xpath("//button[@class='btn btn-filter module_grid__btn_filter btn btn-default']")
		
	def get_request_status_dropdown(self):
		return self.driver.find_element_by_xpath("//select[@id='formControlsSelect']")

	def get_apply_filter_button(self):
		return self.driver.find_element_by_xpath("//button[@class='btn-filter btn btn-default']")

	def get_first_name_column(self):
		return self.driver.find_element_by_xpath("//th[contains(text(),'First Name')]")

	def search(self, params):
		self.get_filter_button().click()
		select_status = Select(self.get_request_status_dropdown())
		select_status.select_by_visible_text(params['request_status'])
		self.get_request_status_dropdown().send_keys(Keys.ENTER)
		self.get_apply_filter_button().click()
		

	def sort(self, by):
		if by == 'First Name':
			self.get_first_name_column().click()