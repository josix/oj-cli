import json
from collections import defaultdict
from os import stat

from constants import HOST
from util.colors import cyan_wrapper, green_wrapper, purple_wrapper, red_wrapper, gray_wrapper
from util.curl import curl


def status(submission_id):
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
	print("=================================================")
