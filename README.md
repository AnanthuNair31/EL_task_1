# EL_task_1
Cleaning & Pre-processing dataset from Titanic-Dataset.csv 

This project demonstrates a complete data cleaning and pre-processing pipeline for the Titanic dataset using Python. 
The process includes handling missing values, encoding categorical features, feature scaling, detecting and removing outliers, and data visualization.

1. Data Loading & Exploration

- Loaded dataset using 'pandas'
- Displayed initial rows, data types, and summary statistics

2. Missing Values Handling

- Imputed missing 'Age' values with median
- Filled missing 'Embarked' values with mode
- Dropped 'Cabin' due to excessive missing values

3. Encoding Categorical Data

- Mapped 'Sex' column: male → 0, female → 1
- One-hot encoded 'Embarked' (dropped the first to avoid dummy variable trap Embarked ="C")
- Dropped 'Name', 'Ticket', and 'PassengerId' as they are identifiers

4. Feature Scaling

- Standardized numerical columns: 'Age', 'Fare', 'Pclass', 'SibSp', 'Parch' using 'StandardScaler'

5. Outlier Detection and Removal

- Used the IQR (Interquartile Range) method to identify and remove outliers
- Visualized data before and after cleaning using boxplots


NOTE-  Libraries Used

- 'pandas'
- 'matplotlib'
- 'seaborn'
- 'sklearn.preprocessing.StandardScaler'

Boxplots are used to visualize:
- Raw vs Cleaned distribution of 'Age', 'Fare', 'SibSp', 'Parch'




