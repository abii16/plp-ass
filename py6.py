import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.dropna()

print(df.describe())

grouped = df.groupby('species')['sepal length (cm)'].mean()
print(grouped)

sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
for species in df['species'].unique():
    plt.plot(df[df['species']==species].index, df[df['species']==species]['sepal length (cm)'], label=species)
plt.title("Sepal Length Trend by Species")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['sepal width (cm)'], bins=10, kde=True)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
