import pandas as pd
from scipy import stats

data = pd.read_csv('student-mat.csv')
statistic, p_value = stats.shapiro(data['G3'])

print("H0: Распределение значений G3 является нормальным")
print("H1: Распределение значений G3 не является нормальным\n")
print(f"Значение статистики: {statistic}")
print(f"p-value: {p_value}\n")

alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу")
    print("Вывод: Распределение значений G3 не является нормальным")
else:
    print("Не можем отвергнуть нулевую гипотезу")
    print("Вывод: Распределение значений G3 является нормальным")