import scipy.stats as stats
import numpy as np


#Сравните 1- и 2-е измерения (предыдущей задачи №2), предполагая, что 3-го измерения через 30 минут не было.
#Есть ли статистически значимые различия между измерениями давления?

α=0.05
data1 = np.array([150, 160, 165, 145, 155])
data2 = np.array([140, 155, 150, 130, 135])


print(f"Анализ зависимых выборок, 2 группы данных.\n\
Выбран критерий Уилкоксона, α={α}.\n\
H0: статистически значимых различий нет\n\
H1: имеются статистически значимые различия\n")

print(stats.wilcoxon(data1, data2))

statistic, pvalue = stats.wilcoxon(data1, data2)
msg = 'H0 принимается, статистически значимых отличий нет' if α < pvalue \
    else 'H0 отвергается, принимается H1, есть статистически значимые отличия'
print(f'{msg}')