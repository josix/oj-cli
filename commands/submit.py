import json
import os

from util.curl import curl

from constants import ASSIGNMENT_MAPPING_PATH


def submit(assign_number):
    with open(ASSIGNMENT_MAPPING_PATH, "rt") as jsoin_in:
        assign_to_config = json.load(jsoin_in)
    if assign_number not in assign_to_config:
        print("Invalid Assign Number!")
        return
    contest_id, problem_id = (
        assign_to_config[assign_number]["contest_id"],
        assign_to_config[assign_number]["contest_problem_id"],
    )
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