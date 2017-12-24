from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'heart beat'



if __name__ == "__main__":
    print("test")
    application.run()