from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

from predictor.views import predictor
app.register_blueprint(predictor)


if __name__ == '__main__':
    app.run(debug=True)