from flask import Flask, request, abort
#from joblib import delayed
#import SimpleITK as sitk
#import dicom
import math
import json

application = Flask(__name__)


# stddev
def stddev(numbers):
    mean_numbers = sum([float(number) for number in numbers]) / len(numbers)
    std_dev = math.sqrt(sum([(float(number) - mean_numbers)**2 for number in numbers])/len(numbers))
    return str(std_dev)


# mean
def mean(numbers):
    return sum([float(i) for i in numbers]) / len(numbers)


def median(numbers):
    length = len(numbers)
    numbers.sort()
    if length % 2 == 0:
        return str((float(numbers[length/2 - 1]) + float(numbers[length/2])) / 2)
    else:
        return numbers[length/2]


@application.route('/')
def heart_beat():
    return 'heart beat'


@application.route('/<operation>', methods=['POST'])
def statistics(operation):
    try:
        numbers = request.get_json()['numbers']
    except Exception as e:
        print(e)
        return abort(500)
    if operation == 'mean':
        return str(mean(numbers))
    elif operation == 'median':
        return median(numbers)
    elif operation == 'sort':
        numbers.sort()
        return json.dumps(numbers)
    elif operation == 'stddev':
        return stddev(numbers)
    elif operation == 'mode':
        return operation


if __name__ == "__main__":
    print("test")
    application.run()
