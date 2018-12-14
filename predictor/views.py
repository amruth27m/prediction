from flask import Blueprint,make_response,jsonify
from flask_restful import Api,Resource,reqparse
from utils.constants import PATIENT_DATA_PARAMETERS
from utils.validator import validateArgs

predictor = Blueprint('predictor', __name__)

@predictor.route('/predictor/home/',methods=['GET'])
def index():
    return "Predictor Home stub",200

def parseRequest(parser):
    for parameter in PATIENT_DATA_PARAMETERS:
        parser.add_argument(parameter)
    return parser.parse_args()




@predictor.route('/predictor/test/',methods=['GET'])
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
    respone = {}
    try:
        respone["validation"] = validateArgs(args)
        respone["predicted_dosage"] = True
    except (TypeError,ValueError) as error:
        respone["validation"] = False
        respone["predicted_dosage"] = False
    finally:
        return make_response(jsonify(respone)),200
