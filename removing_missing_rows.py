# example of removing rows that contain missing values
# from numpy import nan
from pandas import read_csv
# load the dataset
dataset = read_csv('data.csv')
# summarize the shape of the raw data
print('total data:')
print(dataset.shape)
#
# to check the missing values
print(dataset.isnull())
# sum of the missing
print(dataset.isnull().sum())
#
# to drop that row that contain null values
dataset.dropna(inplace=True)
#
# print('after droping da')
print(dataset.shape)
# # # summarize the shape of the data with missing rows removed
# # print(dataset.shape)



