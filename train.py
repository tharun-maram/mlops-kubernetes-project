import mlflow
import numpy as np
from sklearn.linear_model import LinearRegression

mlflow.set_tracking_uri("http://13.49.137.41:5000")
mlflow.set_experiment("house-price")

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

with mlflow.start_run():
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("score", model.score(X, y))

print("Training complete 🚀")
