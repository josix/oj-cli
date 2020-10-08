from os.path import dirname, expanduser, realpath

HOST = "<URL>"
API_HOST = HOST + "api"

CONTENT_TYPE_OPTION = " -H 'Content-Type: application/json' "

home = expanduser("~")
COOKIES_DIR = home + "/.cookies/"
COOKIES_NAME = "oj_cookies"
COOKIES_PATH = COOKIES_DIR + COOKIES_NAME

ASSIGNMENT_MAPPING_PATH = dirname(realpath(__file__)) + "/assign_mapping.json"

TEMPLATE_FILENAME = {
    "C": "main.c",
    "C++": "main.cpp",
    "Java": "main.java",
    "Python2": "mainpy2.py",
    "Python3": "mainpy3.py",
    "Golang": "main.go",
}
