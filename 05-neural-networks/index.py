import tensorflow as tf
import sys
import numpy as np

from datasets import fashion_mnist, pima, cifar10, cats_breeds
from confusion_matrix import print_confusion_matrix
from models import get_trained_pima_model, get_trained_cifar10_model, get_trained_mnist_model, get_trained_cats_breeds_model
from classifiers import invoke_pima_model_with_sample_data, invoke_cifar10_model_with_sample_data, invoke_cats_model_with_sample_data
from collections import Counter

if __name__ == '__main__':
    """
    Orchestrates the process of training and evaluating neuronal networks
    on multiple dataset.
    
    Selection by sys arg, described in README.md. In 
    confusion_matrix implementation in pima datasets.
    """
    dataset_type = sys.argv[1]
    model_filename = f'{dataset_type}_model.keras'

    if dataset_type == 'fashion_mnist':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = fashion_mnist()
        model = get_trained_mnist_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)

    elif dataset_type == 'cats':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = cats_breeds()
        print(Counter(np.argmax(y_train, axis=1)))
        model = get_trained_cats_breeds_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        invoke_cats_model_with_sample_data(model)

    elif dataset_type == 'pima':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = pima()
        model = get_trained_pima_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        print_confusion_matrix(model, X_test, y_test)
        invoke_pima_model_with_sample_data(model)
        
    elif dataset_type == 'cifar10':
        (X_train, y_train), (X_test, y_test), input_shape, num_classes = cifar10()
        model = get_trained_cifar10_model(input_shape, num_classes, X_train, y_train)
        model.save(model_filename)
        model.evaluate(X_test, y_test)
        invoke_cifar10_model_with_sample_data(model, X_test[0:1])
    else:
        raise ValueError("Unknown dataset type. Use 'fashion_mnist', 'pima', 'cats', or 'cifar10'.")

    print(f"Model training and evaluation completed for {dataset_type} dataset.")
