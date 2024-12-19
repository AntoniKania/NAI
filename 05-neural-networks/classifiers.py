import numpy as np
import pandas as pd

def invoke_cifar10_model_with_sample_data(model, sample_image):
    predictions = model.predict(sample_image)
    predicted_class = np.argmax(predictions)
    print(predictions)
    print(f"Predicted Class: {predicted_class}")

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
