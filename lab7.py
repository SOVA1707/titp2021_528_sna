#2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Activation
import sklearn
import pandas as pd

data = pd.read_table('data7.txt', names=['val','var'], decimal='.', delimiter=',')

x_files = data['val'].to_numpy()

y_files = data['var'].to_numpy()

x_y_shuffle = np.ones((2, len(x_files)))

x_y_shuffle[0] = x_files.copy()

x_y_shuffle[1] = y_files.copy()

x_y_shuffle = x_y_shuffle.T

np.random.shuffle(x_y_shuffle)

x_y_shuffle = x_y_shuffle.T

x = x_y_shuffle[0]

y = x_y_shuffle[1]

x_training1 = np.split(x, [0, (len(x)//5)*4])

y_training1 = np.split(y, [0, (len(x)//5)*4])

x_training = x_training1[1]

y_training = y_training1[1]

x_test = x_training1[2]

y_test = y_training1[2]

print(x_training)
print(y_training)
print(x_test)
print(y_test)

model = Sequential()

model.add(Dense(1024,input_shape=(1,), input_dim=1, activation='tanh'))
model.add(Dense(1024,input_shape=(1,), input_dim=1, activation='tanh'))
model.add(Dense(1024,input_shape=(1,), input_dim=1, activation='tanh'))

#model.add(Dense(1024, activation='tanh'))


model.add(Dense(1, activation='elu'))

model.compile(loss='mean_squared_error', optimizer='adam') #выбран оптимизатор adam

model.fit(x, y, epochs=5000, batch_size=500, verbose=0)

plt.scatter(x_training, y_training)

plt.scatter(x_test, y_test)

xx=np.arange(min(x_files), max(x_files), 0.1)

plt.scatter(xx, model.predict(xx),s=1)

print (mean_squared_error (y_test, model.predict(x_test)))

plt.show()
