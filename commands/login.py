import json
import os
from getpass import getpass

from constants import COOKIES_DIR
from constants import COOKIES_PATH
from util.common import get_csrf_token
from util.curl import curl
from util.colors import green_wrapper

def login():
	username = raw_input("Username: ")
	passwd = getpass("Password: ")
	payload = {
		"username": username,
		"password": passwd,
	}
	result = curl("post", payload=payload, endpoint="login/", use_x_csrf_token=True)
	#print(result)
	result = json.loads(result)
	print("%s!!" % result["data"])
	os.chmod(COOKIES_PATH, 0700)

def fetch_csrf_token():
	if not os.path.isdir(COOKIES_DIR):
		os.mkdir(COOKIES_DIR)
	if os.path.isfile(COOKIES_PATH):
		os.remove(COOKIES_PATH)
	curl("get", endpoint="profile/")

def auth():
	fetch_csrf_token()
	login()
