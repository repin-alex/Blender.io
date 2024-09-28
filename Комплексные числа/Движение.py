import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
mass = 1.0  # Масса частицы
charge = 1.0  # Заряд частицы
B = np.array([0.0, 0.0, 1.0])  # Вектор магнитного поля

# Временные параметры
t_start = 0.0  # Начальное время
t_end = 10.0  # Конечное время
dt = 0.01  # Шаг времени

# Функция, описывающая движение частицы в электромагнитном поле
def particle_motion(t, r, v):
    # Уравнение движения в электромагнитном поле
    a = charge / mass * np.cross(v, B)
    return v, a

# Метод Рунге-Кутты 4-го порядка для решения дифференциального уравнения
def runge_kutta4(t, r, v, dt):
    v_temp, a_temp = particle_motion(t, r, v)
    k1_r, k1_v = v_temp
    k2_r, k2_v = dt * particle_motion(t + 0.5 * dt, r + 0.5 * k1_r, v + 0.5 * k1_v)
    k3_r, k3_v = dt * particle_motion(t + 0.5 * dt, r + 0.5 * k2_r, v + 0.5 * k2_v)
    k4_r, k4_v = dt * particle_motion(t + dt, r + k3_r, v + k3_v)
    r[i] = r[i-1] + (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6
    v[i] = v[i-1] + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
    return r, v

# Создание временного массива
t = np.arange(t_start, t_end, dt)

# Инициализация массивов для позиции и скорости
r = np.zeros((len(t), 3))
v = np.zeros((len(t), 3))

# Задание начальных условий
r[0] = np.array([1.0, 0.0, 0.0])  # Начальное положение
v[0] = np.array([0.0, 1.0, 0.0])  # Начальная скорость

# Численное интегрирование с использованием метода Рунге-Кутты
for i in range(1, len(t)):
    r[i], v[i] = runge_kutta4(t[i-1], r[i-1], v[i-1], dt)

# Построение графика траектории частицы
fig = plt.figure()
ax = fig.add
