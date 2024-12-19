import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import kagglehub
import os
from PIL import Image


def cats_breeds(img_size=(128, 128), batch_size=32):
    """Load and preprocess the Cats breed dataset."""
    img_size=(128, 128)
    data = kagglehub.dataset_download("yapwh1208/cats-breed-dataset")
    data_dir = data + '/cat_v1'
    # data_dir = '/root/.cache/kagglehub/datasets/yapwh1208/cats-breed-dataset/versions/1/cat_v1' - use for not downoading each time data
    if not os.path.exists(data_dir):
        raise ValueError(f"Dataset directory '{data_dir}' does not exist.")

    X = []
    y = []
    class_names = []
    
    # Read images and labels from the directory structure
    for class_idx, class_name in enumerate(sorted(os.listdir(data_dir))):
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            class_names.append(class_name)
            for img_file in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_file)
                try:
                    # Load image, resize, and normalize pixel values
                    img = Image.open(img_path).convert('RGB').resize(img_size)
                    X.append(np.array(img) / 255.0)
                    y.append(class_idx)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
    
    X = np.array(X, dtype='float32')
    y = np.array(y, dtype='int')
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    num_classes = len(class_names)
    y_train = tf.keras.utils.to_categorical(y_train, num_classes=num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes=num_classes)

    input_shape = (img_size[0], img_size[1], 3)  # RGB images

    return (X_train, y_train), (X_test, y_test), input_shape, num_classes

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
    num_classes = 10
    return (X_train, y_train), (X_test, y_test), input_shape, num_classes
