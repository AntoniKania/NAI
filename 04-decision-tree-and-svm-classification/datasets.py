import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def load_pima_indian_dataset():
    """
    Loads and preprocesses the Pima Indians Diabetes dataset for machine learning tasks.

    The function performs the following steps:
    1. Loads the dataset from file.
    2. Identifies features that may have missing or zero values ('Glucose', 'BloodPressure', 
       'SkinThickness', 'Insulin', 'BMI') and replaces zero values with NaN.
    3. Applies median imputation to handle missing values in the identified features.

    Returns:
    X : pandas.DataFrame
        The feature set, containing all columns except 'Outcome'.
    y : pandas.Series
        The target variable, indicating outcome (1 for have diabetis, 0 for not have diabetis).
    """
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
               'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    data = pd.read_csv("resources/pima-indians-diabetes.csv", names=columns)

    features_with_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    data[features_with_missing] = data[features_with_missing].replace(0, np.nan)
    imputer = SimpleImputer(strategy='median')
    data[features_with_missing] = imputer.fit_transform(data[features_with_missing])
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    return X, y

def load_titanic_dataset():
    """
    Loads and preprocesses the Titanic dataset for machine learning tasks.

    The function performs the following steps:
    1. Loads the dataset from file.
    2. Drops unnecessary columns.
    3. Fills missing values in the 'Age' column with the median age.
    4. Fills missing values in the 'Embarked' column with the most common embarkation point (mode).
    5. Encodes the 'Sex' column as binary (0 for 'male', 1 for 'female').
    6. Converts the 'Embarked' column to dummy variables using one-hot encoding.

    Returns:
    X : pandas.DataFrame
        The feature set, containing all columns except 'Survived'.
    y : pandas.Series
        The target variable, indicating survival (1 for survived, 0 for did not survive).
    """
    data = pd.read_csv('resources/titanic.csv')
    data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data = pd.get_dummies(data, columns=['Embarked']) # hot-one encoding

    X = data.drop('Survived', axis=1)
    y = data['Survived']
    return X, y

def load_survey_dataset():
    """
    Loads and preprocesses the job satisfaction survey dataset for machine learning tasks.

    The function performs the following steps:
    1. Loads the dataset from file.
    2. Drops the 'SurveyedId' column.
    3. Encodes the 'Sex' column as binary values (0 for 'male', 1 for 'female').

    Returns:
    X : pandas.DataFrame
        The feature set, containing all columns except 'Satisfied'.
    y : pandas.Series
        The target variable, indicating satisfaction (1 for satisfied, 0 for not satisfied).
    """
     
    data = pd.read_csv('resources/job-satisfaction-survey.csv')
    data = data.drop(['SurveyedId'], axis=1)
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

    X = data.drop('Satisfied', axis=1)
    print(X)
    y = data['Satisfied']
    return X, y
