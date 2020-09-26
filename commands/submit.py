import json
import os
import time

from util.curl import curl

from constants import ASSIGNMENT_MAPPING_PATH, HOST


def submit(assign_number, filename):
	with open(ASSIGNMENT_MAPPING_PATH, "rt") as jsoin_in:
		assign_to_config = json.load(jsoin_in)
	if assign_number not in assign_to_config:
		print("Invalid Assign Number!")
		return
	contest_id, problem_id, contest_problem_id = (
		assign_to_config[assign_number]["contest_id"],
		assign_to_config[assign_number]["problem_id"],
		assign_to_config[assign_number]["contest_problem_id"],
	)
	try:
		codefile = open(filename, "r")
		code = codefile.read()
	except IOError:
		print("file \"" + filename + "\" does not exist!")
		return
	payload = {
		"problem_id": problem_id,
		"language": "C",
		"code": code,
		"contest_id": contest_id
	}
	endpoint = "submission"

#--------------------------------------------------------------------------

	try:
		submission_response = json.loads(curl("POST", payload=payload, endpoint=endpoint, use_x_csrf_token=True))
	except ValueError:
		print("No response is received! Please contact class TA!")

	try:
		submission_id = submission_response["data"]["submission_id"]
	except TypeError:
		if(submission_response["data"] == "The contest have ended"):
			print("The contest have ended.")
			return
		else:
			print("Unknown error received!")
			return
	print("submit successful! Grading...")

	endpoint = "submission?id={}".format(submission_id)
	while(True):
		result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
		try:
			total_score = result["data"]["statistic_info"]["score"]
		except KeyError:
			time.sleep(1)
			continue
		try:
			print("Your code has been graded! Here's your results:")
			Index = 0
			for answers in result["data"]["info"]["data"]:
				Index += 1
				answers_status = answers["result"]
				if (answers_status == 4):
					print("\033[0;35mTestcase " + str(Index) + " : RE(Runtime Error)\033[0m")
				elif(answers_status == 3):
					print("\033[0mTestcase " + str(Index) + " : MLE(Memory Limit Exceeded)\033[0m")
				elif(answers_status == 1):
					print("\033[0mTestcase " + str(Index) + " : TLE(Time Limit Exceeded)\033[0m")
				elif(answers_status == 0):
					print("\033[0;32mTestcase " + str(Index) + " : AC(Accept)\033[0m")
				elif(answers_status == -1):
					print("\033[0;31mTestcase " + str(Index) + " : WA(Wrong Answer)\033[0m")
				else:
					print("\033[0mTestcase " + str(Index) + " : SE(System Error)\033[0m")
			break
		except KeyError:
			if(result["data"]["result"] == -2):
				print("\033[0;36mResults : CE(Compilation Error)\033[0m")
			else:
				print("\033[0mTestcase : SE(System Error)\033[0m")
			break
	print("Your total score: " + str(total_score))
	print("For graphical results, please visit: " + HOST + "status/" + submission_id)
					
# -2 : CE
# -1 : WA
# 0 : AC
# 1 : TLE
# 2 :
# 3 : MLE
# 4 : RE

#--------------------------------------------------------------------------
	#print(submission_id)
	'''
    with open(ASSIGNMENT_MAPPING_PATH, "rt") as jsoin_in:
        assign_to_config = json.load(jsoin_in)
    if assign_number not in assign_to_config:
        print("Invalid Assign Number!")
        return
    contest_id, problem_id = (
        assign_to_config[assign_number]["contest_id"],
        assign_to_config[assign_number]["contest_problem_id"],
    )
	// start here.
    endpoint = "contest/problem?contest_id={}&problem_id={}".format(
        contest_id, problem_id
    )
    result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
    data = result["data"][0]
    if not data:
        print("Unexpected Error with Server")
        return
    try:
        samples = data["samples"]
        template = data["template"]["C"]
    except:
        print("Unexpected Error in Parsing Response")
        return
    dir_name = "assign{}".format(assign_number)
    template_path = dir_name + "/" + "hw{}.c".format(assign_number)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with open(template_path, "wt") as fout:
        fout.write(template)
    for idx, sample in enumerate(samples):
        sample_num = idx + 1
        input_sample_path = dir_name + "/" + "{}.in".format(sample_num)
        input_ = sample["input"]
        with open(input_sample_path, "wt") as fout:
            fout.write(input_)
        output_sample_path = dir_name + "/" + "{}.out".format(sample_num)
        output = sample["output"]
        with open(output_sample_path, "wt") as fout:
            fout.write(output)
	'''
