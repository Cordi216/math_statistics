import pandas as pd

data = pd.read_csv('student-mat.csv')
num_rows, num_columns = data.shape
data_types = data.dtypes
missing_values = data.isnull().sum().sum()

print("Название базы данных: student-mat.csv")
print("Количество наблюдений:", num_rows)
print("Количество переменных:", num_columns)
print("Типы данных:")
print(data_types)
print("Количество пропущенных значений:", missing_values)