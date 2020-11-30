import json
import os
from datetime import datetime

from constants import ASSIGNMENT_MAPPING_PATH
from constants import COOKIES_DIR
from util.common import get_csrf_token
from util.curl import curl
from util.colors import cyan_wrapper, green_wrapper, purple_wrapper, red_wrapper

def contests(option, assign_name):
	if option == 'status' or option == 's':
		contests_status(assign_name)
	elif option == 'rank' or option == 'r':
		contests_result(assign_name)
	elif option == 'update' or option == 'u':
		update_map()

def contests_status(assign_name):
	with open(ASSIGNMENT_MAPPING_PATH, "rt") as json_in:
		assign_to_config = json.load(json_in)
	if assign_name not in assign_to_config:
		print("Invalid Assign Number!")
		print("Available name now is:")
		for hwmap in assign_to_config:
			print("- " + hwmap)
		print("\nIf you want to update latest homework assignment, type: [oj update] to update.")
		return
	contest_id, problem_id = (
        assign_to_config[assign_name]["contest_id"],
        assign_to_config[assign_name]["contest_problem_id"],
    )
	endpoint = "contest_submissions?myself=0&contest_id={}&limit=20".format(
        contest_id
    )
	result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
	result = result["data"]["results"]
	
	status_to_response = {
			-1: red_wrapper("WA(Wrong Answer)"),  # WA
			-2: cyan_wrapper("CE(Compilation Error)"),  # CE
			0: green_wrapper("AC(Accept)"),  # AC
			2: "TLE(Time Limit Exceeded)",  # TLE
			3: "MLE(Memory Limit Exceeded)",  # ML 
			4: purple_wrapper("RE(Runtime Error)"),  # RE
			8: cyan_wrapper("PAC(Partial Accepted)")
			}
	print('|{:12}|{:22}|{:7}|{:5}|{}'.format("User","Status","Time","Mem","When"))
	for i in result:
		timestr = i["create_time"].split("T")[0]
		timestr += " " + i["create_time"].split("T")[1].split(".")[0]
		if i["result"] != -2:
			print('|{:12}|{:33}|{:5}ms|{:3}MB|{}|'.format(i["username"], status_to_response[i["result"]], i["statistic_info"]["time_cost"], (i["statistic_info"]["memory_cost"]/1048576)+1, timestr))
		else:
			print('|{:12}|{:33}|{:5}--|{:3}--|{}|'.format(i["username"], status_to_response[i["result"]], "-----", "---", timestr))




def contests_result(assign_name):
	with open(ASSIGNMENT_MAPPING_PATH, "rt") as json_in:
		assign_to_config = json.load(json_in)
	if assign_name not in assign_to_config:
		print("Invalid Assign Number!")
		print("Available name now is:")
		for hwmap in assign_to_config:
			print("- " + hwmap)
		print("\nIf you want to update latest homework assignment, type: [oj update] to update.")
		return

	contest_id, problem_id = (
        assign_to_config[assign_name]["contest_id"],
        assign_to_config[assign_name]["contest_problem_id"],
    )
	endpoint = "contest_rank?myself=0&contest_id={}&limit=100".format(
        contest_id
    )
	result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
	result = result["data"]["results"]
	print('|{:12}|{:10}|{:5}|'.format("User","Graph","Score"))
	for usr in result:
		blocks = usr["total_score"]/10
		blockstr = ''
		for i in range(blocks):
			blockstr += '*'
		for i in range(blocks,10):
			blockstr += ' '
		print('|{:12}|{:10}|{:5}|'.format(usr["user"]["username"], green_wrapper(blockstr), usr["total_score"]))


def update_map():
	endpoint = "contests?offsets=0&limit=100&status=0"
	payload = {
			"offsets":0,
			"limit":100,
			"status":0
			}
	inputstr = '{'
	result = json.loads(curl("get", payload=payload, endpoint=endpoint, use_x_csrf_token=True))
	for i in range(0,len(result['data']['results'])):
		contestid = result['data']['results'][i]['id']
		payload = {
				"contest_id" : str(contestid)
				}
		endpoint = "contest/problem?contest_id=" + str(contestid)
		result2 = json.loads(curl("get", payload=payload, endpoint=endpoint, use_x_csrf_token=True))
		q_string = result2["data"][0]["_id"]
		_pid = q_string.split()[0] + "+" + q_string.split()[1]
		print("Found HomeWork: " + cyan_wrapper(q_string.split()[1]))
		if i != 0:
			inputstr += ','
		inputstr += '"' + str(q_string.split()[1])+'":{"contest_id":' + str(contestid) + ',"contest_problem_id":"' + str(_pid)+ '","problem_id":' + str(result2["data"][0]["id"]) + '}'
	inputstr += '}'
	f = open(ASSIGNMENT_MAPPING_PATH,'w')
	f.write(inputstr)
	f.close
	print("\nUpdated successfully!\n")
