from flask import Blueprint,make_response,jsonify
from flask_restful import Api,Resource,reqparse
from utils.constants import PROCEDURES,GENDER,AGE_MIN,AGE_MAX,INR_MIN,INR_MAX,PATIENT_DATA_PARAMETERS

predictor = Blueprint('predictor', __name__)

@predictor.route('/predictor/home/',methods=['GET'])
def index():
    return "Predictor Home stub",200

def parseRequest(parser):
    for parameter in PATIENT_DATA_PARAMETERS:
        parser.add_argument(parameter)
    return parser.parse_args()

def validateArgs(args):
    '''Returns true is the args is valid patient data parameters
        else throws Exception
    '''
    try:
        age = int(args["age"])
        if age <= AGE_MIN or age > AGE_MAX:
            raise ValueError("age must be between %d and %d" % (AGE_MIN,AGE_MAX))
    except ValueError as error:
        raise ValueError(error)

    procedure = args["procedure"]
    if procedure not in PROCEDURES:
        raise ValueError("Undefined procedure %s" % procedure)

    gender = args["gender"]
    if gender not in GENDER:
        raise ValueError("Undefined gender %s" % gender)

    try:
        oldINRValue = float(args["oldINRValue"])
        if oldINRValue<=INR_MIN or oldINRValue>INR_MAX:
            raise ValueError("oldINRValue must be between %d and %d" %(INR_MIN, INR_MAX))
    except TypeError as error:
        raise ValueError("oldINRValue cannot be %s \n %s" %(args["oldINRValue"],error))

    try:
        newINRValue = float(args["newINRValue"])
        if newINRValue<=INR_MIN or newINRValue>INR_MAX:
            raise ValueError("oldINRValue must be between %d and %d" % (INR_MIN, INR_MAX))
    except TypeError as error:
        raise ValueError("newINRValue cannot be %s \n %s"%(args['newINRValue'],error))

    return True

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
        response["validation"] = False
    finally:
        return make_response(jsonify(response))


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
        return make_response(jsonify(respone))
