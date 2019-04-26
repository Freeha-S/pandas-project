# Project 2019
This repositery contains (Iris Data Set) project 2019 for the Module "Programming and Scripting" of Higher Dip. in Data Analytics at GMIT.by Freha Saleem
-----
The aim of this project is to research the iris data set, and  write documentation and code in the Python programming language based on that research.
---------
## Lecturer: Dr Ian McLoughlin

# Background Information
-----
## Iris Flower Data Set

![](images/irisimage.png)

<p  align="justify">The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis. 
This dataset sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture and picked on the same day and measured at the same time by the same person with the same apparatus". </p>
<p  align="justify">
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
Four features: sepal length, sepal width, petal length and petal width (meaurements in centimeters) for each flower. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.</p>
-
Dataset Link : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

<h2>Summery of DataSet</h2>

**This dataset consist of 150 rows of data in 5 columns** 

    | sepal_length  | sepal_width  | petal_length | petal_width | species  |
    | :-----------: | :----------: | :----------: | :---------: | :------: |
    |               |              |              |             |          |

**There are 3 classes (types/species) and 4 predictors (variables/attributes) in this data set**
        
**Species(classes)**
            
         1. Setosa    
         2. Virginica 
         3. versicolor

**Attributes**

        1. sepal_length (in cm)
        2. sepal_width  (in cm)
        3. petal_length (in cm)
        4. petal_width (in cm) 
    
# Data Analysis Process
    
![](images/AnalysisProcess.PNG)

I start from seond phase that is Exploration of data.

# Import Python Libraries for Data Analysis
    
    import pandas as pd    
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
- **pandas**
        is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. pandas is a NumFOCUS sponsored project.
            [source: https://pandas.pydata.org/] 
            Pandas is the most popular data manipulation package in Python, and DataFrames are the Pandas data type for storing tabular 2D data.
 
- **numpy**
        is the fundamental package for scientific computing with Python. 
    
- **matplotlib**
        is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.[source: https://matplotlib.org/]
    
- **seaborn**
        is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. [source: https://seaborn.pydata.org/]
    
   
# Read Data
  First download the datset csv file from the 
Dataset Link : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data and save it in the project folder as iris.cvs.
    
*( CSV is a simple file format used to store tabular data. CSV (comma-separated value) file format is common for transferring and storing data. The ability to read, manipulate, and write data to and from CSV files using Python is a key skill for any data scientist or business analysis.)*
   
Read data from file 'iris.csv'into pandas DataFrames
  ```
   dataset = pd.read_csv("iris.csv")
   ```  
Print the name of columns (headings)
   ``` 
    dataset.columns 
   ```
   ![](images/columns.PNG)

# Exploratory Data Analysis(EDA)
   
   Exploratory Data Analysis is an approach/philosophy for data analysis that employs a variety of techniques to:

    1. Better understand the data
    2. Build an intuition about the data

## Insight into Dataset

- The number of data points and number of columns/features
   ```
     print(dataset.shape)
   ```
    (150,5)

- There is not any null value in data set *to check if there is any empty cell*
   ``` 
     print(dataset.isnull().any())
   ```
   ![](images/notNull.png)

- It is a **balanced dataset**. The number of observations is same for all the classes in the dataset.
   ```   
     print(dataset["species"].value_counts())
   ```
   ![](images/rows.png)
   
    50 rows for each species

- Information about dataset
   ```
     print(dataset.info()) 
   ```
   ![](images/datasetInfo.png)

- First 10 rows of data set
   ```
      print(dataset.head(10)) 
   ```
   ![](images/head.png)
 
- Statistics summery of dataset
   ```
     print(dataset.describe()) 
   ```
    ![](images/datasetdescribe.PNG)

- Statistics summery of dataset of three species seprately
   ```
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
   ```
    ![](images/sdescribe.PNG)
    

# Visualisation of Dataset
## Histogram

    A histogram is a great tool for quickly assessing a probability distribution that is  understood by almost any audience. Python offers a handful of different options for building and plotting histograms. Most people know a histogram by its graphical representation, which is similar to a bar graph
## Box Plot
   
    Boxplot is probably one of the most common type of graphic. It gives a summary of one or several numeric variables. The line that divides the box into 2 parts represents the **median** of the data. The end of the box shows **the upper and lower quartiles**. The extreme lines shows **the highest and lowest value excluding outliers**. Note that boxplot hide the number of values existing behind the variable.

## Scatter Graph
    
    A scatter plot/ scatter graph is a two-dimensional data visualization that uses dots to represent the values obtained for two different variables - one plotted along the x-axis and the other plotted along the y-axis.
    scatter graphs are powerful data visualization tools. these are also used to show if there is any connection between groups of data.
    If there is a strong connection or correlation, a ‘line of best fit’ can be drawn.
    
### Patterns
    First 2D scatter graph was drawn of the data set with sepal length and sepal width 
   ![](graphs/Figure_1.png)
    <p>than colour coded graph was drawn as it is clear from the image data of stosa flowers is seprable from others</p>
    ![](graphs/Figure_2.png)
    <p>Next colour coded 2d scatter graph of petal width and length shows the same that the dat of stosa is clearly seprable.</p>
    ![](graphs/Figure_3.png)
    <p>The best tool to identify the outliers is the box plot.</p>
# Reference

1. Python Pandas read_csv – Load Data from CSV Files:[https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/]
2. Iris datset-Exploratory Data Analysis[https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis]
3. Iris Data Visualization: [https://www.kaggle.com/kstaud85/iris-data-visualization]
4. Scatter graphs [https://www.bbc.com/bitesize/guides/zmt9q6f/revision/1]
5. Visualize Iris dataset using Python [http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python]
6. Python Histogram : [https://realpython.com/python-histograms/]
7. Boxplot: [https://python-graph-gallery.com/boxplot/]
