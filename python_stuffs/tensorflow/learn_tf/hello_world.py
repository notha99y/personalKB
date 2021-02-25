'''
x = -1,0,1,2,3,4
y = -3,-1,1,3,5,7

find the mapping y = f(x)

ans: y = 2x - 1
'''


import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense



model = Sequential()
model.add(Dense(units=1, input_shape = [1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

print(model.summary())
x = np.array([-1,0,1,2,3,4])
y = np.array([-3,-1,1,3,5,7])

model.fit(x,y,epochs=500)

print(model.predict([10.0]))