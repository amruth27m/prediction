import enum

PATIENT_DATA_PARAMETERS = ["gender","procedure","age","oldINRValue","newINRValue","oldDose"]

class AgeConstants(enum.Enum):
    AgeMin = 1
    AgeMax = 120


class GenderConstants(enum.Enum):
    Male = 0
    Female = 1
    Other = 2


class ProcedureConstants(enum.Enum):
    MVR = 0
    AVR = 1
    DVR = 2
    AF = 3


class INRConstants(enum.Enum):
    INRMin = 2.0
    INRMax = 6.0