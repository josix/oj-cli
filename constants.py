from os.path import expanduser, dirname, realpath

HOST = "https://oj.mozix.ebg.tw/"
API_HOST = HOST + "api"

CONTENT_TYPE_OPTION = " -H 'Content-Type: application/json' "

home = expanduser("~")
COOKIES_DIR = home + "/.cookies/"
COOKIES_NAME = "oj_cookies"
COOKIES_PATH = COOKIES_DIR + COOKIES_NAME

ASSIGNMENT_MAPPING_PATH = dirname(realpath(__file__)) + "/assign_mapping.json"
