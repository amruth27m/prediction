from app import db,app

class Age(db.Model):
    '''patient's age'''
    age = db.Coloumn(db.Integer,nullable=False)
    _ageMax = 120
    _ageMin = 23

    def __init__(self,age):
        self.age = age

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def ageMax(self):
        return type(self)._ageMax

    @property
    def ageMin(self):
        return type(self)._ageMin

    @staticmethod
    def validate(age):
        if age <=Age.ageMax  or age > Age.ageMin:
            raise ValueError("age must be between %d and %d" % (Age.ageMin, Age.ageMax))
        return True
