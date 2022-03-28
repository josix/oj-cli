import json
import csv
import os
from util.curl import curl

GRADE_CSV = "./Grade.csv"

def write_csv(data = None):
    with open(GRADE_CSV, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def get_grades(contest):
    # fetch contest ID
    print("[info] fetch contest ID...")
    endpoint = "contests?offset=0&limit=20&keyword=&rule_type=&status="	
    result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
    contestID = None
    for r in result["data"]["results"]:
        if contest in r["title"]:
            contestID = r["id"]
    if contestID == None:
        print("Invalid contest name")
        return

    # fetch all users
    print("[info] fetch all users...")
    allUsers = []
    current, total = 0, 1
    while current < total:
        endpoint = "contest_rank?offset={}&limit=50&contest_id={}".format(current, contestID)
        result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
        for r in result["data"]["results"]:
            try:
                allUsers.append(str(r["user"]["username"]))
            except:
                allUsers.append(str(r["user"]["id"]))
        current, total = current + 50, result["data"]["total"]
    # fetch all hw
    print("[info] fetch all hw...")
    allHW = []
    current, total = 0, 1
    while current < total:
        endpoint = "admin/contest/problem?keyword&offset={}&limit=50&contest_id={}".format(current, contestID)
        result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
        for r in result["data"]["results"]:
            allHW.append(str(r["_id"]))
        current, total = current + 50, result["data"]["total"]

    # write csv
    if os.path.isfile(GRADE_CSV):
        os.remove(GRADE_CSV)
    allUsers.insert(0, "")
    write_csv(allUsers)
    allUsers.remove("")

    print("[info] fetch user status...")
    userACMap = {}
    for user in allUsers:
        current, total = 0, 1
        while current < total:
            ACSet = set()
            endpoint = "contest_submissions?contest_id={}&result=0&username={}&limit=100&offset={}".format(contestID, user, current)
            result = json.loads(curl("GET", endpoint=endpoint, use_x_csrf_token=True))
            for r in result["data"]["results"]:
                ACSet.add(str(r["problem"]))
            current, total = current + 100, result["data"]["total"]
        userACMap[user] = list(ACSet)
    print("[info] write csv")
    for hw in allHW:
        data = [hw]
        for user in allUsers:
            if hw in userACMap[user]:
                data.append(100)
            else:
                data.append(0)
        write_csv(data)
    print("[info] finish!")