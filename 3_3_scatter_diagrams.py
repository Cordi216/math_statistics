import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-mat.csv')

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.scatterplot(x='G1', y='G2', data=df, color='skyblue')
plt.title('G1 vs G2')
plt.subplot(1, 3, 2)
sns.scatterplot(x='G2', y='G3', data=df, color='salmon')
plt.title('G2 vs G3')
plt.subplot(1, 3, 3)
sns.scatterplot(x='G1', y='G3', data=df, color='lightgreen')
plt.title('G1 vs G3')
plt.tight_layout()
plt.show()