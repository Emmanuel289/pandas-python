import pandas as pd
import numpy as np
pd.set_option('max_rows',10)

#Read data files
iris = pd.read_csv('./Iris_Data.csv')  #syntax to read a file that is located inside the current directory

#Provide a summary of the species column using the describe method
print(iris.species.describe()) #The describe method provides a high-level summary of the attributes of a 
#given column. It is type-aware, meaning that its output will depend on the data type of the input

#Provide a summary of the sepal-width column
print(iris.sepal_width.describe())

#Print the mean, standard deviation of the petal_widths
#print("The first-order statistics of the petal-width of the Iris flower are: \n"
#"min: {} \n max: {} \n mean: {} \n std: {}".format(iris.petal_width.min(), iris.petal_width.max(), iris.petal_width.mean(), iris.petal_width.std()))
 
 
#Print a list of unique values of the petal lengths
#print("The list of unique petal lengths of the Iris flower is: \n {}".format(iris.petal_length.unique()))

#Print a list of the unique values and how often they occur
#print("The unique petal lengths of the Iris flower and their frequency of occurence are: \n {}".format(iris.petal_length.value_counts()))

#Use the map method to reformat entries in a series
mean_petal_length = iris.petal_length.mean()
#print("The mean petal-length of the Iris flower is {}".format(mean_petal_length))
#print(iris.petal_length.map(lambda x: x/mean_petal_length))  #rescale the petal-lengths by dividing by the mean



def height_class(p_length):
	if p_length >mean_petal_length:
		p_length = "Tall"
	else:
		p_length = "Short"
	return p_length

#print(iris.petal_length.map(height_class))#	method 1: pass in the function name as an argument to map
#print(iris.petal_length.map(lambda y: height_class(y))) #method 2: pass in a lambda function as an argument to map


#Use the apply method to reformat entries in a Dataframe
mean_sepal_length,mean_sepal_width, mean_petal_length, mean_petal_width = iris.sepal_length.mean(),iris.sepal_width.mean(),iris.petal_length.mean(),iris.petal_width.mean()

def height_class2(row):
	if ((row.sepal_width > mean_sepal_width) & (row.sepal_length > mean_sepal_width)  &(row.petal_width > mean_petal_width) & (row.petal_length > mean_petal_width)):
		row.sepal_width, row.sepal_length, row.petal_width, row.petal_length  = "Tall", "Tall", "Tall", "Tall"
	elif ((row.sepal_width < mean_sepal_width) & (row.sepal_length < mean_sepal_width)  &(row.petal_width < mean_petal_width) & (row.petal_length < mean_petal_width)):
		row.sepal_width, row.sepal_length, row.petal_width, row.petal_length  = "Short", "Short", "Short", "Short"
	else:
		row.sepal_width, row.sepal_length, row.petal_width, row.petal_length  = "Typical", "Typical", "Typical", "Typical"
	return row

print(iris.apply(height_class2, axis ="columns"))