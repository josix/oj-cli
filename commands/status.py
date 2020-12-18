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
	if "info" in response_data:
		if response_data == "Submission doesn't exist":
			print("Submission doesn't exist")
			return
		print("========================================================")
		status_to_response = {
				-1: red_wrapper("WA(Wrong Answer)"),  # WA
				-2: cyan_wrapper("CE(Compilation Error)"),  # CE
				0: green_wrapper("AC(Accept)"),  # AC
				1: purple_wrapper("TLE(TimeLimitExceeded)"),  # TLE
				3: purple_wrapper("MLE(MemoryLimitExceeded)"),  # MLE
				4: purple_wrapper("RE(Runtime Error)"),  # RE
				8: cyan_wrapper("PAC(Partial Accepted)")
				}
		this_result = response_data["result"]
		try:
			print("Result: {:40}  Score:{:4}".format(status_to_response[this_result],response_data["statistic_info"]["score"]))
			if "data" not in response_data["info"]:
				print(gray_wrapper(response_data["statistic_info"]["err_info"]))
				print("========================================================")
				return
			print("|ID |Status                       |   Time|  Mem| Score|")
			for ans in result["data"]["info"]["data"]:
				print("|#{:2}|{:40}|{:5}ms|{:3}MB| {:5}|".format(ans["test_case"],status_to_response[ans["result"]], ans["real_time"], (ans["memory"]/1048576)+1, ans["score"]))
			print("========================================================")
		except:
			print(result)
			print("Bad response! Please check your internet connection and ask TAs!")
	else:
		if response_data == "Submission doesn't exist":
			print("Submission doesn't exist")
			return
		print("==============================================")
		status_to_response = {
				-1: red_wrapper("WA(Wrong Answer)"),  # WA
				-2: cyan_wrapper("CE(Compilation Error)"),  # CE
				0: green_wrapper("AC(Accept)"),  # AC
				1: purple_wrapper("TLE(TimeLimitExceeded)"),  # TLE
				3: purple_wrapper("MLE(MemoryLimitExceeded)"),  # MLE
				4: purple_wrapper("RE(Runtime Error)"),  # RE
				8: cyan_wrapper("PAC(Partial Accepted)")
				}
		this_result = response_data["result"]
		try:
			print("Result: {:40}".format(status_to_response[this_result]))
			if "err_info" in response_data["statistic_info"]:
				print(gray_wrapper(response_data["statistic_info"]["err_info"]))
				print("==============================================")
				return
			print("|Status                       |   Time|  Mem|")
			print("|{:40}|{:5}ms|{:3}MB|".format(status_to_response[this_result], response_data["statistic_info"]["time_cost"], (response_data["statistic_info"]["memory_cost"]/1048576)+1))
			print("==============================================")
		except:
			print(result)
			print("Bad response! Please check your internet connection and ask TAs!")

	
