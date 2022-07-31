Step 1) Install Linux on Chrome Book
Step 2) Install Visual Studio Code 
Step 3) Install Python3
(The following is from a Flash + Heroku + Python tutorial here:
https://mattermost.com/blog/deploying-a-web-app-with-python-flask-and-heroku/)
BUT THEN CHANGED to
https://realpython.com/flask-by-example/part-1-project-setup
Step 4) Install Pip (package manager for python)
    4.1) sudo apt update
    4.2) sudo apt install python3-venv python3-pip
    Note: python3-pip and python-venv should already be installed
Step 5) Setting up virtual environment
    5.1) python3 -m venv venv
    5.2) source venv/bin/activate
Step 6) Install flask
    6.1) pip install flask (you might have to run 'pip uninstall flask' first, if you had older version)
    6.2) python3 -m pip freeze > requirements.txt
    6.2) add /home/<username>/.local/bin into PATH in the ~/.bashrc
Step 7) Initialize Application 
    7.1) Create app.py
Step 8) Run flask
    8.1) flask run
    8.2) http://127.0.0.1:5000/ should now display a welcome message!