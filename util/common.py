from constants import COOKIES_PATH
from util.colors import red_wrapper

def get_csrf_token():
    csrf_token = None
    try:
        with open(COOKIES_PATH) as fin:
            for line in fin:
                line = line.strip()
                if line == "" or line[0] == "#":
                    continue
                line = line.strip().split("\t")
                if line[-2] == "csrftoken":
                    csrf_token = line[-1]
                    return csrf_token
    except:
        print(red_wrapper("cookie file not found or parsing error"))
