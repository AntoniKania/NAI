import sys
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
import seaborn as sns

def create_svm_model():
    """
    Creates an SVM (Support Vector Machine) model with a kernel specified via command-line arguments.

    The function performs the following:
    1. Checks if a kernel type is provided as a command-line argument (`sys.argv[1]`).
    - If a kernel is specified, it uses that kernel and prints the chosen kernel type.
    - If no kernel is provided, defaults to the 'linear' kernel and prints a default notification.
    2. Returns an instance of the `SVC` classifier with the selected kernel and a fixed random state.
    Returns:
    svm_model : sklearn.svm.SVC
        An SVM classifier initialized with the specified or default kernel.
    """
    kernel = "linear"
    if len(sys.argv) > 1:
        kernel = sys.argv[1]
        print(f"Using: {kernel} kernel")
    else:
        print("No metric provided, linear")
    return SVC(kernel=kernel, random_state=42)

def get_decision_tree_model(X, y):
    """
    Trains a decision tree classifier on the given dataset and evaluates its performance.

    The function performs the following steps:
    1. Splits the dataset into training and testing sets.
    2. Trains a decision tree classifier with a maximum depth of 4 and a fixed random state for reproducibility.
    3. Predicts outcomes on the test set and evaluates the model using:
        - Accuracy score.
        - Classification report (precision, recall, F1-score).
    4. Visualizes the decision tree.

    Parameters:
    X : pandas.DataFrame
        Feature set used to train the decision tree classifier.
    y : pandas.Series
        Target variable used to train the decision tree classifier.

    Returns:
    decision_tree_model : sklearn.tree.DecisionTreeClassifier
        The trained decision tree classifier.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    decision_tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
    decision_tree_model.fit(X_train, y_train)
    dt_predicted = decision_tree_model.predict(X_test)
    print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predicted))
    print(classification_report(y_test, dt_predicted))
    plt.figure(figsize=(12, 8))
    plot_tree(decision_tree_model, feature_names=X.columns, filled=True)
    plt.show()
    return decision_tree_model

def get_svm_model(X, y):
    """
    Trains a Support Vector Machine (SVM) classifier on the given dataset and evaluates its performance.

    The function performs the following steps:
    1. Splits the dataset into training and testing sets.
    2. Trains a linear SVM model on the training set.
    3. Predicts outcomes on the test set and evaluates the model using:
        - Accuracy score.
        - Classification report (precision, recall, F1-score).
        - Confusion matrix, visualized as a heatmap.

    Parameters:
    -----------
    X : pandas.DataFrame
        Feature set used to train the decision tree classifier.
    y : pandas.Series
        Target variable used to train the decision tree classifier.

    Returns:
    --------
    svm_model : sklearn.svm.SVC
        The trained SVM classifier.
    """
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svm_model = create_svm_model()
    svm_model.fit(X_train, y_train)
    y_pred_svm = svm_model.predict(X_test)

    print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
    print(classification_report(y_test, y_pred_svm))
    conf_matrix = confusion_matrix(y_test, y_pred_svm)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('SVM Confusion Matrix')
    plt.show()
    return svm_model
