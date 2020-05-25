# coding: utf-8

from login_page import LoginPage
from parent_portal_page import ParentPortalPage
import requests

def login(driver, username, password):
	login_page = LoginPage(driver)
	login_page.login(username, password)

def search(driver, params):
	parent_portal_page = ParentPortalPage(driver)
	parent_portal_page.search(params)
	
def sort(driver, by):
	parent_portal_page = ParentPortalPage(driver)
	parent_portal_page.sort(by)

def get_post_api(driver, post_id):
	res = requests.get("https://my-json-server.typicode.com/typicode/demo/posts/%s" % post_id)
	print(res.status_code)

