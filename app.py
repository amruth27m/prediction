from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import  SQLAlchemy
# from config import LocalDev
from predictor.views import predictor

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test11.db'

db = SQLAlchemy(app)

app.register_blueprint(predictor)

if __name__ == '__main__':
    from predictor.models import Patient
    db.create_all()
    db.session.commit()
    app.run(debug=True)
