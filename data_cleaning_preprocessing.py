from unittest.mock import inplace


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
print(df.head())
print(df.info())
print(df.describe())


df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'],  inplace=True)
print(df.columns)
print(df.isnull().sum())

df['Sex']=df['Sex'].map({'male':0, 'female':1})
df=pd.get_dummies(df, columns=['Embarked'], drop_first=True)
df.drop(columns=[ 'Name', 'Ticket','PassengerId'], inplace=True)

print(df.columns)
print(df.head())

from sklearn.preprocessing import StandardScaler

column_scale = ['Age', 'Fare', 'Pclass','SibSp', 'Parch']

scaler = StandardScaler()

df[column_scale] = scaler.fit_transform(df[column_scale])

print("Scaled numerical features:")
print(df[column_scale].head())
print(df.describe())

scaled_column = ['Age', 'Fare', 'Pclass', 'SibSp', 'Parch']

for col in scaled_column:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()


check_columns = ['Age', 'Fare',  'SibSp', 'Parch']

for col in check_columns:
 Q1 = df[col].quantile(0.25)
 Q3 = df[col].quantile(0.75)
 IQR = Q3 - Q1
 lower = Q1 - 1.5 * IQR
 upper = Q3 + 1.5 * IQR
 df = df[(df[col] >= lower ) & (df[col] <= upper)]


print("\nAfter cleaning:")
print(df[['Age', 'Fare', 'SibSp']].describe())

print(df.columns)

plt.style.use('ggplot')


for col in check_columns:
    plt.figure()
    plt.boxplot(df[col], vert=False)
    plt.title(f"Boxplot of {col} (Cleaned)")
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()



