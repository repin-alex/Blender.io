import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
mass = 1.0  # Масса частицы
charge = 1.0  # Заряд частицы
B = np.array([0.0, 0.0, 1.0])  # Вектор магнитного поля

# Временные параметры
import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
L = 1.0  # Длина расчетной области
T = 1.0  # Время расчета
dx = 0.01  # Шаг по координате x
dt = 0.001  # Шаг по времени
c = 1.0  # Скорость распространения волны

# Создание сетки
x = np.arange(0, L, dx)
t = np.arange(0, T, dt)
nx = len(x)
nt = len(t)

# Инициализация массива для решения
u = np.zeros((nt, nx), dtype=np.complex128)

# Задание начальных условий
u[0] = np.exp(-(x - L/2)**2) * np.exp(1j * x)

# Численное решение уравнения распространения волны
for n in range(1, nt):
    for j in range(1, nx - 1):
        u[n, j] = u[n-1, j] + (c * dt / dx) * (u[n-1, j+1] - 2 * u[n-1, j] + u[n-1, j-1])

# Построение графика
plt.figure()
for n in range(nt):
    plt.plot(x, np.real(u[n]), label=f"t = {n * dt:.2f}")
plt.xlabel('x')
plt.ylabel('Re(u)')
plt.title('Propagation of Wave')
plt.legend()
plt.grid(True)
plt.show()
