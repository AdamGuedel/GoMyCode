from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# load the iris datasets
dataset = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target)

# fit a SVC model to the data
model = LinearSVC()
model.fit(X_train, y_train)

# make predictions
expected = y_test
predicted = model.predict(X_test)

#confusion matrix
a=confusion_matrix(expected, predicted)
print(a)

#accuracy
b=accuracy_score(expected, predicted)
print(b)