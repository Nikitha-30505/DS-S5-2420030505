
# Regression Models for Predictive Analytics
# House Price Prediction and Purchase Classification

import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

# Linear Regression
print("----- Linear Regression -----")

X = np.array([[1000], [1200], [1500], [1800], [2000]])
y = np.array([50, 55, 65, 80, 90])

model = LinearRegression()
model.fit(X, y)

price = model.predict([[1700]])

print("House Sizes:", X.flatten())
print("House Prices:", y)
print("Predicted Price for 1700 sq.ft:", price[0])

# Logistic Regression
print("\n----- Logistic Regression -----")

X2 = np.array([[40], [50], [60], [70], [80], [90]])
y2 = np.array([0, 0, 0, 1, 1, 1])

model2 = LogisticRegression()
model2.fit(X2, y2)

test_price = np.array([[75]])
prediction = model2.predict(test_price)
probability = model2.predict_proba(test_price)

print("Test House Price:", test_price[0][0])
print("Purchase Prediction:", prediction[0])
print("Prediction Probabilities:", np.round(probability, 2))
