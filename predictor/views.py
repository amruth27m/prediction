from flask import Blueprint,make_response,jsonify
from flask_restful import Api,Resource,reqparse
from utils.constants import PATIENT_DATA_PARAMETERS
from utils.validator import validateArgs
from machineLearning import mlPredictor
predictor = Blueprint('predictor', __name__)

@predictor.route('/predictor/home/',methods=['POST','GET'])
def index():
    return "Predictor Home stub",200

def parseRequest(parser):
    for parameter in PATIENT_DATA_PARAMETERS:
        parser.add_argument(parameter)

    args = parser.parse_args()
    print(args)
    return args

@predictor.route('/predictor/test/',methods=['GET','POST'])
def test():
    return "test",200

@predictor.route('/predictor/validate/',methods=['POST','GET'])
def validate():
    parser = reqparse.RequestParser()
    args = parseRequest(parser)
    response = {}
    try:
        response["validation"] = validateArgs(args)
    except (TypeError,ValueError) as error:
        print(error)
        response["validation"] = False
    finally:
        return make_response(jsonify(response)),200


@predictor.route('/predictor/predict/',methods=['POST'])
def predict():
    '''Stub for prediction'''
    parser = reqparse.RequestParser()
    args = parseRequest(parser)
    print("TESTING")
    respone = {}
    try:
        respone["validation"] = validateArgs(args)
        print(respone["validation"])
        respone["predicted_dosage"] = mlPredictor.predict(args).tolist()
    except (TypeError,ValueError) as error:
        print(error)
        respone["validation"] = False
        respone["predicted_dosage"] = False
    finally:
        return make_response(jsonify(respone)),200

@predictor.route('/predictor/create/',methods=['POST'])
def testCreate():
    test = {
        "gender": "Male",
        "procedure": "MVR",
        "age": 10,
        "oldINRValue": 3.2,
        "newINRValue": 3.2,
        "oldDose": 5
    }
    from predictor.models import Patient
    testPatient = Patient(test)
    testPatient.save()
    return 'success',200