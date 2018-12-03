# Flask Restful API Deployment Tutorial

- Before Deployment:
    1. Install Python3 onto server
        - If on linux server run commands:
        - sudo apt-get update
        - sudo apt-get install python3.6
    2. Pip install virtual environment
        - Run command: pip3 install virtualenv

- Checking if Project Can Run On Server:
    1. Clone this Project from Github to Server
        - Run command: git clone https://github.com/tsoijackson/Flask-Restful-API-Deployment-Tutorial.git
    2. Cd into project folder ( cd Flask-Restful-API-Deployment-Tutorial )
    3. Create virtual environment
        - Run command: virtualenv projectenv
    4. Activate virtual environment
        - Run command: source projectenv/bin/activate
    5. Pip install all required libraries needed
        - Run Command: pip install -r requirements.txt
    6. Test if Flask application can run
        - Run Command: python3 app.py
        - If app runs, enter command CTRL-C to exit application
    7. Use Gunicorn to bind Flask app to a port
        - Run Command: gunicorn --bind 0.0.0.0:8000 wsgi
        - If app runs, enter command CTRL-C to exit application

- Deployment:
    1. Install Supervisor
        - apt-get install supervisor
        - service supervisor restart
        - sudo supervisorctl reload
    2. Create conf file
        - sudo nano /etc/supervisor/conf.d/Flask-Restful-API-Deployment-Tutorial.conf
    3. Write into the file  

        [program:Flask-Restful-API-Deployment-Tutorial]  
        command=/Flask-Restful-API-Deployment-Tutorial/projectenv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi  
        directory=/Flask-Restful-API-Deployment-Tutorial  
        autostart=true  
        autorestart=true  
        stderr_logfile=/var/log/Flask-Restful-API-Deployment-Tutorial.err.log  
        stdout_logfile=/var/log/Flask-Restful-API-Deployment-Tutorial.out.log  
    4. Update Changes
        - sudo supervisorctl reread
        - sudo supervisorctl update
    5. Check if Processes Running
        - ps ax | grep gunicorn
        - sudo supervisorctl status Flask-Restful-API-Deployment-Tutorial
        - Log Errors: sudo nano /var/log/Flask-Restful-API-Deployment-Tutorial.err.log