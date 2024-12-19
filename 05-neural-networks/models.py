import tensorflow as tf

def get_trained_cats_breeds_model(input_shape, num_classes, X_train, y_train):
    """
    Create and train a model for the Cats Breeds dataset.

    Args:
        input_shape (tuple): Shape of the input data (height, width, channels).
        num_classes (int): Number of classes (output categories).
        X_train (ndarray): Training data.
        y_train (ndarray): Training labels (one-hot encoded).

    Returns:
        tf.keras.Model: A trained CNN model for Cats breed classification.
    """
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax' if num_classes > 1 else 'sigmoid')
    ])

    loss = 'categorical_crossentropy' if len(y_train.shape) == 2 else 'sparse_categorical_crossentropy'
    
    model.compile(optimizer='adam',
                  loss=loss,
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    return model

def get_trained_mnist_model(input_shape, num_classes, X_train, y_train):
    """
    Build, train, and return a Convolutional Neural Network (CNN) model for MNIST fashion database

    Parameters:
        input_shape (tuple): The shape of the input data, e.g., (28, 28, 1) for MNIST grayscale images.
        num_classes (int): The number of output classes
        X_train (numpy.ndarray): Training input data
        y_train (numpy.ndarray): Training labels, a 1D array of integers corresponding to class indices.

    Returns:
        tf.keras.Model: A trained CNN model for MNIST classification.
    """
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2, verbose=1)
    return model


def get_trained_cifar10_model(input_shape, num_classes, X_train, y_train):
    """
    Build, train, and return a Convolutional Neural Network (CNN) model for the CIFAR-10 dataset.

    Parameters:
        input_shape (tuple): The shape of the input data, e.g., (32, 32, 3) for CIFAR-10 images.
        num_classes (int): The number of output classes, 10 for CIFAR-10.
        X_train (numpy.ndarray): Training input data, a 4D array with shape (num_samples, height, width, channels).
        y_train (numpy.ndarray): Training labels, either a 2D array (one-hot encoded) or a 1D array (integer class labels).

    Returns:
        tf.keras.Model: A trained CNN model for CIFAR-10 classification.
    """
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


def get_trained_pima_model(input_shape, num_classes, X_train, y_train):
    """
    Build, train, and return a Convolutional Neural Network (CNN) model for pima diabetes database
    
    Parameters:
        input_shape (tuple): The shape of the input data, e.g., (8,) for the 8 features in the Pima dataset.
        num_classes (int): The number of output classes. 1 for binary classification.
        X_train (numpy.ndarray): Training input data, a 2D array with shape (num_samples, num_features).
        y_train (numpy.ndarray): Training labels, either a 1D array of integers for class indices or binary labels.

    Returns:
        tf.keras.Model: A trained neural network model for the Pima diabetes dataset.
    """
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
