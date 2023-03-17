#https://flask.palletsprojects.com/en/1.1.x/quickstart/
#pypi.org
#Day35 Environment variable
#https://github.com/appbrewery/terminal-mac-cheatsheet
#python tutor: https://pythontutor.com/visualize.html#mode=edit

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()