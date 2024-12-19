import tensorflow as tf
import sys

from datasets import fashion_mnist, pima, cifar10 
from confusion_matrix import print_confusion_matrix
from models import get_trained_pima_model, get_trained_cifar10_model
from classifiers import invoke_pima_model_with_sample_data, invoke_cifar10_model_with_sample_data

if __name__ == '__main__':
    dataset_type = sys.argv[1]
    model_filename = f'{dataset_type}_model.keras'

    if dataset_type == 'fashion_mnist':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = fashion_mnist()
    elif dataset_type == 'pima':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = pima()
        model = get_trained_pima_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        print_confusion_matrix(model, X_test, y_test)
        invoke_pima_model_with_sample_data(model)
        
    elif dataset_type == 'cifar10':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = cifar10()
        # y_train = tf.keras.utils.to_categorical(y_train, num_classes)
        # y_test = tf.keras.utils.to_categorical(y_test, num_classes)
        model = get_trained_cifar10_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        invoke_cifar10_model_with_sample_data(model, X_test[0:1])
    else:
        raise ValueError("Unknown dataset type. Use 'fashion_mnist', 'pima', or 'cifar10'.")

    if dataset_type in ['pima', 'cifar10']:
        print(f"Model training and evaluation completed for {dataset_type} dataset.")
    else:
        image_filename = sys.argv[2]
        image = tf.keras.utils.load_img(image_filename, target_size=(28, 28), color_mode='grayscale')
        input_arr = tf.keras.utils.img_to_array(image) / 255.0
        input_arr = input_arr.reshape((1, 28, 28, 1))
        predictions = model.predict(input_arr)
        print(predictions)
