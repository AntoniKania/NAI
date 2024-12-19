import tensorflow as tf

def get_trained_cifar10_model(input_shape, num_classes, X_train, y_train):
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


def get_trained_pima_model(input_shape, num_classes, X_train, y_train):
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
