import json
import os
from getpass import getpass

from constants import COOKIES_DIR
from constants import ASSIGNMENT_MAPPING_PATH, PROBLEM_MAPPING_PATH, STATEMENT_PATH, CONTEST_NAME
from util.common import get_csrf_token
from util.curl import curl
from util.colors import cyan_wrapper, green_wrapper

def update_map():
	if not os.path.isdir(STATEMENT_PATH):
		os.mkdir(STATEMENT_PATH)
	os.chmod(STATEMENT_PATH, 0700)
	endpoint = "problem?offset=0&limit=200"
	inputstr = '{'
	result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
	counter_1 = 1
	for i in range(0,len(result['data']['results'])):
		real_id = result['data']['results'][i]['id']
		display_id = result['data']['results'][i]['_id'].replace(" ","_")
		if counter_1 != 1:
			inputstr += ','
		inputstr += '"' + str(display_id) + '":{"_id":"' + str(real_id) + '"}'
		counter_1+=1
	inputstr += '}'
	f = open(PROBLEM_MAPPING_PATH,'w')
	f.write(inputstr.encode("utf-8"))
	f.close
	print(green_wrapper("Updated problems successfully!"))
	print("Target Contest: " + cyan_wrapper(CONTEST_NAME))
	endpoint = "contests?offset=0&limit=10&status=0"
	inputstr = '{'
	result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
	counter = 1
	for i in range(0,len(result['data']['results'])):
		if(result['data']['results'][i]['title'] != CONTEST_NAME):
			continue
		contestid = result['data']['results'][i]['id']
		payload = {
				"contest_id" : str(contestid)
				}
		endpoint = "contest/problem?contest_id=" + str(contestid)
		result2 = json.loads(curl("get", payload=payload, endpoint=endpoint, use_x_csrf_token=True))
		if result2["error"] == "error":
			print("Error : " + result2["data"])
			continue
		for problems in range(0,len(result2['data'])):
			name = result2['data'][problems]['title']
			c_id = result2['data'][problems]['_id']
			r_id =  result2['data'][problems]['id']
			print("Found HomeWork: " + cyan_wrapper(str(c_id) + " [" + name + "]"))
			if counter != 1:
				inputstr += ','
			inputstr += '"' + str(c_id) + '":{"contest_name":"' + str(name) + '","contest_id":' + str(contestid) + ',"contest_problem_id":"' + str(c_id)+ '","problem_id":' + str(r_id) + '}'
			counter += 1
	inputstr += '}'
	if not os.path.isdir(STATEMENT_PATH):
		os.mkdir(STATEMENT_PATH)
	f = open(ASSIGNMENT_MAPPING_PATH,'w')
	f.write(inputstr.encode("utf-8"))
	f.close
	print(green_wrapper("Updated assign successfully!"))
	
