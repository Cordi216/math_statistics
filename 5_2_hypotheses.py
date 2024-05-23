import pandas as pd
import numpy as np

data = pd.read_csv('student-mat.csv')

group1_scores = data[data['sex'] == 'F']['G3']
group2_scores = data[data['sex'] == 'M']['G3']

def bootstrap_mean_diff(data1, data2, num_boots=1000):
    mean_diffs = []
    combined_data = np.concatenate((data1, data2))

    for _ in range(num_boots):
        bootstrap_sample = np.random.choice(combined_data, size=len(combined_data), replace=True)
        bootstrap_mean1 = np.mean(bootstrap_sample[:len(data1)])
        bootstrap_mean2 = np.mean(bootstrap_sample[len(data1):])
        mean_diffs.append(bootstrap_mean1 - bootstrap_mean2)

    return mean_diffs

mean_diffs = bootstrap_mean_diff(group1_scores, group2_scores)
observed_mean_diff = np.mean(group1_scores) - np.mean(group2_scores)

p_value = (np.sum(np.abs(mean_diffs) >= np.abs(observed_mean_diff)) + 1) / (len(mean_diffs) + 1)

print("H0: Средние двух групп равны")
print("H1: Средние двух групп не равны\n")
print(f"Наблюдаемая разница в средних: {observed_mean_diff}")
print(f"p-value: {p_value}\n")

alpha = 0.05
if p_value < alpha:
    print("Отвергаем нулевую гипотезу")
    print("Вывод: Средние двух групп различаются")
else:
    print("Не можем отвергнуть нулевую гипотезу")
    print("Вывод: Средние двух групп равны - нет статистически значимых различий")