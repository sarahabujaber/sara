import pandas as pd
data = pd.read_csv('data.csv')
print(data.head()) # print first 5 rows (defualt)
print(data.tail()) # print last 5 rows (defualt)
print(type(data))

data.dropna(inplace=True)
data2 = data.dropna()
data.fillna(40, inplace=True)
data2 = data.fillna(40)
print(data2.info())
print(data["Duration"])


print(data.info())
data["Calories"].fillna(70, inplace=True)
print(data.info())
print(data.duplicated())
data.drop_duplicates(inplace=True)
print(data.info())
