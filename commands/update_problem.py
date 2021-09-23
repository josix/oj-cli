import json
import os

from constants import PROBLEM_MAPPING_PATH, STATEMENT_PATH, CONTEST_NAME
from util.curl import curl
from util.colors import green_wrapper

def update_problem_map():
	if not os.path.isdir(STATEMENT_PATH):
		os.mkdir(STATEMENT_PATH)
	os.chmod(STATEMENT_PATH, 0700)
	endpoint = "problem?offset=0&limit=200"
	inputstr = '{'
	result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
	counter_1 = 1
	for i in range(0,len(result['data']['results'])):
		real_id = result['data']['results'][i]['id']
		display_id = result['data']['results'][i]['_id'].replace(" ","")
		if counter_1 != 1:
			inputstr += ','
		inputstr += '"' + str(display_id) + '":{"_id":"' + str(real_id) + '","query_id":"' + result['data']['results'][i]['_id'].replace(" ","+") + '"}'
		counter_1+=1
	inputstr += '}'
	f = open(PROBLEM_MAPPING_PATH,'w')
	f.write(inputstr.encode("utf-8"))
	f.close
	print(green_wrapper("Updated problems successfully!"))
	
