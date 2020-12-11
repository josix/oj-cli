# oj-cli
## Installation 
### Installation from source code & Ghost Installation
```
cd ~
git clone https://github.com/andyjjrt/oj-cli.git
cd oj-cli
chmod 700 install.sh
chmod 700 update.sh
./install.sh
```

### Commands
### `oj login`
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

### `oj get_assign <assign_no>`
#### About
Use `oj get_assign <assign_no>` to download the latest assignment from contest. The downloaded files are stored in folder `hwX`. The folder includes testing data, output data, and template C script, which are named as `1.in`, `1.out`, and `main.c` separately.
#### Usage
`oj get_assign` only required one argument to execute.
##### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers.

### Example
```
$ oj get_assign hw2
<invalid sample>
$ oj get_assign hw4
Invalid Assign Number!
Available names are:
- hw2 [Assignment 9]
- hw1 [Exercise 9]
If you want to update latest homework assignment, type: [oj update] to update. 
```


### `oj submit <assign_no> <code_file>`
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
Your submission Id is xxxxxxxxxxxxxxxxxx
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


### `oj rank <assign_no>`
### About
Use `oj rank <assign_no>` to view the class result of this assign.
### Usage
`oj rank` only required one argument to execute.
#### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers. 

### Example
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


### `oj update`
### About
Use `oj update` to get the latest assignments.
### Usage
No argument required. Only enter `oj update` and it will automatically get the assignments.

### Example
```
$ oj update
Found HomeWork: hw1 [Exercise 9]
Found HomeWork: hw2 [Assignment 9]
Updated successfully! 
```


### `oj stat <assign_no>`
### About
Use `oj stat <assign_no>` to view the latest 20 submissions of this contest.
### Usage
`oj stat` only required one argument to execute.
#### assign_no
assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers. 

### Example
```
$ oj stat hw2
|User        |Status                |   Time|  Mem|               When|
|1097030xx   |AC(Accept)            |   71ms|  2MB|2020-12-06 06:46:00|
|1097030xx   |RE(Runtime Error)     |    0ms|  2MB|2020-12-06 06:38:57|
|1097030xx   |WA(Wrong Answer)      |   66ms|  2MB|2020-12-06 06:25:41|
|1097030xx   |RE(Runtime Error)     |    0ms|  2MB|2020-12-06 06:22:08|
|1097030xx   |RE(Runtime Error)     |    0ms|  2MB|2020-12-06 06:19:15|
...
```

### `oj mystat <option>`
### About
Use `oj mystat <option>` to view your latest 20 submissions of this contest, each of the submission has the specific ID.
### Usage
`oj mystat` only required one argument to execute.
#### option
Here we have two options:
1. assign_no represents your assign number like `hw1`, `hw2` according to your updates. `oj-cli` will prompt `Invalid Assign Number!` if the input assign number has not opened and give valid assign numbers.  
2. IDx is the specific ID that `oj mystat <hwx>` gives you, here you can see details of this submition.
#### Note
The ID will only update if you type `oj mystat <hwx>`

### Example
```
$ oj mystat hw2
|ID  |Status                |   Time|  Mem|               When|
|ID 0|AC(Accept)            |   71ms|  2MB|2020-12-06 06:46:00|
|ID 1|WA(Wrong Answer)      |   66ms|  2MB|2020-12-06 06:25:41|
|ID 2|AC(Accept)            |   72ms|  2MB|2020-12-03 13:35:16|
|ID 3|CE(Compilation Error) |-------|-----|2020-12-03 13:34:26|
|ID 4|PAC(Partial Accepted) |   47ms|  2MB|2020-12-03 12:17:22|
|ID 5|PAC(Partial Accepted) |   46ms|  2MB|2020-12-03 12:12:47| 
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

### `oj dl <ID>`
### About
Use `oj dl <ID>` to download your specific submission's source code.
### Usage
`oj dl` only required one argument to execute.
#### option
ID is the specific ID that `oj mystat <hwx>` gives you, here you can see details of this submition.
#### Note
The ID will only update if you type `oj mystat <hwx>`

### Example
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

