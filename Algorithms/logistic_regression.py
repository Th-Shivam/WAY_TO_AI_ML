import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification


X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                          n_informative=2, n_clusters_per_class=1, random_state=42)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")


print(f"First 5 predictions: {predictions[:5]}")
print(f"First 5 actual values: {y_test[:5]}")
