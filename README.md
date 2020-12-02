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


### `oj rank <assign_no>`
 ### About
 Use `oj rank <assign_no>` to view the class result of this assign.
 ### Usage
 `oj rank` only required one argument to execute.
 #### assign_no
 assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened.

 ### Example
 ```
 $ oj rank hw2
 $ oj rank ex3
 ```


 ### `oj update`
 ### About
 Use `oj update` to get the latest assignments.
 ### Usage
 No argument required. Only enter `oj update` and it will automatically get the assignments.

 ### Example
 ```
 $ oj update
 ```


 ### `oj stat <assign_no>`
 ### About
 Use `oj stat <assign_no>` to view the latest 20 submissions of this contest.
 ### Usage
 `oj stat` only required one argument to execute.
 #### assign_no
 assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened.

 ### Example
 ```
 $ oj stat hw2
 $ oj stat ex3
 ```



 ### `oj mystat <assign_no || ID>`
 ### About
 Use `oj mystat <assign_no || ID>` to view your latest 20 submissions of this contest or your specific submission.
 ### Usage
 `oj mystat` only required one argument to execute.
 #### assign_no || ID
 assign_no represents your assign number like `hw1`, `ex1`, etc. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened.
 Your stat will show by table and every stat have an ID for you to see details. Type `oj mystat <ID>` to see.
 
 
 ### Example
 ```
 $ oj mystat hw2
 $ oj mystat ID2
 ```
 
