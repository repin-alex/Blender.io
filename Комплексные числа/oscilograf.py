import numpy as np
from turtle import*
import matplotlib.pyplot as plt

# Параметры модели
mass = float(textinput("Масса","Введите значение"))  # Масса 1.0
k = float(textinput("Коэффициент упругости","Введите значение"))  # Коэффициент упругости 2.0
omega = np.sqrt(k / mass)  # Угловая частота

# Временные параметры
t_start = float(textinput("Начальное время","Введите значение"))  # Начальное время 0.0
t_end = float(textinput("Конечное время","Введите значение"))  # Конечное время 10.0
dt = float(textinput("Шаг времени","Введите значение"))  # Шаг времени 0.01

# Создание временного массива
t = np.arange(t_start, t_end, dt)

# Создание комплексного массива для позиции осциллятора
x = np.exp(1j * omega * t)  # Используем комплексное число для представления фазы и амплитуды

# Извлечение реальной части для графического представления
x_real = np.real(x)

# Построение графика позиции осциллятора
plt.plot(t, x_real)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Harmonic Oscillator')
plt.grid(True)
plt.show()
