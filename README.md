# Python Base

This repo is going to be the "starter kit" for your project. 
It will provide the necessary APIs.

## Setup
* First of all, make sure that you have `python` installed. Run
```cmd
python --version
```
from a regular command prompt window (or a terminal on macOS). 
It should show something like `3.6.3`.
Ensure that the version is not `2.7.*` or so (this project is not compatible with Python 2).

    
* Next, clone this repository using `git` 
(Windows users, use Git Bash for this step instead of command prompt) 
```cmd
git clone https://github.com/CodeSlammers/python-base.git myproject --depth 3
```

* The above step will download this repository to your local machine.
The download will take about a minute to complete. 

* After the download completes, enter the newly created `myproject` directory using:
```cmd
cd myproject
```
in command prompt (or terminal on macOS).

* Now, install all the dependencies such as `flask` and `SQLAlchemy` using:
```cmd
python -m pip install -r requirements.txt
```

>Note: macOS users will need to enter `sudo` before the previous command. 
It will also ask you for your password.

* [Setup MySQL server](https://github.com/CodeSlammers/waka/wiki/Setting-up-MySQL-server-and-database).

## Run the project
* Launch PyCharm and open this directory.
* [Setup run configuration in PyCharm](https://github.com/CodeSlammers/waka/wiki/Setup-run-configuration-in-PyCharm).
* Now, run the project from PyCharm. 
* Open a new browser tab, and go to address `http://localhost:5000/app`. 
It should give you a simple "Welcome" page. 
If it does, your local is working properly. Otherwise, you'll need to look up, 
first in the wiki, then all over the internet regarding why your project is not working.

## Features
* Flask micro framework
* Flask WTForms for HTML form submissions
* Flask SQLAlchemy (supports MySQL)
* Flask Bootstrap (Twitter Bootstrap, jQuery)

## License
The MIT License