from utils.constants import AgeConstants, GenderConstants, ProcedureConstants, INRConstants


class PatientAgeValidator:
    @staticmethod
    def validate(age):
        age = int(age)
        if age <= AgeConstants.AgeMin.value  or age > AgeConstants.AgeMax.value:
            raise ValueError("age must be between %d and %d" % (AgeConstants.AgeMin
                                                                , AgeConstants.AgeMax))
        return True


class PatientGenderValidator:
    @staticmethod
    def validate(gender):
        if gender not in GenderConstants.__members__:
            raise ValueError("Unidentified gender %s" %gender)
        return True


class PatientProcedureValidator:
    @staticmethod
    def validate(procedure):
        if procedure not in ProcedureConstants.__members__:
            raise ValueError("Undefined procedure %s" %procedure)
        return True


class PatientOldINRValueValidator:
    @staticmethod
    def validate(oldINRValue):
        oldINRValue = float(oldINRValue)
        if oldINRValue <= INRConstants.INRMin.value or oldINRValue > INRConstants.INRMax.value:
            raise ValueError("Old INR Value %f out of limit" %oldINRValue)
        return True

class PatientNewINRValueValidator:
    @staticmethod
    def validate(newINRValue):
        newINRValue = float(newINRValue)
        if newINRValue <= INRConstants.INRMin.value or newINRValue > INRConstants.INRMax.value:
            raise ValueError("New INR Value %f out of limit" %newINRValue)
        return True

class PatientOldDoseValidator:
    @staticmethod
    def validate(oldDose):
        return True

argValidators = {
    "age": PatientAgeValidator,
    "gender": PatientGenderValidator,
    "procedure": PatientProcedureValidator,
    "oldINRValue": PatientOldINRValueValidator,
    "newINRValue": PatientNewINRValueValidator,
    "oldDose": PatientOldDoseValidator
}


def validateArgs(args):
    if set(args.keys()) != set(argValidators.keys()):
        raise ValueError("Missing Argument")
    for key,value in args.items():
        argValidators[key].validate(value)
    return True


