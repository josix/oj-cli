import json
import os

from constants import TEMPLATE_FILENAME, PROBLEM_MAPPING_PATH
from util.curl import curl
from util.colors import cyan_wrapper


def get_problem(problem_id):
    with open(PROBLEM_MAPPING_PATH, "rt") as json_in:
        problem_to_config = json.load(json_in)
    if problem_id not in problem_to_config:
        print(cyan_wrapper("Invalid problem id!") + " Please confirm your input.")
        return
    pid = problem_to_config[problem_id]["query_id"]
    endpoint = "problem?problem_id={}".format(pid)
    result = json.loads(curl("get", endpoint=endpoint, use_x_csrf_token=True))
    data = result["data"]
    if not data:
        print("Unexpected Error with Server")
        return
    try:
        samples = data["samples"]
        templates = data["template"]
        languages = data["languages"]
    except:
        print("Unexpected Error in Parsing Response:")
        print(data)
        return
    dir_name = "problem_{}".format(problem_id)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        print("Made a [{}] folder in your current directory.".format(dir_name))
    for language in languages:
        if language not in templates:
            continue
        template_file = dir_name + "/{}".format(TEMPLATE_FILENAME[language])
        content = templates[language]
        with open(template_file, "wt") as fout:
            try:
                fout.write(content)
            except:
                print("None-ascii character in template")
            # TODO: Update to support utf-8 encoding.
    for idx, sample in enumerate(samples):
        sample_num = idx + 1
        input_sample_path = dir_name + "/" + "{}.in".format(sample_num)
        input_ = sample["input"]
        with open(input_sample_path, "wt") as fout:
            try:
                fout.write(input_)
            except:
                print("None-ascii character in input file")
            # TODO: Update to support utf-8 encoding.
        output_sample_path = dir_name + "/" + "{}.out".format(sample_num)
        output = sample["output"]
        with open(output_sample_path, "wt") as fout:
            try:
                fout.write(output)
            except:
                print("None-ascii character in ouput file")
            # TODO: Update to support utf-8 encoding.
