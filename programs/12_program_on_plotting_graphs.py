"""
Seaborn: for plotting graphs
"""

print("Inside Seaborn Library")
print("-"*20)
# -------------

import seaborn as sns

print(dir(sns))

print("#"*40, end="\n")
################################

print("Get Iris Data")
print("-"*20)
# -------------

import pandas as pd

iris_data = pd.read_csv("Iris.csv")
print(iris_data)

print("#"*40, end="\n")
################################

print("top 5 rows")
print("-"*20)
# -------------

import pandas as pd

print(iris_data.head(5))

print("#"*40, end="\n")
################################

print("SepalLengthCm")
print("-"*20)
# -------------

print(iris_data["SepalLengthCm"])

print("#"*40, end="\n")
################################

print("Min SepalLengthCm")
print("-"*20)
# -------------

print(iris_data["SepalLengthCm"].min())

print("#"*40, end="\n")
################################

print("Max SepalLengthCm")
print("-"*20)
# -------------

print(iris_data["SepalLengthCm"].max())

print("#"*40, end="\n")
################################

print("Average SepalLengthCm")
print("-"*20)
# -------------

print(iris_data["SepalLengthCm"].mean())

print("#"*40, end="\n")
################################


print("Violinplot")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.violinplot(x= "Species", y="SepalWidthCm", data=iris_data)

plt.show()
# plt.savefig("Violinplot.png")
print("#"*40, end="\n")
################################


print("Lineplot")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(x= "Species", y="SepalWidthCm", data=iris_data)

plt.show()
# plt.savefig("Violinplot.png")
print("#"*40, end="\n")
################################

