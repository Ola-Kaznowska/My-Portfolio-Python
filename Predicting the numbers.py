import os
import cv2 as cv
import numpy as np
import tensorflow as tf
import random

SIZE = 28
DIRECTORY = "trainingSet"
CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# def load_data():
#     training_data = []
#     for category in CATEGORIES:
#         path = os.path.join(DIRECTORY, category)
#         class_num = CATEGORIES.index(category)
#         for image in os.listdir(path):
#             try:
#                 image_array = cv.imread(os.path.join(path, image), cv.IMREAD_GRAYSCALE)
#                 image_array = cv.resize(image_array, (SIZE, SIZE))
#                 training_data.append([image_array, class_num])
#             except:
#                 pass
#         random.shuffle(training_data)
#     return training_data


# training_data = load_data()
# images = []
# labels = []

# for image,label in training_data:
#     images.append(image)
#     labels.append(label)

# print(labels[:10])
# images = np.array(images).reshape(-1, SIZE, SIZE, 1)
# labels = np.array(labels)

# model = tf.keras.models.Sequential([
#     tf.keras.layers.Rescaling(1./255, input_shape=(SIZE, SIZE, 1)),
#     tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
#     tf.keras.layers.MaxPooling2D(2, 2),
#     tf.keras.layers.Dropout(0.2),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])

# model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# history = model.fit(images, labels, batch_size=256, epochs=10, validation_split=0.2)
# model.save("CNN.h5")

model = tf.keras.models.load_model("CNN.h5")
image_array = cv.imread("num.png", cv.IMREAD_GRAYSCALE)
image_array = cv.resize(image_array,(SIZE,SIZE))
image_array = np.array(image_array).reshape(-1,SIZE,SIZE, 1)
prediction = model.predict(image_array)
print(np.argmax(prediction))


model = tf.keras.models.load_model("CNN.h5")
image = cv.imread("num.png", cv.IMREAD_GRAYSCALE)
image = cv.resize(image, (SIZE, SIZE))
image = np.array(image).reshape(-1, SIZE, SIZE, 1)
prediction = model.predict(image)
print(np.argmax(prediction))

print(prediction)