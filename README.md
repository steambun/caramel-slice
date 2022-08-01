# PART I - INSTALLING DEVELOPMENT ENVIRONMENT

1) Install Linux on Chrome Book
2) Install Visual Studio Code 

# PART II - SETTING UP PYTHON/flask

1) Install Python3
2) Install Pip (package manager for python)
    https://pip.pypa.io/en/stable/installation/
    - 2.1) `sudo apt update`
    - 2.2) `sudo apt install python3-venv python3-pip`
    Note: python3-pip and python-venv should already be installed

(The following is from a Flash + Heroku + Python tutorial here:
https://mattermost.com/blog/deploying-a-web-app-with-python-flask-and-heroku/)
BUT THEN CHANGED to
https://realpython.com/flask-by-example/part-1-project-setup

3) Setting up virtual environment
    - 3.1) `python3 -m venv venv`
    - 3.2) `source venv/bin/activate`
4) Install flask
    - 4.1) `pip install flask (you might have to run 'pip uninstall flask'` first, if you had older version)
    - 4.2) `python3 -m pip freeze > requirements.txt`
    - 4.4) add `/home/<username>/.local/bin` into `PATH` in the `~/.bashrc`
5) Initialize Application 
    - 5.1) Create app.py
6) Run flask
    - 6.1) `flask run`
    - 6.2) http://127.0.0.1:5000/ should now display a welcome message!

# PART III - DEPLOYING ON HEROKU

1) Install Heroku CLI
    https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods

    Mac:
    - 1.1) Install brew CLI from https://brew.sh 
    - 1.2) Install Heroku CLI 
        `brew tap heroku/brew && brew install heroku`

2)  Login
    - 2.1) `heroku login`

3) Deploying
    - 3.1) Create procfile
    
    - 3.2) Install Gunicorn
        `python3 -m pip install gunicorn==20.0.4`
        Add entry to requirements.txt
    
    - 3.3) Creating app in heroku (WARNING only 1 person needs to do this!)
        `heroku create caramel-slice`
    
    - 3.4) Manually open the app within Heroku and auto deploy the main branch upon any changes being received 
        https://dashboard.heroku.com/apps/caramel-slice


# PART IV - INTEGRATING QUADDLE BEHAVIOUR INTO WEB APP

1) Rendering HTML rather than txt
    https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

*) Introducing sessions to avoid using global variables
    https://vivek-kaushal.medium.com/handling-global-variables-in-flask-36c5b4564792
    https://flask-session.readthedocs.io/en/latest/

