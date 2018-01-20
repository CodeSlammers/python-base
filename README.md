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
* Flask Web assets
* Flask Navigation

## Directory Structure
* All JavaScript and CSS files will go inside their corresponding directories in `static/`
* These files need to be registered before they are run on the browser. 
To do so, register the files in `bundle/bundle.py`
* Flask configuration are stored in `config/config.py`. 
Development specific configurations are stored in `config/dev_config.py`.
* The project is divided into two parts: HTTP API, whose blueprint lies in the `api/` directory,
and the frontend layouts, whose blueprints are stored in the `frontend/` directory.
* If you want to add a new page, you need to create a route mapping in `frontend/`, blueprint
* If you want this page to appear on the navigation bar, register it on `nav/nav.py`. 
For further info, search for "Flask Nav" extension
* All HTML documents will go in `templates/` directory. These documents are templated using Jinja2.
* See `templates/sample_page.html` on how to create a sample HTML page.
* All database models are stored in `database/models` directory. 
If you create a new model, don't forget to include it in `database/models/__init__.py`.

## Endpoints
The default endpoint is `http://localhost:5000`. 
Here's the breakdown of everything that is accessible through web
* On `/`, You'll get a "Hello, World!" response.
* The HTTP API rests on `/api/`
* On `/api/count` there's a counter in order to test database connection. 
This value should increase every time you refresh the page.
* On `/app`, the frontend UI rests.
* On `/_debug` and `/reflect/`, you can see a simple debugging toolbar 
where you can see the registered routes.

## License
The MIT License