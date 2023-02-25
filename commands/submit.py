import json
import time

from constants import ASSIGNMENT_MAPPING_PATH
from util.curl import curl
from .status import status
from util.colors import cyan_wrapper

def submit(assign_number, filename):
    with open(ASSIGNMENT_MAPPING_PATH, "rt") as json_in:
        assign_to_config = json.load(json_in)
    if assign_number not in assign_to_config:
        print("Invalid Assign Number!")
        print("Available names are:")
        for hwmap in assign_to_config:
            print("- " + cyan_wrapper(hwmap + " [" + assign_to_config[hwmap]['contest_name'] + "]"))
        print("If you want to update latest homework assignment, type: [oj update] to update.")
        return
    contest_id, problem_id = (
        assign_to_config[assign_number]["contest_id"],
        assign_to_config[assign_number]["problem_id"],
    )
    try:
        with open(filename, "r") as fin:
            code = fin.read()
    except IOError:
        print('File "' + filename + '" does not exist!')
        return
    payload = {
        "problem_id": problem_id,
        "code": code,
        "contest_id": contest_id,
    }
    endpoint = "submission"
    type = filename.split(".")[-1]
    if type == "c":
        payload["language"] = "C"
    elif type == "cpp":
        payload["language"] = "C++"
    else:
        print("Wrong file format.")
        return

    try:
        submission_response = json.loads(
            curl("POST", payload=payload, endpoint=endpoint, use_x_csrf_token=True)
        )
    except ValueError:
        print("No response is received! Please contact class TA!")

    response_data = submission_response["data"]
    if response_data == "The contest have ended":
        print("The contest has ended.")
        return
    try:
        submission_id = response_data["submission_id"]
    except TypeError:
        if submission_response["error"] == "invalid-code":
            print("You can't submit empty file.'")
            return
        print("Error occuried!")
        print(submission_response["data"])
        return
    print(
        "Submit successfully!\n"
        "Getting submission status...".format(submission_id)
    )
    time.sleep(1.0)
    status(submission_id)