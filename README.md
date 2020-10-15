# oj-cli
## Installation 
### Ghost Server
```
echo 'export PATH="~f103207425/.local/bin:$PATH"' > ~/.profile
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
#### Example
```
$ oj login
Usernme:
Password:
```

### `oj get_assign <assign_no>`
### About
Use `oj get_assign <assign_no>` to download the latest assignment from source. The downloaded files are stored in folder `hwX` or `exX`. The folder includes testing data, output data, and template C script, which are named as `1.in`, `1.out`, and `hwX.c`(or `exX.c`) separately.
