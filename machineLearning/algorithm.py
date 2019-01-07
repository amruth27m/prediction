import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
from sklearn import datasets, metrics
import csv
from copy import deepcopy
from sklearn.externals import joblib


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


data = load_csv('preprocessed_data.csv')
trainset, testset = splitDataset(data, 0.7)

x_train = trainset[:, :-1]
y_train = trainset[:, -1]

x_test = testset[:, :-1]
y_test = testset[:, -1]

# create linear regression object
reg = SVR(kernel='linear', C=1e2, gamma=0.1)

# train the model using the training sets
reg.fit(x_train, y_train)

joblib.dump(reg,'mlModels/svmL.pkl')

# variance score: 1 means perfect prediction
print('Variance score of linear: {}'.format(reg.score(x_test, y_test)))

# mean squared error
print('Mean Squared Error of test data for linear: ', metrics.mean_squared_error(y_test, reg.predict(x_test)))
print('Mean Squared Error of train data for linear: ', metrics.mean_squared_error(y_train, reg.predict(x_train)))

# real and predicted new dose
print('Real new dose : ', y_test)
print('Predicted new dose using linear: ', reg.predict(x_test))

print(reg.support_vectors_)
# plot for residual error of linear

## setting plot style
plt.style.use('fivethirtyeight')

## plotting residual errors in training data
plt.scatter(reg.predict(x_train), reg.predict(x_train) - y_train,
            color="green", s=10, label='Train data')

## plotting residual errors in test data
plt.scatter(reg.predict(x_test), reg.predict(x_test) - y_test,
            color="blue", s=10, label='Test data')

## plotting line for zero residual error
plt.hlines(y=0, xmin=0, xmax=50, linewidth=2)

## plotting legend
plt.legend(loc='upper right')

## plot title
plt.title("Residual errors")

## function to show plot
plt.show()
