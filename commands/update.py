import json
import os
from getpass import getpass

from constants import COOKIES_DIR
from constants import ASSIGNMENT_MAPPING_PATH
from util.common import get_csrf_token
from util.curl import curl
from util.colors import cyan_wrapper

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
