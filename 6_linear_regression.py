import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('student-mat.csv')

X = data[['G1']]
y = data['G2']

model = LinearRegression()
model.fit(X, y)

intercept = model.intercept_
slope = model.coef_[0]

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='b', label='Данные')
plt.plot(X, model.predict(X), color='r', label=f'Линейная регрессия: y = {slope:.2f} * x + {intercept:.2f}')
plt.xlabel('Оценка G1')
plt.ylabel('Оценка G2')
plt.title('Линейная регрессия между оценками G1 и G2')
plt.legend()
plt.show()