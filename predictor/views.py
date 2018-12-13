from flask import Blueprint,make_response,jsonify
from flask_restful import Api,Resource,reqparse
from utils.constants import PROCEDURES,SEX,AGE_MIN,AGE_MAX,INR_MIN,INR_MAX

predictor = Blueprint('predictor', __name__)

@predictor.route('/predictor/home/',methods=['GET'])
def index():
    return "Predictor Home stub",200

def parseRequest(parser):
    parser.add_argument("sex")
    parser.add_argument("procedure")
    parser.add_argument("age")
    parser.add_argument("oldINRValue")
    parser.add_argument("newINRValue")
    parser.add_argument("oldDose")
    return parser.parse_args()

def validateArgs(args):

    age = int(args["age"])
    if age<=AGE_MIN or age>AGE_MAX:
        return False

    procedure = args["procedure"]
    if procedure not in PROCEDURES:
        return False

    sex = args["sex"]
    if sex not in SEX:
        return False

    oldINRValue = float(args["oldINRValue"])
    if oldINRValue<=INR_MIN or oldINRValue>INR_MAX:
        return False

    newINRValue = float(args["newINRValue"])
    if newINRValue<=INR_MIN or newINRValue>INR_MAX:
        return False

    return True

@predictor.route('/predictor/validate/',methods=['POST'])
def validate():
    parser = reqparse.RequestParser()
    args = parseRequest(parser)
    if(validateArgs(args)):
        return make_response(jsonify({
            "validation": "success"
        }))
    else:
        return make_response(jsonify({
            "validation": "failed"
        }))