# Quaddle [![unit-tests](https://github.com/steambun/caramel-slice/actions/workflows/main.yml/badge.svg)](https://github.com/steambun/caramel-slice/actions/workflows/main.yml)

> Quaddle is an alternative interpretation of Wordle for 4 letters.  It notably leverages the python flask web app framework along with GPT3.

- [Developing Quaddle](#develop)
  - [Device](#device)
  - [Python](#python)
  - [Heroku](#heroku)
  - [Testing](#testing)
  - [Debugging](#debugging)
  - [Tutorials](#tutorials)
 
## Developing Quaddle

Read on for the basic setup to develop quaddle.

### Device

1) Install Linux on Chrome Book
2) Install Visual Studio Code 

### Python

1) Install Python v3
2) Install [Pip](https://pip.pypa.io/en/stable/installation/), the package manager for Python
    ```sh
    sudo apt update
    sudo apt install python3-venv python3-pip
    ```

    > **Note**: python3-pip and python-venv should already be installed.

    [Python Flask Tutorial](https://realpython.com/flask-by-example-part-1-project-setup) - basics of setting up a Python Flask Example application
    
    [Python Flask with Heroku Tutorial](https://mattermost.com/blog/deploying-a-web-app-with-python-flask-and-heroku) - alternative tutorial that also includes heroku

3) Setting up virtual environment
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
4) Install flask
    ```sh
    # (optional) uninstall
    pip uninstall flask

    # install
    pip install flask 

    # snapshot dependency version requirements
    python3 -m pip freeze > requirements.txt
    ```

5) Setup path
    - Add `/home/<username>/.local/bin` into `PATH` in the `~/.bashrc`

6) Initialize Application 
    - Create a file called `app.py` in the top level directory

7) Run flask
    ```sh
    flask run
    ```
    Goto http://127.0.0.1:5000/ and it should display a welcome message!

### Heroku

1) Install Heroku CLI
    [Heroku Installation Tutorial](https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods)

    Mac:
    - 1.1) Install brew CLI from https://brew.sh 
    - 1.2) Install Heroku CLI 

        ```
        brew tap heroku/brew && brew install heroku
        ```

2) Login

    ```sh
    heroku login
    ```

3) Deploying
    - 3.1) Create a Procfile    
    - 3.2) Install Gunicorn
        ```sh
        # installing gunicorn
        python3 -m pip install gunicorn==20.0.4

        # snapshot dependency version requirements
        python3 -m pip freeze > requirements.txt
        ```    
    
    - 3.3) Creating app in heroku (WARNING only 1 person needs to do this!)
        ```sh
        heroku create caramel-slice
        ```
    
    - 3.4) Manually open the app within Heroku and auto deploy the main branch upon any changes being received 
        https://dashboard.heroku.com/apps/caramel-slice


### Testing

Recommended and simplist/cleanest unit testing framework for python is pytest

1. Install the framework
    ```sh
    pip install pytest
    ```

2. Update the requirements file to reflect the latest install
    ```sh
    python3 -m pip freeze > requirements.txt
    ```

3. Familiarise yourself with framework with an [online tutorial](https://realpython.com/pytest-python-testing/)


### Debugging

VSCode has a great built in support for python flask debugging.  

**Gotchas:**
  * Ensure that you are not running existing services locally on the same port 
  * Kill existing web browsers running on the local port so that you can deliberately control the execution of the first http request


### Tutorials

1. **HTML**: Rendering HTML rather than text [tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)

2. **Sessions**: Using sessions to avoid using global variables [tutorial 1](https://vivek-kaushal.medium.com/handling-global-variables-in-flask-36c5b4564792) and [tutorial 2](https://flask-session.readthedocs.io/en/latest/)

    The particular problem that we're trying to avoid is that when running guniron (python webserver) within heroku it defaults to running 2 workers (not 1) and so sharing global state is dangerous and unworkable.  Description of problem on [stackoverflow](https://stackoverflow.com/questions/62328835/why-my-flask-backend-is-unstable-on-heroku/62330039#62330039)

    To solve this we have chosen to use client-side sessions (stored on client's device) not server side sessions (stored on server/db)
      * Generate a secret key by running the following on linux ([instructions](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY))        
        ```sh
        python3 -c 'import os; print(os.urandom(16))'
        ```

3) **GitHub**: Start using issues in github to track new features / bugs in the software
    Familarise yourself with the commit auto picked up syntax reading their [doc](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)
    
      e.g. Write "Fix #4" as part of the pull request commit message
