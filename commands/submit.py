import json
import time

from constants import ASSIGNMENT_MAPPING_PATH
from util.curl import curl

from .status import status


def submit(assign_number, filename):
    with open(ASSIGNMENT_MAPPING_PATH, "rt") as json_in:
        assign_to_config = json.load(json_in)
    if assign_number not in assign_to_config:
		print("Invalid Assign Number!")
		print("Available names are")
		for hwmap in assign_to_config:
			print("- " + hwmap)
		print("\nIf you want to update latest homework assignment, type: [oj update] to update.")
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
        "language": "C",
        "code": code,
        "contest_id": contest_id,
    }
    endpoint = "submission"

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
        print("Unknown error occuried!")
        return
    print(
        "Submit successfully!\n"
        "Your submission Id is {}\n"
        "Getting submission status...".format(submission_id)
    )
    time.sleep(0.6)
    status(submission_id)
