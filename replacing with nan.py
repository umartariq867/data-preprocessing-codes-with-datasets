# example of marking missing values with nan values
from numpy import nan
import pandas as pd
# load the dataset
dataset = pd.read_csv('data.csv')
print(dataset.head())
# # replace '0' values with 'nan'
dataset = dataset.replace(nan, 0)
print("after:")
print(dataset.head())
# # count the number of nan values in each column
# print(dataset.isnull().sum())
# print(dataset.head())