import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from Clustering import kmeans_least_confidence_samples

# Load the data
df = pd.read_excel('Data/compressed_data_with_noise.xlsx')
data = df.iloc[:, :3].to_numpy()  # Only use the first three columns for clustering

indices, samples = kmeans_least_confidence_samples(data)

# Split data into features (X) and labels (y)
X = df.iloc[:, :3]
y = df.iloc[:, 3]

# Split the dataset into a small initial training set, a set for informative samples, and a test set
X_train_small, X_test, y_train_small, y_test = train_test_split(X, y, test_size=0.10, random_state=42)
#_, X_test, _, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Create an SVM classifier
svm_model = SVC()

# Train the model on the small initial training set
svm_model.fit(X_train_small, y_train_small)

# Evaluate and print the model's performance
y_pred = svm_model.predict(X_test)
print("\nInitial Model Performance:")
print(classification_report(y_test, y_pred))

# Append the informative samples to the training set
X_train_augmented = pd.concat([X_train_small, df.iloc[indices, :3]])
y_train_augmented = pd.concat([y_train_small, df.iloc[indices, 3]])

# Retrain the SVM on this augmented training set
svm_model.fit(X_train_augmented, y_train_augmented)

# Evaluate and print the model's performance again
y_pred_augmented = svm_model.predict(X_test)
print("\nModel Performance after Adding Informative Samples:")
print(classification_report(y_test, y_pred_augmented))

# Print the sizes for the data
print(f"\nX_train_small size: {len(X_train_small)}, y_train_small size: {len(y_train_small)}")
print(f"X_test size: {len(X_test)}, y_test size: {len(y_test)}")
print(f"\nX_train_augmented size: {len(X_train_augmented)}, y_train_augmented size: {len(y_train_augmented)}")
print(f"X_test size: {len(X_test)}, y_test size: {len(y_test)}")
print(f"samples size: {len(samples)}")
