#Data collection


#ex 1
#load dataset (titanic  dataset from seaborn or csv)

import seaborn as sns
df = sns.load_dataset("titanic")
print("Data Shape: ", df.shape)
print(df.head())

#ex 2
#data cleaning and preprocessing
# Handle missing values
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

# Fill missing values
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=['sex', 'class', 'embarked'], drop_first=True)

# Feature engineering: family size
df['family_size'] = df['sibsp'] + df['parch']

print(df.head())


# Exploratory Data Analysis (EDA)
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

# Histogram of age
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

df = sns.load_dataset("tips")

# Histogram of size
sns.histplot(df['size'], bins=10, kde=True)
plt.title("Age Distribution")
plt.show()