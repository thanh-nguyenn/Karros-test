# coding: utf-8
from selenium.webdriver import Chrome, Firefox
from common_lib import *
import unittest

class Parent_Portal_Test(unittest.TestCase):
	#@classmethod
	def setUp(self):
		self.driver = Firefox()
		self.driver.get("http://ktvn-test.s3-website.us-east-1.amazonaws.com/")
		self.driver.maximize_window()

	# @classmethod
	def tearDown(self):
		self.driver.close()
	
	def test_get_api_post(self):
		post_id = 1
		get_post_api(self.driver, post_id)
	
	def test_filter_and_sort_INACTIVE_requests(self):
		username = "admin@test.com"
		password = "test123"
		login(self.driver, username, password)
		search(self.driver, {'request_status':'Inactive'})
		sort(self.driver, 'First Name')
		
if __name__ == "__main__":
	unittest.main()