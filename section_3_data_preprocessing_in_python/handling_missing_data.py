# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('pima-indians-diabetes.csv')

# Identify missing data (assumes that missing data is represented as NaN)
missing_data = df.isnull().sum()

# Print the number of missing entries in each column
print(missing_data)

# Configure an instance of the SimpleImputer class

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')


# Fit the imputer on the DataFrame
imputer.fit(df)


# Apply the transform to the DataFrame
df_imputed = imputer.transform(df)

#Print your updated matrix of features
print(df_imputed)