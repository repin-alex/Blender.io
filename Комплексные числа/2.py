import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
growth_rate = 0.05  # Коэффициент роста популяции

# Временные параметры
t_start = 0.0  # Начальное время
t_end = 10.0  # Конечное время
dt = 0.01  # Шаг времени

# Функция, описывающая рост популяции
def population_growth(t, p):
    return growth_rate * p * (1 - p)

# Метод Рунге-Кутты 4-го порядка для решения дифференциального уравнения
def runge_kutta4(t, p, dt):
    k1 = dt * population_growth(t, p)
    k2 = dt * population_growth(t + 0.5 * dt, p + 0.5 * k1)
    k3 = dt * population_growth(t + 0.5 * dt, p + 0.5 * k2)
    k4 = dt * population_growth(t + dt, p + k3)
    p += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return p

# Создание временного массива
t = np.arange(t_start, t_end, dt)

# Инициализация массива для популяции
p = np.zeros(len(t), dtype=np.complex128)

# Задание начального условия
p[0] = 0.1  # Начальная популяция

# Численное интегрирование с использованием метода Рунге-Кутты
for i in range(1, len(t)):
    p[i] = runge_kutta4(t[i-1], p[i-1], dt)

# Построение графика роста популяции
plt.plot(t, np.real(p))
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Growth')
plt.grid(True)
plt.show()
