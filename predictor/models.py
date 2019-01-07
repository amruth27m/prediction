from app import db
import enum
from sqlalchemy import Enum,Column,Integer,Float
from utils.constants import GenderConstants,ProcedureConstants

Column
class Patient(db.Model):

    __tablename__ = 'patient'

    pk = db.Column(db.Integer,primary_key=True)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column('gender',Enum(GenderConstants),nullable=False)
    oldINRValue = db.Column(db.Float,nullable=False)
    procedure = db.Column('procedure',Enum(ProcedureConstants),nullable=False)
    newINRValue = db.Column(db.Float,nullable=False)
    oldDose = db.Column(db.Float,nullable=False)

    def __init__(self,args):
        self.age = args['age']
        self.gender = args['gender']
        self.oldINRValue = args['oldINRValue']
        self.newINRValue = args['newINRValue']
        self.oldDose = args['oldDose']
        self.procedure = args['procedure']

    def save(self):
        db.session.add(self)
        db.session.commit()

if __name__ == '__main__':
    db.create_all()
    db.session.commit()

