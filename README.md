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
    2. Cd into project folder ( cd Flask-Restful-API-Deployment-Tutorial )
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
        - Run Command: gunicorn --bind 0.0.0.0:8000 wsgi
        - If app runs, enter command CTRL-C to exit application
    8. Create systemd file
        - Run Command: sudo nano /etc/systemd/system/Flask-Restful-API-Deployment-Tutorial.service
    9. Write into conf file (without bullet points) <br /><br />
        [Unit]  
        Description=Gunicorn instance 
        After=network.target  

        [Service]  
        User=root  
        Group=nginx  
        WorkingDirectory=/home/root/Flask-Restful-API-Deployment-Tutorial  
        Environment="PATH=/home/root/Flask-Restful-API-Deployment-Tutorial/projectenv/bin"  
        ExecStart=/home/root/Flask-Restful-API-Deployment-Tutorial/projectenv/bin/gunicorn --workers 3 --bind unix:Flask-Restful-API-Deployment-Tutorial.sock -m 007 wsgi  

        [Install]  
        WantedBy=multi-user.target  
    
    10. Start Process
        - Run Command: sudo start Flask-Restful-API-Deployment-Tutorial