import json
import os

from constants import ASSIGNMENT_MAPPING_PATH, STATEMENT_PATH, CONTEST_NAME
from util.curl import curl
from util.colors import cyan_wrapper, green_wrapper

def update_contest_map():
	if not os.path.isdir(STATEMENT_PATH):
		os.mkdir(STATEMENT_PATH)
	os.chmod(STATEMENT_PATH, 0700)
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
			c_id = result2['data'][problems]['_id']
			name = result2['data'][problems]['title']
			r_id =  result2['data'][problems]['id']
			try:
				print("Found HomeWork: " + cyan_wrapper(str(c_id) + " [" + name + "]"))
			except:
				print("Found HomeWork: " + cyan_wrapper(str(c_id) + " [" + str(c_id) + "]"))
			if counter != 1:
				inputstr += ','
			try:
				inputstr += '"' + str(c_id) + '":{"contest_name":"' + str(name) + '","contest_id":' + str(contestid) + ',"contest_problem_id":"' + str(c_id)+ '","problem_id":' + str(r_id) + '}'
			except:
				inputstr += '"' + str(c_id) + '":{"contest_name":"' + str(c_id) + '","contest_id":' + str(contestid) + ',"contest_problem_id":"' + str(c_id)+ '","problem_id":' + str(r_id) + '}'
			counter += 1
	inputstr += '}'
	if not os.path.isdir(STATEMENT_PATH):
		os.mkdir(STATEMENT_PATH)
	f = open(ASSIGNMENT_MAPPING_PATH,'w')
	f.write(inputstr.encode("utf-8"))
	f.close
	print(green_wrapper("Updated assign successfully!"))
	
