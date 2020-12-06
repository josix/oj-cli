import json
from collections import defaultdict
from os import stat

from constants import HOST, MY_STATUS_PATH
from util.colors import cyan_wrapper, green_wrapper, purple_wrapper, red_wrapper, gray_wrapper
from util.curl import curl


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
	#print(response_data)
	if response_data == "Submission doesn't exist":
		print("Submission doesn't exist")
		return
	print("=================================================")
	status_to_response = {
			-1: red_wrapper("WA(Wrong Answer)"),  # WA
			-2: cyan_wrapper("CE(Compilation Error)"),  # CE
			0: green_wrapper("AC(Accept)"),  # AC
			2: "TLE(Time Limit Exceeded)",  # TLE
			3: "MLE(Memory Limit Exceeded)",  # MLE
			4: purple_wrapper("RE(Runtime Error)"),  # RE
			8: cyan_wrapper("PAC(Partial Accepted)")
			}
	this_result = response_data["result"]
	print("Result: {:33}  Score:{:4}\n".format(status_to_response[this_result],response_data["statistic_info"]["score"]))
	if "data" not in response_data["info"]:
		print(gray_wrapper(response_data["statistic_info"]["err_info"]))
		print("=================================================")
		return
	print("|ID |Status                |   Time|  Mem| Score|")
	for ans in result["data"]["info"]["data"]:
		print("|#{:2}|{:33}|{:5}ms|{:3}MB| {:5}|".format(ans["test_case"],status_to_response[ans["result"]], ans["real_time"], (ans["memory"]/1048576)+1, ans["score"]))
	dirname = response_data["username"] + "|" + response_data["id"] + ".c"
	with open(dirname, "wt") as fout:                                                                                                                  
		fout.write(response_data["code"])
	print("=================================================")
	print("Downloaded your file!!!\nFile name:{} in yor current directory.".format(dirname))
	#print(response_data["code"])
