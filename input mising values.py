#input missing values with numpy
from pandas import read_csv
# load the dataset
dataset = read_csv('data.csv', header=None)
# fill missing values with mean column values
print(dataset.head())
dataset.fillna(dataset.mean(), inplace=True)
# # count the number of NaN values in each column
print("after inputing:")
print(dataset.head())
# print(dataset.isnull().sum())