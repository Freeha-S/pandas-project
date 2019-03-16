#import the pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# reading file
dataset = pd.read_csv("iris.csv")
# create the heading row
#attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "type"]
#df.columns = attributes
print(dataset.info())
print(dataset.head(50))
#Create 3 DataFrame for each Species
setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']
#print information of 3 data sets
print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())