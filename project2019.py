#This program part of Programming and Scripting module and its objective is to analyse the Iris Data Set

import pandas as pd #import the pandas
import matplotlib.pyplot as plt #import matplotlib.pyplot
import numpy as np #import numpy
import seaborn as sns # import seaborn

# reading file(load file in pandas dataframe)
dataset = pd.read_csv("iris.csv")
#print the heading
print("The Analysis of Iris Dataset")
print("-----------------------------")

#print the shape of dataset
#that is the number of data points and features 
print( "The number of data points and number of columns/features", dataset.shape)# outputt (150,5)
print("-----------------------------")

print("Name of the columns of dataset")
print(dataset.columns)# column names in dataset

# complete information of a data set data types etc
print("Iris Data Set Info ")
print(dataset.info()) 

# Print first 10 rows of data set to get the idea about data in dataset
print("Iris Data Set first 10 rows ")
print(dataset.head(10)) 

print("Number of data rows of each species in Iris data set")
print(dataset["species"].value_counts())#how many flowers are of each species
#balanced data set as all 3 species has equal numbers of data points 50 each

print("Is there any null (Empty) value in dataset")
print(dataset.isnull().any())

#statistics of data set
print("Descriptive statistics of Iris dataset")
print(dataset.describe().round(3)) # round is optional i used it to maked output look tidy


#Create 3 DataFrame for each Species
setosa=dataset[dataset['species']=='setosa'] # setosa
versicolor =dataset[dataset['species']=='versicolor'] #versicolor
virginica =dataset[dataset['species']=='virginica'] #virginica
print("information of 3 species data sets")
print("Descriptive statistics of Setosa")
print(setosa.describe().round(3))
print("Descriptive statistics of versicolor")
print(versicolor.describe().round(3))
print("Descriptive statistics of virginica")
print(virginica.describe().round (3))

# Visualization
# histograms
# histograms are used to plot a univariate distribution of observation
# sepal length histogram for the dataset
plt.figure() 
x = dataset["sepal_length"]
plt.hist(x, bins = 20, color = "blue") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal Length (cm)") 
plt.ylabel("Count") 
plt.show()
# sepal width histogram for the dataset
plt.figure() 
x = dataset["sepal_width"] 
plt.hist(x, bins = 20, color = "blue") 
plt.title("Sepal Widthh in cm") 
plt.xlabel("Sepal Width (cm)") 
plt.ylabel("Count") 
plt.show()
#petal length histogram for the dataset
plt.figure()
x = dataset["petal_length"]   
plt.hist(x, bins = 20, color = "blue") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count") 
plt.show()
#petal width histogram for the dataset
plt.figure() 
x = dataset["petal_width"]  
plt.hist(x, bins = 20, color = "blue") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_width_cm") 
plt.ylabel("Count") 
plt.show()

# histogram for all 4 varients of data set
dataset.hist()
plt.show()

# Boxplot
# A box plot shows the distribution of quantitative data across a categorical variable.
# Boxplot for whole dataset (numerical data columns)
plt.figure()
dataset.boxplot()
plt.show()

# Box plot of all attributes grouped by species
dataset.boxplot(by="species", figsize=(7,7))
plt.show()

# petal length boxplot group by species
plt.figure()
sns.boxplot(x="species", y="petal_length", data=dataset)
plt.show()
# petal width boxplot graph group by species
plt.figure()
sns.boxplot(x="species", y="petal_width", data=dataset)
plt.show()

# sepal length boxplot group by species
plt.figure()
sns.boxplot(x="species", y="sepal_length", data=dataset)
plt.show()
# sepal width boxplot graph group by species
plt.figure()
sns.boxplot(x="species", y="sepal_width", data=dataset)
plt.show()

#Boxplot with datapoint 
plt.figure(figsize = (10, 7)) 
ax= sns.boxplot(x="species", y="petal_length", data=dataset)
ax= sns.stripplot(x="species", y="petal_length", data=dataset, jitter=True, edgecolor="gray")

boxtwo = ax.artists[2]
boxtwo.set_facecolor('red')
boxtwo.set_edgecolor('black')
boxthree=ax.artists[1]
boxthree.set_facecolor('yellow')
boxthree.set_edgecolor('black')

plt.show()

#Violin plot 
# plays a similar role as a box and whisker plot.
# It shows the distribution of quantitative data across several levels of one (or more) 
# categorical variables such that those distributions can be compared.

#sepal width violin plot
fig, ax = plt.subplots(figsize =(9, 7)) 
sns.violinplot(ax = ax, x = dataset["species"],y = dataset["sepal_width"] ) 
plt.show()
#sepal length violin plot
fig, ax = plt.subplots(figsize =(9, 7)) 
sns.violinplot(ax = ax, x = dataset["species"],y = dataset["sepal_length"] ) 
plt.show()
#petal width violin plot
fig, ax = plt.subplots(figsize =(9, 7)) 
sns.violinplot(ax = ax, x = dataset["species"],y = dataset["petal_width"] ) 
plt.show()
#petal length violin plot
fig, ax = plt.subplots(figsize =(9, 7)) 
sns.violinplot(ax = ax, x = dataset["species"],y = dataset["petal_length"] ) 
plt.show()

#pairplot
# Pair Plot is used to view the pairwise relationship between all the variables in a dataset
# and the diagonal axes show the univariate distribution of the variable. 
# It takes the entire dataset as input and distinguishes data on species with varying colors.

sns.pairplot(dataset, hue="species", height=3)
plt.show()

# Scatter plot is a two-dimensional data visualization that uses dots to represent the values
# obtained for two different variables - one plotted along the x-axis and the other plotted along the y-axis.
# scatter graphs are powerful data visualization tools. 
# these are also used to show if there is any connection between groups of data. 
# If there is a strong connection or correlation, a ‘line of best fit’ can be drawn.

#2-D scatter plot of the data set
dataset.plot(kind="scatter",x="sepal_length", y="sepal_width")
plt.show()

#2-D scatter with colour-coding for each species
sns.set_style("whitegrid")
sns.FacetGrid(dataset,hue="species", height = 4).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()
# the graph shows that setosa species data can be easily seprated
#it means by using sepal_length and sepal_width, setosa flowers can distinguish from other
sns.set_style("whitegrid")
sns.FacetGrid(dataset,hue="species", height = 4).map(plt.scatter,"petal_length","petal_width").add_legend()
plt.show()
# the graph shows that setosa species data can be easily seprated
#it means by using petal_length and petal_width, setosa flowers can be identified from others
# in this graph even virginica and versicolor are mostly seprable
