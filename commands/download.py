import json
from collections import defaultdict
from os import stat

from constants import HOST, MY_STATUS_PATH
from util.colors import cyan_wrapper, green_wrapper, purple_wrapper, red_wrapper, gray_wrapper
from util.curl import curl
from .status import status


def dl(assign_name):
	submission_id = ''
	with open(MY_STATUS_PATH, "rt") as json_in:
		status_config = json.load(json_in)
		if assign_name in status_config:
			submission_id = status_config[assign_name]["id"]
		else:
			print("Invalid ID! Please use[oj mystat <assign_no>] to get ID")
			return
	endpoint = "submission?id={}".format(submission_id)
	result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
	response_data = result["data"]
	status(submission_id)
	dirname = response_data["username"] + "|" + response_data["id"] + ".c"
	with open(dirname, "wt") as fout:                                                                                                                  
		fout.write(response_data["code"])
	print("Downloaded your file!!!\nFile name:{} in yor current directory.".format(dirname))
	#print(response_data["code"])
