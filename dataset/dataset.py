import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target  # Add target column
# Display the first few rows
print(df.head())

# Check the structure of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())
# Display the first few rows
print(df.head())

# Check the structure of the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())
# Compute basic statistics
print(df.describe())

# Group by 'target' and compute mean for each group
grouped = df.groupby('target').mean()
print(grouped)

# Identify patterns or interesting findings
# For example, compare means across groups
print("Mean sepal length for each species:")
print(grouped['sepal length (cm)'])
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

avg_petal_length = df.groupby('target')['petal length (cm)'].mean()
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_petal_length.index, y=avg_petal_length.values)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.xticks(ticks=[0, 1, 2], labels=iris.target_names)
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['sepal width (cm)'], kde=True)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue=df['target'], data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species', labels=iris.target_names)
plt.show()