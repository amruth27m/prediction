from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
api = Api(app)

from predictor.views import predictor
app.register_blueprint(predictor)

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)