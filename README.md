# REST FLASK

## Developer Installation Guide (Windows)

## Prerequisites

- Python 3
- pip 3


## Install

## Virtual Environment

1.  Following command will install python virtual environment library globally.\
    > `python -m pip install virtualenv`

2.  Following command will create virtual environment directory named venv in your projects.\
    > `python -m virtualenv venv`

3.  Following command will activate the virtual environment for your project. \
    >  `.\venv\Scripts\activate`

    After this steps, `(venv)` should be appier at the begning of terninal line, like below which 
    confirms virtual environment is successfully activated. \

### Python Libraries
1.  Upgrade pip\
    (venv) ... > `python -m pip install --upgrade pip`
2.  Following command will install all the library requires for this project in the virtual environment.\
    (venv) ... > `python -m pip install -r requirements/dev.txt -e .`

## Visual studio code settings

Settings for Python Interpreter

- Purpose: This settings will enable virtual environment automatically instead of activatiin it manually.

- Press `Ctrl+Shift+P`, this will open pallete, type `interpreter`, Select `Python: Select Interpreter`, 
Select `Enter Interpreter Path`, Select `Find`, then select the python Application in your venv\Scripts directory.

Settings for [Black](https://pypi.org/project/black/): code formatter, [Flake8](https://flake8.pycqa.org/en/latest/):Style Guide Enforcer, [isort](https://pypi.org/projects/isort/): Import Sorter.

- Press `Ctrl+Shift+P`, this will open pallete, type `settings`, select `Preferences:Open Settings (JSON)`, this will open settings.json file. Replace the json data in `settings.json` with the json data in `vscode_settings.json` file.

    ***Note*** If this setting is not used, run the following commands manually every time before `Check In` the code.

    > (venv) ...\rest_flask> `black .\src`\
    > (venv) ...\rest_flask> `isort .\src`\
    > (venv) ...\rest_flask> `flake .\src`

Useful VS code Extensions:

- json
- Markdown Preview Enhanced
- markdownlint
- Partial Diff
- Pylance
- Python
- Python test Explorer for Visual Studio Code
