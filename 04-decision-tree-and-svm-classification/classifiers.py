import pandas as pd

def invoke_classifiers_with_titanic_data(svm_model, decision_tree_model):
    """
    Uses given machine learning models to make predictions about surviving
    on titanic of two individuals based on their age, class and other
    parameters.

    The function defines two hypothetical individuals (person1 and person2) and
    prints result of predictions

    Parameters:
    svm_model : sklearn.svm.SVC
        A trained support vector classifier model for predicting survivability.
    decision_tree_model : sklearn.tree.DecisionTreeClassifier
        A trained decision tree classifier model for predicting survivability.
    """
    person1 = {
        'Pclass': [3],
        'Sex': [0],
        'Age': [28.0],
        'SibSp': [1],
        'Parch': [1],
        'Fare': [15.2458],
        'Embarked_C': [False],
        'Embarked_Q': [False],
        'Embarked_S': [True]
    }
    person2 = {
        'Pclass': [3],
        'Sex': [1],
        'Age': [28.0],
        'SibSp': [1],
        'Parch': [1],
        'Fare': [15.2458],
        'Embarked_C': [False],
        'Embarked_Q': [False],
        'Embarked_S': [True]
    }
    print("SVC prediction for person1: " + (
        "Will" if svm_model.predict(pd.DataFrame(person1)) == 1 else "Won't") + " survive")
    print("SVC prediction for person2: " + (
        "Will" if svm_model.predict(pd.DataFrame(person2)) == 1 else "Won't") + " survive")
    print("Decision tree prediction for person1: " + (
        "Will" if decision_tree_model.predict(pd.DataFrame(person1)) == 1 else "Won't") + " survive")
    print("Decision tree prediction for person2: " + (
        "Will" if decision_tree_model.predict(pd.DataFrame(person2)) == 1 else "Won't") + " survive")

def invoke_classifiers_with_pima_indians_data(svm_model, decision_tree_model):
    """
    Uses given machine learning models to make predictions about having a
    diabetis of two individuals based on their health data.

    The function defines two hypothetical individuals (person1 and person2) and
    prints result of predictions

    Parameters:
    svm_model : sklearn.svm.SVC
        A trained support vector classifier model for predicting diabetis.
    decision_tree_model : sklearn.tree.DecisionTreeClassifier
        A trained decision tree classifier model for predicting diabetis.
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
    print("Decision tree prediction for person1: " + (
        "Has" if decision_tree_model.predict(pd.DataFrame(person1)) == 1 else "Doesn't have") + " diabetes")
    print("Decision tree prediction for person2: " + (
        "Has" if decision_tree_model.predict(pd.DataFrame(person2)) == 1 else "Doesn't have") + " diabetes")
    print("SVC prediction for person1: " + (
        "Has" if svm_model.predict(pd.DataFrame(person1)) == 1 else "Doesn't have") + " diabetes")
    print("SVC prediction for person2: " + (
        "Has" if svm_model.predict(pd.DataFrame(person2)) == 1 else "Doesn't have") + " diabetes")

def invoke_classifiers_with_survey_data(svm_model, decision_tree_model):
    """
    Uses given machine learning models to make predictions about the happiness
    at work of two individuals based on their survey data.

    The function defines two hypothetical individuals (person1 and person2) and
    prints result of predictions

    Parameters:
    svm_model : sklearn.svm.SVC
        A trained support vector classifier model for predicting happiness.
    decision_tree_model : sklearn.tree.DecisionTreeClassifier
        A trained decision tree classifier model for predicting happiness.
    """
    person1 = {
        'Sex': [0],
        'Age': [29.0],
        'EducationLevel': [4]
    }
    person2 = {
        'Sex': [1],
        'Age': [32.0],
        'EducationLevel': [5]
    }
    print("Decision tree prediction for person1: " + (
        "Is" if decision_tree_model.predict(pd.DataFrame(person1)) == 1 else "Isn't") + " happy")
    print("Decision tree prediction for person2: " + (
        "Is" if decision_tree_model.predict(pd.DataFrame(person2)) == 1 else "Isn't") + " happy")
    print("SVC prediction for person1: " + (
        "Is" if svm_model.predict(pd.DataFrame(person1)) == 1 else "Isn't") + " happy")
    print("SVC prediction for person2: " + (
        "Is" if svm_model.predict(pd.DataFrame(person2)) == 1 else "Isn't") + " happy")
