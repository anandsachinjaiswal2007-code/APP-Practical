import numpy as np
import pandas as pd

# Create customer dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106],
    'Age': [25, 35, 45, np.nan, 30, 50],
    'MonthlyCharges': [500, 700, 900, 600, np.nan, 800],
    'Tenure': [2, 12, 24, 6, 3, 36],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

print("\nCleaned Data:")
print(df)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn count
print("\nChurn Count:")
print(df['Churn'].value_counts())

# Average charges by churn
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Compare average tenure
print("\nAverage Tenure:")
print(df.groupby('Churn')['Tenure'].mean())