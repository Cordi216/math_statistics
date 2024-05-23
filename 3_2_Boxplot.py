import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-mat.csv')

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
sns.boxplot(y='G1', data=df, color='skyblue')
plt.title('G1 Boxplot')
plt.subplot(1, 3, 2)
sns.boxplot(y='G2', data=df, color='salmon')
plt.title('G2 Boxplot')
plt.subplot(1, 3, 3)
sns.boxplot(y='G3', data=df, color='lightgreen')
plt.title('G3 Boxplot')
plt.tight_layout()
plt.show()