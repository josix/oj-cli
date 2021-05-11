from constants import COOKIES_PATH


def get_csrf_token():
    csrf_token = None
    with open(COOKIES_PATH) as fin:
        for line in fin:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue
            line = line.strip().split("\t")
            if line[-2] == "csrftoken":
                csrf_token = line[-1]
                return csrf_token
