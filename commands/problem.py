import json
import time

from constants import PROBLEM_MAPPING_PATH
from util.curl import curl
from .status import status
from util.colors import cyan_wrapper, green_wrapper

def problem_submit(problem_id, language, filename): 
    with open(PROBLEM_MAPPING_PATH, "rt") as json_in:
        problem_to_config = json.load(json_in)
        if problem_id not in problem_to_config:
            print(cyan_wrapper("Invalid problem id!") + " Please confirm your input.")
            return
    try:
        with open(filename, "r") as fin:
            code = fin.read()
    except IOError:
        print('File "' + filename + '" does not exist!')
        return
    if language != "C" and language != "C++" and language != "Python3" and language != "Python2" and language != "Golang" and language != "Java":
        print("Please select a language type form " + cyan_wrapper("C, C++, Python2, Python3, Golang, Java."))
        return
    payload = {
        "problem_id": problem_to_config[problem_id]["_id"],
        "language": language,
        "code": code,
    }
    endpoint = "submission"

    try:
        submission_response = json.loads(
            curl("POST", payload=payload, endpoint=endpoint, use_x_csrf_token=True)
        )
    except ValueError:
        print("No response is received! Please contact class TA!")
    if submission_response["error"] == "error":
        print(submission_response["data"])
        return
    submission_id = submission_response["data"]["submission_id"]
    print(green_wrapper("Submit successfully!!"))
    print("Getting submission status...".format(submission_id))
    time.sleep(1.0)
    status(submission_id)
