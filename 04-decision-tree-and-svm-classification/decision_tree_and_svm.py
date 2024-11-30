import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer



def load_pima_indian_dataset():
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
    data = pd.read_csv('resources/titanic.csv')
    data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data = pd.get_dummies(data, columns=['Embarked'], drop_first=True) # hot-one encoding

    X = data.drop('Survived', axis=1)
    y = data['Survived']
    return X, y

# X, y = load_pima_indian_dataset()
X, y = load_titanic_dataset()

# sns.pairplot(data, hue='Outcome')
# plt.show()

# plt.figure(figsize=(10, 8))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

decision_tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
decision_tree_model.fit(X_train, y_train)
dt_predicted = decision_tree_model.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predicted))
print(classification_report(y_test, dt_predicted))

plt.figure(figsize=(12, 8))
plot_tree(decision_tree_model, feature_names=X.columns, filled=True)
plt.show()

svm_model = SVC(kernel='linear', random_state=42)
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
