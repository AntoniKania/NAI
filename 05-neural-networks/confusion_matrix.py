import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def print_confusion_matrix(model, X_test, y_test, num_classes):
    print("num_classes:", num_classes)
    # Get predictions for the test dataset
    y_pred_probabilities = model.predict(X_test)  # Predict probabilities for all samples
    y_pred = (y_pred_probabilities > 0.5).astype(int) 
    
    # Convert true labels (one-hot) to class indices if needed
    if len(y_test.shape) > 1:  # Check if labels are one-hot encoded
        y_true = np.argmax(y_test, axis=1)
    else:
        y_true = y_test

    print("y_test shape:", y_test.shape)
    print("y_true shape:", y_true.shape)

    print("y_pred_probabilities shape:", y_pred_probabilities.shape)
    print("y_pred shape:", y_pred.shape)
    # Create the confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    labels = ['Class 0', 'Class 1']

    # Display the confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    print("cmap=plt.cm.Blues:", plt.cm.Blues)
    disp.plot(cmap=plt.cm.Blues, xticks_rotation="vertical")
    plt.title("Confusion Matrix")
    plt.show()