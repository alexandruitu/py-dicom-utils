from flask import Flask
from joblib import delayed
import SimpleITK as sitk
import dicom

application = Flask(__name__)


@application.route("/")
def hello_world():
    return 'heart beat'


if __name__ == "__main__":
    print("test")
    application.run()
