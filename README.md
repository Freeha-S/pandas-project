# Project 2019
This repositery contains (Iris Data Set) project 2019 for the Module
Programming and Scripting at GMIT.@Freha
---
# Iris Data Set
![](irisimage.png)
<p  align="justify">The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture and picked on the same day and measured at the same time by the same person with the same apparatus".</p>
<p  align="justify">
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.</p>

Dataset Link : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

<h2>Description</h2>
This dataset consist of 150 rows of data and 5 columns 

| sepal_length  | sepal_width  | petal_length | petal_width | species  |
| :-----------: | :----------: | :----------: | :---------: | :------: |
|               |              |              |             |          |

There are 3 classes (types/species) and 4 predictors (variables/attributes) 

<h3>Species(classes)</h3>

    1. Setosa    
    2. Virginica 
    3. versicolor

<h3>Attributes</h3>

    1. sepal_length (in cm)
    2. sepal_width  (in cm)
    3. petal_length (in cm)
    4. petal_width (in cm) 
  
# Exploratory Data Analysis(EDA)
    EDA allows to:
    1. Better understand the data
    2. Build an intuition about the data

    It is a balanced dataset. The number of observations is same for all the classes in the dataset.
        
        dataset["species"].value_counts()
    
    50 rows for each species
    
    There is not any value null in data
    
         dataset.isnull().any()
    
    Information about dataset
    
        dataset.info()

# Visualisation
    Patterns
    First 2D scatter graph was drawn of the data set with sepal length and sepal width 
   ![](Figure_1.png)
    <p>than colour coded graph was drawn as it is clear from the image data of stosa flowers is seprable from others</p>
    ![](Figure_2.png)
    <p>Next colour coded 2d scatter graph of petal width and length shows the same that the dat of stosa is clearly seprable.</p>
    ![](Figure_3.png)
    <p>The best tool to identify the outliers is the box plot.</p>
# Reference
    reference1:[https://www.kaggle.com/kstaud85/iris-data-visualization]