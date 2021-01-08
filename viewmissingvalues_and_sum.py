# 1) to view the missing values in all dataset

import pandas as pd
# df=pd.read_csv("data.csv")
# print(df.head(50))
# 1.1) to view missing values in specific column
df=pd.read_csv('house_dataset1.csv')
# print(df['area'].head())
# # 2) to check missing values
#   # for one coloumn
# print(df['area'].isnull())

# 2.1) for all dataset
print(df.isnull())

# 3) to count the total numbers of null values in your data
print(df.isnull().sum())
# 3.1 to count the total number of null values in specific column
print(df['price'].isnull().sum())


