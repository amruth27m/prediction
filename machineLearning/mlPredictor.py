from sklearn.externals import joblib
import csv
from copy import deepcopy
import numpy as np
from utils.constants import GenderConstants,ProcedureConstants

def load_csv(filename):
    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    data = np.array(x).astype('float')
    return data


def splitDataset(dataset, splitratio):
    trainsize = int(np.round(dataset.shape[0] * splitratio))
    trainset = np.zeros((trainsize, dataset.shape[1]))  # array to store the training set.
    testset = deepcopy(dataset)  # create a copy of the dataset in test set.
    for numsamples in range(trainsize):
        indx = np.random.randint(0, testset.shape[0])  # random index generation
        trainset[numsamples, :] = testset[indx, :]  # adding the randomly selected data vector to the training set
        testset = np.delete(testset, indx, axis=0)  # delete the selected observation from the test set.
    return trainset, testset

def parseArgs(args):
    resultList = []
    result = []
    result.append(GenderConstants[args['gender']].value)
    result.append(ProcedureConstants[args['procedure']].value)
    result.append(args['age'])
    result.append(args['oldINRValue'])
    result.append(args['newINRValue'])
    result.append(args['oldDose'])
    resultList.append(result)
    return  resultList

def predict(args):
    print("Reached MLPredictor")
    model = joblib.load('machineLearning/mlModels/svmL.pkl')
    x = parseArgs(args)
    # x = [[0. ,   0. ,  53.  ,  3.55 , 3.28 ,10.]]
    print("Reached data")
    # real and predicted new dose
    result = model.predict(x)
    print('Predicted new dose using linear: ', model.predict(x))
    return result

