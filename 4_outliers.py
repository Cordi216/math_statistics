import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('student-mat.csv')

column_data = data['absences']

Q1 = column_data.quantile(0.25)
Q3 = column_data.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(column_data < lower_bound) | (column_data > upper_bound)]

print("Выбросы в столбце 'absences':")
print(outliers)

plt.figure(figsize=(8, 6))
plt.boxplot(column_data, vert=False)
plt.title('Boxplot для столбца "absences"')
plt.show()