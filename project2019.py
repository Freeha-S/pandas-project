#This program is to analyse the Iris Data Set
import pandas as pd #import the pandas
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#SciKit-Learn

# reading file(load file in pandas dataframe)
dataset = pd.read_csv("iris.csv")
print("The Analysis of Iris Dataset")
print("-----------------------------")

 # number of data points and features (150,5)
print( "The number of data points and number of columns/features", dataset.shape)
print("-----------------------------")
# complete information of a data set data types etc
print("Iris Data Set Info ")
print(dataset.info()) 

print("Name of the columns of dataset")
print(dataset.columns)# column names in dataset

print("Iris Data Set first 10 rows ")
print(dataset.head(10)) 

print("Number of data rows of each species")
print(dataset["species"].value_counts())#how many flowers are of each species
print(dataset.isnull().any())

#Create 3 DataFrame for each Species
setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']
print("information of 3 species data sets")
print("Setosa")
print(setosa.describe())
print("versicolor")
print(versicolor.describe())
print("virginica")
print(virginica.describe())
#balanced data set as all 3 species has equal numbers of data points 50 each

# sepal length i
plt.figure(figsize = (10, 7)) 
x = dataset["sepal_length"] 
  
plt.hist(x, bins = 20, color = "blue") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count") 
plt.show()
plt.figure(figsize = (10, 7)) 
x = dataset["sepal_width"] 
  
plt.hist(x, bins = 20, color = "blue") 
plt.title("Sepal Widthh in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count") 
plt.show()
#petal length
plt.figure(figsize = (10, 7)) 
x = dataset["petal_length"] 
  
plt.hist(x, bins = 20, color = "blue") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count") 
plt.show()
#petal width
plt.figure(figsize = (10, 7)) 
x = dataset["petal_width"] 
  
plt.hist(x, bins = 20, color = "blue") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_width_cm") 
plt.ylabel("Count") 
plt.show()
# build the box plot
dataset.boxplot(by="species", figsize=(10, 10))
plt.show()

plt.figure(figsize = (10, 7)) 
sns.boxplot(x="species", y="petal_length", data=dataset)
plt.show()

#2-D scatter plot of the data set
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
