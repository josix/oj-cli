#!/opt/csw/bin/python2.7
import argparse

from commands import auth, get_assign, get_problem, status, submit, update_contest_map, update_problem_map, contests_result, contests_status, my_contests_status,dl, problem_submit, get_grades

parser = argparse.ArgumentParser(
    prog="oj",
    description="https://github.com/andyjjrt/oj-cli#oj-cli",
)
subparsers = parser.add_subparsers(dest="subcmd")
parser_login = subparsers.add_parser(
    "login", description="Login your account to CP Online Judge"
)
parser_login.set_defaults(func=auth)

parser_update = subparsers.add_parser(
    "update", description="Update your Assign and Exercise Homework"
)
parser_login.set_defaults(func=update_contest_map)

parser_update = subparsers.add_parser(
    "update_p", description="Update your Problems"
)
parser_login.set_defaults(func=update_problem_map)

parser_get_assign = subparsers.add_parser(
    "get", description="Get assignment/exercise from contest"
)
parser_get_assign.add_argument("assign_no", type=str, help="assignment number")
parser_get_assign.set_defaults(func=get_assign)


parser_contest = subparsers.add_parser(
    "mystat", description="Show your latest 20 submissions of the specific contest or show specific submission status."
)
parser_contest.add_argument("assign_no", type=str, help="assignment number or submitID")
parser_contest.set_defaults(func=my_contests_status)

parser_contest = subparsers.add_parser(
    "status", description="Show the latest 20 submissions of the specific contest."
)
parser_contest.add_argument("assign_no", type=str, help="assignment number")
parser_contest.set_defaults(func=contests_status)

parser_contest = subparsers.add_parser(
    "rank", description="Show the score of the whole class."
)
parser_contest.add_argument("assign_no", type=str, help="assignment number")
parser_contest.set_defaults(func=contests_result)



parser_get_problem = subparsers.add_parser(
    "get_p", description="Get problem from public problem"
)
parser_get_problem.add_argument("problem_id", type=str, help="problem display ID")

parser_submit = subparsers.add_parser(
    "submit", description="Submit and grade your code"
)
parser_submit.add_argument("assign_no", type=str, help="assignment number")
parser_submit.add_argument("code_file", type=str, help="file of your codes")

parser_dl = subparsers.add_parser("dl", description="Get submission source code")
parser_dl.add_argument("submission_id", type=str, help="Your submission ID")

parser_problem_submit = subparsers.add_parser(
    "submit_p", description="Submit your probkem answer and grade your code"
)
parser_problem_submit.add_argument("problem_id", type=str, help="problem id")
parser_problem_submit.add_argument("code_file", type=str, help="file of your codes")

parser_grades = subparsers.add_parser("grades", description="get grades from contest")
parser_grades.add_argument("contest", type=str, help="contest name")


args = parser.parse_args()
cmd_to_func = {
    "login": auth,
	"update": update_contest_map,
    "update_p": update_problem_map,
    "get": lambda: get_assign(args.assign_no),
    "get_p": lambda: get_problem(args.problem_id),
    "submit": lambda: submit(args.assign_no, args.code_file),
	"submit_p": lambda: problem_submit(args.problem_id, args.code_file), 
	"status": lambda: contests_status(args.assign_no),
	"mystat": lambda: my_contests_status(args.assign_no),
	"rank": lambda: contests_result(args.assign_no),
	"dl": lambda: dl(args.submission_id),
    "grades": lambda:get_grades(args.contest),
}


cmd_to_func[args.subcmd]()
