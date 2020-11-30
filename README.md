# oj-cli
## Installation 
### Ghost Server
```
cd ~
echo 'export PATH="~f103207425/.local/bin:$PATH"' >> ~/.profile
source ~/.bashrc
```

### Install from Source Code
1. Clone this project
```
git clone https://github.com/josix/oj-cli.git
```

2. Update `HOST` variable value in file `oj-cli/constants.py` to the OnlineJudge URL you accessing
3. Update Shebang(`#!/opt/csw/bin/python2.7`) value to a suitable one in `oj.py`

### Commands
### `oj login`
### About
Use `oj login` to login to the account in OnlineJudge. It required you to enter your account information so that `oj-cli` could access OnlineJudge service successfully. After entering your username and password. `oj-cli` will respond if you login successfully or not.
### Usage
No argument required. Only enter `oj login` and fill the account information to login to OnlineJudge.
### Example
```
$ oj login
Usernme:
Password:
```

### `oj get_assign <assign_no>`
### About
Use `oj get_assign <assign_no>` to download the latest assignment from contest. The downloaded files are stored in folder `hwX` or `exX`. The folder includes testing data, output data, and template C script, which are named as `1.in`, `1.out`, and `hwX.c`(or `exX.c`) separately.
### Usage
`oj get_assign` only required one argument to execute.
#### assign_no
assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened.

### Example
```
$ oj get_assign hw2
$ oj get_assign ex3
```


### `oj submit <assign_no> <code_file>`
### About
Use `oj submit <assign_no> <code_file>` to submit your code to contest. 

### Usage
`oj get_assign` required two arguments to execute.

#### assign_no
assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened.

#### code_file
code_file is the path to your script. `oj` will read the file then submit this answer to OnlineJudge Service.

#### Example
```
$ oj submit hw2 hw2.c
$ oj submit ex3 ../ex3.c
```


### `oj contest <options> <assign_no>`
### About
Use `oj contest <option> <assign_no>` to get rank, status, and update contest map.
### Usage
`oj contest` required two arguments to execute.

#### options
options allows three different methods: rank, status, and update.

`rank`
It shows the rank of the contest by bar graph and score.

`status`
It shows the latest 20 submissions of the contest.

`update`
It updates the assignment_map.json.

#### assign_no
assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and provide the existing assign number in the map.

#### Example
```
$ oj contest status Exercise8
$ oj contest rank Assign8
$ oj contest update .
```
