# model.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import cv2
import numpy as np

def create_cnn_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_face(model, image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (64, 64))
    image_array = np.expand_dims(image_resized, axis=0) / 255.0
    prediction = model.predict(image_array)[0][0]
    return prediction > 0.5

# if __name__ == "__main__":
#     # Create and train the model here
#     model = create_cnn_model()

#     # Assuming you have your dataset ready
#     train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
#     train_generator = train_datagen.flow_from_directory(
#         'path_to_dataset', 
#         target_size=(64, 64), 
#         batch_size=32, 
#         class_mode='binary', 
#         subset='training'
#     )
#     validation_generator = train_datagen.flow_from_directory(
#         'path_to_dataset', 
#         target_size=(64, 64), 
#         batch_size=32, 
#         class_mode='binary', 
#         subset='validation'
#     )

#     model.fit(
#         train_generator,
#         steps_per_epoch=train_generator.samples // train_generator.batch_size,
#         validation_data=validation_generator,
#         validation_steps=validation_generator.samples // validation_generator.batch_size,
#         epochs=10
#     )

#     model.save('face_detection_model.h5')