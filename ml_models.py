#Importing the necessary machine learning modules..
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import data as dt
#Implementing the disease predictor class for training, prediction and evaluation..
class DiseasePredictor:
    def __init__(self, model):
        self.model = model
    
    def train(self, X, y):
        self.model.fit(dt.X_train, dt.y_train)
    
    def predict(self, symptoms):
        return self.model.predict([symptoms])
    
    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        return accuracy, conf_matrix

# Instantiate models
dt_model = DiseasePredictor(DecisionTreeClassifier())
rf_model = DiseasePredictor(RandomForestClassifier(n_estimators=100))
knn_model = DiseasePredictor(KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2))
nb_model = DiseasePredictor(GaussianNB())

# Train models
dt_model.train(dt.X_train, dt.y_train)
rf_model.train(dt.X_train, dt.y_train)
knn_model.train(dt.X_train, dt.y_train)
nb_model.train(dt.X_train, dt.y_train)
