from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def print_confusion_matrix(model, X_test, y_test):
    """
        Creates the confusion matrix and display it

        Parameters:
            model (tf.keras.Model): Trained model that is used for predictions.
            X_test (numpy.ndarray): Test input data, a 2D array with shape (num_samples, num_features).
            y_test (numpy.ndarray): Labels, either a 1D array of integers (binary labels).
    """
    y_pred_probabilities = model.predict(X_test)  # Predict probabilities for all samples
    y_pred = (y_pred_probabilities > 0.5).astype(int) 
    y_true = y_test

    cm = confusion_matrix(y_true, y_pred)
    labels = ['Healthy', 'Unhealthy']

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    print("cmap=plt.cm.Blues:", plt.cm.Blues)
    disp.plot(cmap=plt.cm.Blues, xticks_rotation="vertical")
    plt.title("Confusion Matrix")
    plt.show()