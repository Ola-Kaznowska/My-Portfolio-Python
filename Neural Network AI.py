import numpy as np   
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard

name = "linear_function"
TensorBoard = TensorBoard(log_dir=f"logs/{name}")


layer = Dense(units=1, input_shape=[1])
model = Sequential([layer])
model.compile(optimizer="sgd", loss="mean_squared_error", metrics=["accuracy"])


xs = np.array([-2, -1, 0, 1, 2, 3])
xy = np.array([-13, -8, 3, 2, 7, 12])



model.fit(xs, xy, epochs=100, callbacks=[TensorBoard])

print(model.predict(np.arry([10], dtype=int)))
print(layer.get_weights())


