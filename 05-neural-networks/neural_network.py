import tensorflow as tf
import numpy as np
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def load_fashion_mnist():
    """Load and preprocess the Fashion-MNIST dataset."""
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    input_shape = (28, 28, 1) # 28x28 pixels, 1 channel (black&white picture)
    num_classes = 10  # 10 categories of clothing in the dataset
    return (x_train, y_train), (x_test, y_test), input_shape, num_classes


def load_pima():
    """Load and preprocess the Pima Indians Diabetes dataset."""
    csv_path = "resources/pima-indians-diabetes.csv"
    data = pd.read_csv(csv_path)
    x = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42
    )
    input_shape = (x.shape[1],)  # Number of features
    num_classes = 1  # Binary classification
    return (x_train, y_train), (x_test, y_test), input_shape, num_classes


def load_cifar10():
    """Load and preprocess the CIFAR-10 dataset."""
    cifar10 = tf.keras.datasets.cifar10
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    X_train, X_test = X_train / 255.0, X_test / 255.0
    y_train, y_test = y_train.flatten(), y_test.flatten()
    input_shape = (32, 32, 3)  # 32x32px RGB
    num_classes = 10  # 10 classes in CIFAR-10
    return (X_train, y_train), (X_test, y_test), input_shape, num_classes

def create_and_train_model_cifar10(input_shape, num_classes, X_train, y_train):
    """Create and train a model with the given input shape and output classes."""
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax' if num_classes > 1 else 'sigmoid')
    ])

    loss = 'categorical_crossentropy' if len(y_train.shape) == 2 else 'sparse_categorical_crossentropy'
    
    model.compile(optimizer='adam',
                  loss=loss,
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    return model


def create_and_train_model(input_shape, num_classes, X_train, y_train):
    """Create and train a model with the given input shape and output classes."""
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax' if num_classes > 1 else 'sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy' if num_classes > 1 else 'binary_crossentropy',
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10)
    return model

def invoke_model_with_cifar10_data(model, sample_image):
    predictions = model.predict(sample_image)
    predicted_class = np.argmax(predictions)
    print(predictions)
    print(f"Predicted Class: {predicted_class}")

def invoke_model_with_pima_indians_data(model):
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


if __name__ == '__main__':
    dataset_type = sys.argv[1]
    model_filename = f'{dataset_type}_model.keras'

    if dataset_type == 'fashion_mnist':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = load_fashion_mnist()
    elif dataset_type == 'pima':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = load_pima()
        model = create_and_train_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        invoke_model_with_pima_indians_data(model)
    elif dataset_type == 'cifar10':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = load_cifar10()
        y_train = tf.keras.utils.to_categorical(y_train, num_classes)
        y_test = tf.keras.utils.to_categorical(y_test, num_classes)
        model = create_and_train_model_cifar10(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        invoke_model_with_cifar10_data(model, X_test[0:1])
    else:
        raise ValueError("Unknown dataset type. Use 'fashion_mnist', 'pima', or 'cifar10'.")

    # Convert labels to one-hot encoding for classification datasets
        

    # if os.path.isfile(model_filename):
    #     model = tf.keras.models.load_model(model_filename)
    # else:
    #     model = create_and_train_model(input_shape, num_classes, X_train, y_train)
    #     model.save(model_filename)


   

    if dataset_type in ['pima', 'cifar10']:
        print(f"Model training and evaluation completed for {dataset_type} dataset.")
    else:
        image_filename = sys.argv[2]
        image = tf.keras.utils.load_img(image_filename, target_size=(28, 28), color_mode='grayscale')
        input_arr = tf.keras.utils.img_to_array(image) / 255.0
        input_arr = input_arr.reshape((1, 28, 28, 1))
        predictions = model.predict(input_arr)
        print(predictions)
