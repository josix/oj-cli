# oj-cli
## Installation 
### Installation in NCCU GHOST

```
echo 'alias oj="python2.7 ~s10940/oj-cli/oj.py"' >> ~/.profile
source ~/.profile
```

### Installation from source code

```
cd ~
git clone https://github.com/andyjjrt/oj-cli.git
cd oj-cli
echo 'alias oj="python2.7 ~/oj-cli/oj"' >> ~/.bashrc
source ~/.bashrc
```

If your shell is different like `ash`, you may need to change `.bashrc` to `.profile`.
After installation, please modify `CONTEST_NAME` variable in `constants.py` to the target contest name.


### Commands
### oj login
#### About
Use `oj login` to login to the account in OnlineJudge. It required you to enter your account information so that `oj-cli` could access OnlineJudge service successfully. After entering your username and password. `oj-cli` will respond if you login successfully or not.
#### Usage
No argument required. Only enter `oj login` and fill the account information to login to OnlineJudge.
#### Example
```
$ oj login
Usernme:
Password:
```

### oj get <assign_no>
#### About
Use `oj get <assign_no>` to download the latest assignment from contest. The downloaded files are stored in folder `hwX`. The folder includes testing data, output data, and template C script, which are named as `1.in`, `1.out`, and `main.c` separately.
#### Usage
`oj get` only required one argument to execute.
##### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers.

#### Example
```
$ oj get hw1
Made a [hw1] folder in your current directory.
```

### oj get_p <problem_no>
#### About
Use `oj get_p <problem_no>` to download the problem in problem list. The downloaded files are stored in folder `problem_X`. The folder includes testing data, output data, and template C script, which are named as `1.in`, `1.out`, and `main.c` separately.
#### Usage
`oj get_p` only required one argument to execute.
##### problem_no
problem_no represents your problem display id like `1`, `57-2` according to your updates. `oj-cli` will prompt `Invalid Problem Id!` if the input problem id is invalid.
##### Notice
problem_no somtimes has blanks, cli will automatically replace them.
#### Example
```
$ oj get_p 57-2
Made a [problem_57-2] folder in your current directory.
```

### oj submit <assign_no> <code_file>
#### About
Use `oj submit <assign_no> <code_file>` to submit your code to contest and return the results. 

#### Usage
`oj submit` required two arguments to execute.

##### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers. 

##### code_file
code_file is the path to your script. `oj` will read the file then submit this answer to OnlineJudge Service.

#### Example
```
$ oj submit hw2 hw2.c
Submit successfully!
Getting submission status...
=================================================
Result: AC(Accept)              Score: 100
|ID |Status                |   Time|  Mem| Score|
|#1 |AC(Accept)            |    0ms|  2MB|    20|
|#2 |AC(Accept)            |    2ms|  2MB|    20|
|#3 |AC(Accept)            |   40ms|  2MB|    20|
|#4 |AC(Accept)            |   75ms|  2MB|    20|
|#5 |AC(Accept)            |    5ms|  2MB|    20| 
================================================= 
```


### oj submit_p <problem_no> <code_file>
#### About
Use `oj submit_p <problem_no> <code_file>` to submit your code to problem and return the results. 

#### Usage
`oj submit_p` required three arguments to execute.

##### problem_no
assign_no represents your assign number like `1`, `2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number soes not exist. 

Notice that blanks in `problem_no` will be replaced by nothing.

##### code_file
code_file is the path to your script. `oj` will read the file then submit this answer to OnlineJudge Service.

#### Example
```
$ oj problem_submit 1091CP1_Exercise8 ex8.c
Submit successfully!!
Getting submission status...
========================================================
Result: AC(Accept)                     Score: 100
|ID |Status                       |   Time|  Mem| Score|
|#1 |AC(Accept)                   |    1ms|  2MB|    20|
|#2 |AC(Accept)                   |    1ms|  2MB|    20|
|#3 |AC(Accept)                   |    1ms|  2MB|    20|
|#4 |AC(Accept)                   |    2ms|  2MB|    20|
|#5 |AC(Accept)                   |    1ms|  2MB|    20|
========================================================

```


### oj rank <assign_no>
#### About
Use `oj rank <assign_no>` to view the class result of this assign.
#### Usage
`oj rank` only required one argument to execute.
#### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers. 

#### Example
```
$ oj rank hw2
Your status of hw2 : AC(Accept)
================================================
   1~ 10 :  0  |  AC(Accept)             : 8
  11~ 20 :  0  |  RE(Runtime Error)      : 29
  21~ 30 :  0  |  PAC(Partial Accepted)  : 54
  31~ 40 :  1  |  WA(Wrong Answer)       : 81
  41~ 50 :  0  |  CE(Compilation Error)  : 10
  51~ 60 :  0  |--------------------------------
  61~ 70 :  0  |  Total submissions      : 182
  71~ 80 :  0  |
  81~ 90 :  0  |
  91~100 : 12  |
================================================
For real score ranking,please go to the website. 
```


### oj update
#### About
Use `oj update` to get the latest assignments.
#### Usage
No argument required. Only enter `oj update` and it will automatically get the assignments and the problems.

#### Example
```
$ oj update
Updated problems successfully!
Found HomeWork: hw01 [Nim!]
Found HomeWork: ex01 [Tree Postorder]
Updated assign successfully!
```


### oj status <assign_no>
#### About
Use `oj status <assign_no>` to view the latest 20 submissions of this contest.
#### Usage
`oj status` only required one argument to execute.
##### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers. 

#### Example
```
$ oj status hw2
============================================================================
|  Contest Name: hw2                                             |
============================================================================
|User        |Status                     |   Time|  Mem|               When|
|108xxxxxx   |WA(Wrong Answer)           |    0ms|  2MB|2020-12-18 10:31:12|
|109xxxxxx   |AC(Accept)                 |    0ms|  2MB|2020-12-18 10:07:14|
|109xxxxxx   |PAC(Partial Accepted)      |    0ms|  2MB|2020-12-18 09:20:10|
|109xxxxxx   |PAC(Partial Accepted)      |   21ms|  2MB|2020-12-18 09:20:02|
|109xxxxxx   |PAC(Partial Accepted)      |   17ms|  2MB|2020-12-18 09:07:19|
|109xxxxxx   |PAC(Partial Accepted)      |    1ms|  4MB|2020-12-18 08:50:13|
============================================================================
...
```

### oj mystat <option>
#### About
Use `oj mystat <option>` to view your latest 20 submissions of this contest, each of the submission has the specific ID.
#### Usage
`oj mystat` only required one argument to execute.
##### option
Here we have two options:
1. assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers.  
2. IDx is the specific ID that `oj mystat <hwx>` gives you, here you can see details of this submition.
#### Note
The ID will only update if you type `oj mystat <hwx>`

#### Example
```
$ oj mystat hw1
====================================================================
|  Contest Name: hw1                                     |
====================================================================
|ID  |Status                     |   Time|  Mem|               When|
|ID 0|AC(Accept)                 |    0ms|  2MB|2020-12-17 10:39:13|
====================================================================

$ oj mystat ID4
=================================================
Result: PAC(Partial Accepted)   Score:  20
|ID |Status                |   Time|  Mem| Score|
|#1 |AC(Accept)            |    1ms|  2MB|    20|
|#2 |WA(Wrong Answer)      |    2ms|  2MB|     0|
|#3 |WA(Wrong Answer)      |   28ms|  2MB|     0|
|#4 |WA(Wrong Answer)      |   48ms|  2MB|     0|
|#5 |WA(Wrong Answer)      |    5ms|  2MB|     0|
================================================= 
```

### oj dl <ID>
#### About
Use `oj dl <ID>` to download your specific submission's source code.
#### Usage
`oj dl` only required one argument to execute.
#### option
ID is the specific ID that `oj mystat <hwx>` gives you, here you can see details of this submition.
#### Note
The ID will only update if you type `oj mystat <hwx>`

#### Example
```
$ oj dl ID0
=================================================
Result: AC(Accept)              Score: 100
|ID |Status                |   Time|  Mem| Score|
|#1 |AC(Accept)            |    0ms|  2MB|    20|
|#2 |AC(Accept)            |    2ms|  2MB|    20|
|#3 |AC(Accept)            |   40ms|  2MB|    20|
|#4 |AC(Accept)            |   75ms|  2MB|    20|
|#5 |AC(Accept)            |    5ms|  2MB|    20|
=================================================
Downloaded your file!!!
File name:1097030xx|xxxxxxxxxxxxxxxxxxxxxxx.c in yor current directory. 
```


