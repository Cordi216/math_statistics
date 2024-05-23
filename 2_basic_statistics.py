import pandas as pd

df = pd.read_csv('student-mat.csv')
statistics = df[['G1', 'G2', 'G3']].describe()
correlation = df[['G1', 'G2', 'G3']].corr()

print("\nОсновные статистические характеристики для G1, G2, G3:\n")
print(statistics)
print("\n\nКорреляция между G1, G2, G3:\n")
print(correlation)