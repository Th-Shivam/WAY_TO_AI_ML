import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. LOAD AND PREPARE THE DATA
# ==========================================
print("Loading California Housing dataset...")
california = fetch_california_housing(as_frame=True)

# Create a pandas DataFrame
df = california.frame

# Quick look at the features we are working with
# Features include: MedInc (Income), HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
print("\nDataset Sample:")
print(df.head())

# Split data into Features (X) and Target (y)
# Target (MedHouseVal) is the median house value in hundreds of thousands of dollars ($100,000s)
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

# ==========================================
# 2. SPLIT INTO TRAIN AND TEST SETS
# ==========================================
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. FEATURE SCALING
# ==========================================
# Scaling helps models process data more efficiently
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 4. TRAIN THE MODEL
# ==========================================
print("\nTraining the Random Forest model (this might take a few seconds)...")
# Using 100 decision trees
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)
print("Training complete!")

# ==========================================
# 5. EVALUATE THE MODEL
# ==========================================
# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Performance Metrics ---")
print(f"Mean Absolute Error (MAE): ${mae * 100,000:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse * 100,000:,.2f}")
print(f"R-squared (Accuracy Score): {r2:.4f} (or {r2*100:.2f}%)")

# ==========================================
# 6. PREDICT ON A NEW, CUSTOM HOUSE
# ==========================================
print("\nMaking a prediction for a custom house...")

# Example custom house data based on the dataset features:
# [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]
custom_house = np.array([[6.5, 15.0, 6.0, 1.0, 1200.0, 3.0, 34.05, -118.24]])

# Scale the custom input using the SAME scaler
custom_house_scaled = scaler.transform(custom_house)

# Predict
predicted_val = model.predict(custom_house_scaled)
print(f"Predicted Median House Value: ${predicted_val[0] * 100,000:,.2f}")
