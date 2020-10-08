import json
from collections import defaultdict
from os import stat

from constants import HOST
from util.colors import cyan_wrapper, green_wrapper, purple_wrapper, red_wrapper
from util.curl import curl


def status(submission_id):
    endpoint = "submission?id={}".format(submission_id)
    result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
    response_data = result["data"]
    if response_data == "Submission doesn't exist":
        print("Submission doesn't exist")
        return
    print("Your code has been graded! Here's your results:\n")
    status_to_response = {
        -1: lambda idx: red_wrapper("Testcase {}: WA(Wrong Answer)".format(idx)),  # WA
        -2: lambda idx: cyan_wrapper(
            "Testcase {}: CE(Compilation Error)".format(idx)
        ),  # CE
        0: lambda idx: green_wrapper("Testcase {}: AC(Accept)".format(idx)),  # AC
        2: lambda idx: "Testcase {}: TLE(Time Limit Exceeded)".format(idx),  # TLE
        3: lambda idx: "Testcase {}: MLE(Memory Limit Exceeded)".format(idx),  # MLE
        4: lambda idx: purple_wrapper(
            "Testcase {}: RE(Runtime Error)".format(idx)
        ),  # RE
    }
    if "data" not in response_data["info"]:
        print(cyan_wrapper("CE(Compilation Error) before running testing"))
        return
    for idx, ans in enumerate(response_data["info"]["data"]):
        test_case_no = idx + 1
        answers_status = ans["result"]
        if answers_status not in status_to_response:
            print("Testcase {}: SE(System Error)".format(test_case_no))
            continue
        print(status_to_response[answers_status](test_case_no))
    print("For graphical results,\nplease visit: " + HOST + "status/" + submission_id)
