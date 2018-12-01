from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Flask Application Up and Running!"

if __name__ == "__main__":
    application.run(debug=True)