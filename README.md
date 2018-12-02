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
        - Run Command: sudo systemctl start Flask-Restful-API-Deployment-Tutorial
        - Run Command: sudo systemctl enable Flask-Restful-API-Deployment-Tutorial

    12. Install nginx
        - Run Command: sudo apt-get update
        - Run Command: sudo apt-get install nginx

    11. Configure nginx
        - Run Command: sudo nano /etc/nginx/nginx.conf

    12. Add under include
        server {  
            listen 80;  
            server_name server_domain_or_ip;  
            location / {  
                proxy_set_header Host $http_host;  
                proxy_set_header X-Real-IP $remote_addr;  
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
                proxy_set_header X-Forwarded-Proto $scheme;  
                proxy_pass http://unix:/home/root/Flask-Restful-API-Deployment-Tutorial/Flask-Restful-API-Deployment-Tutorial.sock;  
            }  
        }  