# -*- coding: utf-8 -*-
"""ModelPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AWnA2vPlKpHeVwiOVezb96NlVdUx70Tg
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('preprocessed_dataset.csv')

# Separate features (X) and target variable (y)
X = df.drop(['Year', 'Turnout','NA'], axis=1)  # Excluding 'Year' as it's not a predictor
y = df['Turnout']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Impute missing values in X_train
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)

# Train the linear regression model using imputed data
model = LinearRegression()
model.fit(X_train_imputed, y_train)

# Evaluate the model
train_accuracy = model.score(X_train_imputed, y_train)
test_accuracy = model.score(imputer.transform(X_test), y_test)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Predict turnout for 2024
# Assuming a hypothetical data for 2024
X_2024 = pd.DataFrame({
    'turnout_n': [50.0],
    'Regd_Voters': [200000],
    'Total_Votes': [150000],
    'ValidVotes': [140000],
    'RejectedVotes': [10000],
    'Votes': [80000]
})

predicted_turnout_2024 = model.predict(imputer.transform(X_2024))
print("Predicted Turnout for 2024:", predicted_turnout_2024)

overall_accuracy = (train_accuracy + test_accuracy) / 2

print("Overall Accuracy (mean R-squared score):", overall_accuracy)