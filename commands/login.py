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
        "csrfmiddlewaretoken": get_csrf_token(),
    }
    result = curl("post", payload=payload, endpoint="login/", use_x_csrf_token=True)
    result = json.loads(result)
    print("%s!!" % result["data"])
    os.chmod(COOKIES_PATH, 0700)

def fetch_csrf_token():
    if not os.path.isdir(COOKIES_DIR):
        os.mkdir(COOKIES_DIR)
    curl("get", endpoint="profile/")


def auth():
    fetch_csrf_token()
    login()
