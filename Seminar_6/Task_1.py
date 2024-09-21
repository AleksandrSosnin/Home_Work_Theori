import scipy.stats as stats
import numpy as np

# Задача 1: Доверительный интервал для математического ожидания
# Данные
M = 80  # Выборочное среднее
sigma = 16  # Известное стандартное отклонение
n = 256  # Объем выборки
alpha = 0.05  # Уровень значимости

# Квантиль нормального распределения
z_alpha = stats.norm.ppf(1 - alpha / 2)

# Доверительный интервал
confidence_interval_1 = (M - z_alpha * (sigma / np.sqrt(n)), M + z_alpha * (sigma / np.sqrt(n)))
print(f"Доверительный интервал для математического ожидания: {confidence_interval_1}")


# Задача 2: Доверительный интервал для величины X
# Данные
data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n = len(data)
alpha = 0.05  # Уровень значимости

# Выборочное среднее и стандартное отклонение
mean_X = np.mean(data)
std_X = np.std(data, ddof=1)

# Квантиль t-распределения
t_alpha = stats.t.ppf(1 - alpha / 2, df=n-1)

# Доверительный интервал
confidence_interval_2 = (mean_X - t_alpha * (std_X / np.sqrt(n)), mean_X + t_alpha * (std_X / np.sqrt(n)))
print(f"Доверительный интервал для величины X: {confidence_interval_2}")


# Задача 3: Доверительный интервал для разности среднего роста
# Данные
daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
n1 = len(daughters)
n2 = len(mothers)
alpha = 0.05  # Уровень значимости

# Средние и стандартные отклонения
mean_daughters = np.mean(daughters)
mean_mothers = np.mean(mothers)
std_daughters = np.std(daughters, ddof=1)
std_mothers = np.std(mothers, ddof=1)

# Квантиль t-распределения
t_alpha = stats.t.ppf(1 - alpha / 2, df=n1 + n2 - 2)

# Доверительный интервал для разности средних
mean_diff = mean_daughters - mean_mothers
se_diff = np.sqrt((std_daughters**2 / n1) + (std_mothers**2 / n2))
confidence_interval_3 = (mean_diff - t_alpha * se_diff, mean_diff + t_alpha * se_diff)

print(f"Доверительный интервал для разности среднего роста: {confidence_interval_3}")
