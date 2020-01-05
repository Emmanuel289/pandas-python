import sys
import pandas as pd
#There are two core object types in pandas: dataframes and series. Dataframes are tables and series are lists.

#An example of a table that contains string keys and integer lists. They keys are the column names and the values are the list of entries

tab1= pd.DataFrame({'Yes': [50,21], 'No': [131,2] })   
print('An example of a table of integer numbers is: \n {}'.format(tab1))

tab2 = pd.DataFrame({'Bob': ['I Liked it.', 'it was awful'], 'Sue': ['Pretty good.', 'Bland.'] })

print('An example of a table of strings is: \n {} '.format(tab2))

tab2 = pd. DataFrame({'Bob': ['I Liked it.', 'it was awful'], 'Sue': ['Pretty good.', 'Bland.'] }, index = ['Product A', 'Product B']) #assign row labels using the index parameter

print('The rows labels have been assigned and the modified table is: \n {}'.format(tab2))


#Create a series by passing a list object as an input. A dataframe is simply a list of series that are glued together
list1= pd.Series([1,2,3,4,5]) # a series is simply a single column of a DataFrame

print('An example of a pandas series is: \n {}'.format(list1))

list2 = pd.Series([30,35,48], index=['2015 Sales', '2016 Sales', '2017 Sales'], name = 'Product A') #label the rows using the index parameter and label the series using the name parameter.

print('The sales for {} in the previous three years is: \n {}'.format(list2.name, list2)) 


#Reading data files
iris = pd.read_csv('./Iris_Data.csv')  #syntax for reading from a file that is located within the current directory
print('The Iris flower comprises several species which include: \n{}'.format(iris))

print('In the above example, our dataset has {} rows, {} columns, and is of size {} bytes. The first five entries are \n {}'.format(iris.shape[0], iris.shape[1], sys.getsizeof(iris), iris.head()))  #use the shape attribute to know the dimensions of a dataset, the getsizeof method of sys to know the total byte-size, 
#and use the head() method to examine its the first five entries

iris = pd.read_csv('./Iris_Data.csv', index_col =0)  #use the index_col attribute so pandas can retrieve the column index of a file
print(iris.head()) 
