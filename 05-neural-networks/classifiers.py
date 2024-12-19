import numpy as np
import pandas as pd
import tensorflow as tf

def invoke_cats_model_with_sample_data(model):

    class_labels = ["Bengal", "Domestic shorthair", "Maine coon", "Ragdoll", "Siamese"]
    image_path = './resources/random.jpg'
    try:
        # Load the image with the target size matching the model's input shape
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(model.input_shape[1], model.input_shape[2]))

        # Convert the image to a numpy array
        img_array = tf.keras.preprocessing.image.img_to_array(img)

        # Expand dimensions to match the model's expected input (batch size, height, width, channels)
        img_array = np.expand_dims(img_array, axis=0)

        # Normalize the image (optional, depending on your model's preprocessing)
        img_array = img_array / 255.0

        # Invoke the model with the preprocessed image
        predictions = model.predict(img_array)

        if model.output_shape[-1] == 1:  # Binary classification
            predicted_label = class_labels[int(predictions[0] > 0.5)]
        else:  # Multi-class classification
            predicted_label = class_labels[np.argmax(predictions, axis=1)[0]]

        print(predictions)
        print(f"Predicted Class: {predicted_label}")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
        return None



def invoke_cifar10_model_with_sample_data(model, sample_image):
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
