import pandas as pd

iris = pd.read_csv('./Iris_Data.csv', index_col =0)

print('The iris species include: \n {}'.format(iris.head()))
#print('The length of the sepals are: \n{}'.format(iris.sepal_length)) #use dot notation followed by the name of a column to access its entries
#print('The length of the sepals are: \n{}'.format(iris['sepal_length'])) #second method possible if object is a dictionary

print('The sepal_length of Iris-setosa is: {}'.format(iris['sepal_length'][1]))  #retrieve a row entry using its integer index

#Pandas-specific indexing
#print('The {} has the following properties: \n{}'.format(iris.iloc[0,-1],iris.iloc[0])) #index-based selection. Selects first row of dataset
#print('The sepal_lengths of all the species of iris flowers are: \n{}'. format(iris.iloc[:,0]))  #syntax for iloc is row first and colum second. Passing a colon retrieves all values in that row or column dimension
print('The sepal_lengths of the first five species of iris flowers are: \n{}'. format(iris.iloc[:5,0]))
#print('The sepal length of the first species of iris flowers is: {}'.format(iris.loc[1, 'sepal_length'])) #label-based selection

print('The sepal length of the all the species of iris flowers are: {}'.format(iris.loc[:, 'sepal_length'])) #label-based selection
iris.set_index('sepal_length','sepal_lengths')
print(iris)

#Conditional Selection
#print(iris.sepal_length ==5.1) #true for all lengths equal to 5.1 and false otherwise
#print(iris.loc[iris.sepal_length ==5.1]) #can be used inside loc to select the relevant data that meets the condition
#print(iris.loc[(iris.sepal_length ==4.8)&(iris.sepal_width ==3.0)]) #can check if multiple conditions are satisfied &

#print(iris.loc[(iris.sepal_length >4.8)|(iris.sepal_width <=3.0)]) #can check if any of the conditions are satisfied using |

#print(iris.loc[iris.species.isin(['Iris-setosa', 'Iris-virginica'])]) #check the data under a particular column whose value is in a list of values

#print(iris.loc[iris.sepal_width.isnull()]) #print sepal_widths that are empty or NaN
print(iris.loc[iris.sepal_width.notnull()]) #print sepal_widths that are not empty