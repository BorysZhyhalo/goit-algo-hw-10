import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 2  

# Визначення функції та межі інтегрування
def func(x):
    return x ** 2

if __name__ == "__main__":

    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = func(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

