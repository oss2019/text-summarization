import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.callbacks import CSVLogger

(X_train, Y_train),(X_test, Y_test) = mnist.load_data()

# print(Y_test.shape)
# print(X_train)

X_train = X_train.reshape(X_train.shape[0],784)
X_test = X_test.reshape(X_test.shape[0], 784)


X_train = X_train / 255
X_test = X_test / 255

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)
# print(Y_test.shape[1])

model = Sequential()
model.add(Dense(512,input_dim = 784 ,activation = 'relu'))
model.add(Dense(10,activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

csv_logger = CSVLogger('Shivam_Logs.txt')
model.fit(X_train,Y_train, validation_data=(X_test,Y_test),epochs = 10, batch_size = 100, verbose = 2)

scores = model.evaluate(X_test, Y_test, verbose=0)

print("Accuracy: %.2f%%" % (scores[1]*100))