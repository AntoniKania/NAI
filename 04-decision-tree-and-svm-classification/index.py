
from datasets import load_pima_indian_dataset, load_titanic_dataset, load_survey_dataset
from models import get_decision_tree_model, get_svm_model
from classifiers import invoke_classifiers_with_survey_data, invoke_classifiers_with_titanic_data, invoke_classifiers_with_pima_indians_data

def handle_survey():
    """
    Orchestrates the process of training and evaluating models
    on the job satisfaction survey dataset.
    """
    X, y = load_survey_dataset()
    decision_tree_model = get_decision_tree_model(X, y)
    svm_model = get_svm_model(X, y)
    invoke_classifiers_with_survey_data(decision_tree_model, svm_model)

def handle_diabetis():
    """
    Orchestrates the process of training and evaluating models
    on the diabetis dataset.
    """
    X, y = load_pima_indian_dataset()
    decision_tree_model = get_decision_tree_model(X, y)
    svm_model = get_svm_model(X, y)
    invoke_classifiers_with_pima_indians_data(decision_tree_model, svm_model)

def handle_titanic():
    """
    Orchestrates the process of training and evaluating models
    on the titanic dataset.
    """
    X, y = load_titanic_dataset()
    decision_tree_model = get_decision_tree_model(X, y)
    svm_model = get_svm_model(X, y)
    invoke_classifiers_with_titanic_data(decision_tree_model, svm_model)

handle_survey()
handle_diabetis()
handle_titanic()
