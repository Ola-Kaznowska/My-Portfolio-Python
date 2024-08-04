import tensorflow as tf
import tensorflow.python.keras.layers
from tensorflow.keras.models import Sequential

img_height, img_width = 32, 32
batch_size = 128
data_dir = "trainingSet"

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)

resnet_model = Sequential()

pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                   input_shape=(img_height, img_width, 3),
                   pooling='max', classes=10,
                   weights='imagenet')
for layer in pretrained_model.layers:
        layer.trainable=False

resnet_model.add(pretrained_model)
resnet_model.add(tensorflow.keras.layers.Flatten())
resnet_model.add(tensorflow.keras.layers.Dense(512, activation='relu'))
resnet_model.add(tensorflow.keras.layers.Dense(10, activation='softmax'))

resnet_model.build([None,32, 32, 3])
resnet_model.summary()

resnet_model.compile(optimizer="adam",loss='sparse_categorical_crossentropy',metrics=['accuracy'])
history = resnet_model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=10
)

# Save the model
resnet_model.save('tl2.h5')