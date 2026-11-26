import os
from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    env = os.environ.get("APP_ENV", "not set")
    return f"<h1>Beanstalk App - Version 1</h1><p>APP_ENV = {env}</p>"

if __name__ == "__main__":
    application.run()
