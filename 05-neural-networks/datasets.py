import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

def fashion_mnist():
    """Load and preprocess the Fashion-MNIST dataset."""
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    input_shape = (28, 28, 1) # 28x28 pixels, 1 channel (black&white picture)
    num_classes = 10  # 10 categories of clothing in the dataset
    return (x_train, y_train), (x_test, y_test), input_shape, num_classes


def pima():
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


def cifar10():
    """Load and preprocess the CIFAR-10 dataset."""
    cifar10 = tf.keras.datasets.cifar10
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    X_train, X_test = X_train / 255.0, X_test / 255.0
    y_train, y_test = y_train.flatten(), y_test.flatten()
    input_shape = (32, 32, 3)  # 32x32px RGB
    num_classes = 10  # 10 classes in CIFAR-10
    return (X_train, y_train), (X_test, y_test), input_shape, num_classes
