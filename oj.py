#!/usr/local/bin/python2.7

import argparse
from commands import auth, get_assign

parser = argparse.ArgumentParser(
    prog="oj",
    description="CLI tool that helping you access CP Online Judge",
)
subparsers = parser.add_subparsers(dest="subcmd")
parser_login = subparsers.add_parser(
    "login", description="Login your account to CP Online Judge"
)
parser_login.set_defaults(func=auth)

parser_get_assign = subparsers.add_parser(
    "get_assign", description="Get you assignment/exercise from CP Online Judge"
)
parser_get_assign.add_argument("assign_no", type=str, help="assignment number")
parser_login.set_defaults(func=get_assign)

args = parser.parse_args()
cmd_to_func = {
    "login": auth,
    "get_assign": lambda: get_assign(args.assign_no),
}
cmd_to_func[args.subcmd]()
