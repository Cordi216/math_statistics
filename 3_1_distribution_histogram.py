import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-mat.csv')

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
sns.histplot(df['G1'], kde=True, color='skyblue')
plt.title('G1 Distribution')
plt.subplot(1, 3, 2)
sns.histplot(df['G2'], kde=True, color='salmon')
plt.title('G2 Distribution')
plt.subplot(1, 3, 3)
sns.histplot(df['G3'], kde=True, color='lightgreen')
plt.title('G3 Distribution')
plt.tight_layout()
plt.show()