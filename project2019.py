#import the pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# reading file(load file in pandas dataframe)
dataset = pd.read_csv("iris.csv")

print(dataset.shape) # number of data points and features (150,5)

print(dataset.info()) # 

print(dataset.columns)# column names in dataset

dataset["species"].value_counts()#how many flowers are of each species

#Create 3 DataFrame for each Species
setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']
#print information of 3 data sets
print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())
#balanced data set as all 3 species has equal numbers of data points 50 each
#2-D scatter plot(
dataset.plot(kind="scatter",x="sepal_length", y="sepal_width")
plt.show()
#2-D scatter with colour-coding for each species
sns.set_style("whitegrid")
sns.FacetGrid(dataset,hue="species", size = 4).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()
# the graph shows that setosa species data can be easily seprated
#it means by using sepal_length and sepal_width, setosa flowers can distinguish from other
sns.set_style("whitegrid")
sns.FacetGrid(dataset,hue="species", size = 4).map(plt.scatter,"petal_length","petal_width").add_legend()
plt.show()
# the graph shows that setosa species data can be easily seprated
#it means by using petal_length and petal_width, setosa flowers can be identified from others
# in this grap even virginica and versicolor are mostly seprable