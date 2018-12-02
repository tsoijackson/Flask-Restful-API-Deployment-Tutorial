# Flask Restful API Deployment Tutorial

- Before Deployment:
    1. Install Python3 onto server
        - If on linux server run commands:
        - sudo apt-get update
        - sudo apt-get install python3.6
    2. Pip install virtual environment
        - Run command: pip3 install virtualenv

- Deployment:
    1. Clone this Project from Github to Server
        - Run command: git clone https://github.com/tsoijackson/Flask-Restful-API-Deployment-Tutorial.git
    2. Cd into project folder
    3. Create virtual environment
        - Run command: virtualenv projectenv
    4. Activate virtual environment
        - Run command: source projectenv/bin/activate
    5. Pip install all required libraries needed
        - Run Command: pip3 install -r requirements.txt
    6. Test if Flask application can run
        - Run Command: python3 app.py
        - If app runs, enter command CTRL-C to exit application
    7. Use Gunicorn to bind Flask app to a port
        - Run Command: gunicorn --bind localhost:8000 wsgi