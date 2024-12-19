import numpy as np
import pandas as pd
import tensorflow as tf

def invoke_cats_model_with_sample_data(model):
    """
    Uses given machine learning models to make predictions of cat breed
    on the image. Loads hard-coded image from resources folder. Preprocess 
    it

    Prints result of prediction

    Parameters:
    model : tf.keras.Model
        A trained neural network model for predicting cat breed.
    """
    class_labels = ["Bengal", "Domestic shorthair", "Maine coon", "Ragdoll", "Siamese"]
    image_path = './resources/random.jpg'
    try:
        #pre-procesing image
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(model.input_shape[1], model.input_shape[2]))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        predictions = model.predict(img_array)
        predicted_label = class_labels[np.argmax(predictions, axis=1)[0]]

        print(predictions)
        print(f"Predicted Class: {predicted_label}")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
        return None

def invoke_cifar10_model_with_sample_data(model, sample_image):
    """
    Uses given machine learning models to make predictions of what is
    on the image.

    Prints result of prediction

    Parameters:
    model : tf.keras.Model
        A trained neural network model for predicting diabetes.
    """
    cifar10_labels = [
        "airplane", "automobile", "bird", "cat", "deer", 
        "dog", "frog", "horse", "ship", "truck"
    ]   
    predictions = model.predict(sample_image)
    predicted_class = np.argmax(predictions)
    print(predictions)
    print(f"Predicted Class: {cifar10_labels[predicted_class]}")

def invoke_pima_model_with_sample_data(model):
    """
    Uses given machine learning models to make predictions about having a
    diabetes of two individuals based on their health data.

    The function defines two hypothetical individuals (person1 and person2) and
    prints result of predictions

    Parameters:
    model : tf.keras.Model
        A trained neural network model for predicting diabetes.
    """
    person1 = {
        'Pregnancies': [2],
        'Glucose': [84.0],
        'BloodPressure': [72.0],
        'SkinThickness': [35.0],
        'Insulin': [0.0],
        'BMI': [32.3],
        'DiabetesPedigreeFunction': [0.304],
        'Age': [21]
    }
    person2 = {
        'Pregnancies': [2],
        'Glucose': [140.0],
        'BloodPressure': [72.0],
        'SkinThickness': [35.0],
        'Insulin': [270.0],
        'BMI': [38.0],
        'DiabetesPedigreeFunction': [0.304],
        'Age': [51]
    }
    print("Neural network model prediction for person1: " + (
        "Has" if model.predict(pd.DataFrame(person1)) == 1 else "Doesn't have") + " diabetes")
    print("Neural network model prediction for person2: " + (
        "Has" if model.predict(pd.DataFrame(person2)) == 1 else "Doesn't have") + " diabetes")
