import scipy.integrate as integrate
import numpy as np

from view import func, a, b


def analytical_integral(a_val, b_val):
    """Аналітичний інтеграл для f(x) = x²: ∫ x² dx = x³/3."""
    return (b_val**3 - a_val**3) / 3


def monte_carlo(func, a_val, b_val, num_points):
    ymax = func(b_val)
    x = np.random.uniform(a_val, b_val, num_points)
    y = np.random.uniform(0, ymax, size=num_points)
    under_curve = np.sum(y < func(x))
    return (b_val - a_val) * ymax * (under_curve / num_points)


if __name__ == "__main__":
    num_points = 1_000_000

    analytical = analytical_integral(a, b)
    quad_result, quad_error = integrate.quad(func, a, b)
    mc_result = monte_carlo(func, a, b, num_points=num_points)

    mc_diff = abs(mc_result - quad_result)
    mc_relative_error = mc_diff / quad_result * 100

    print(f"Функція: f(x) = x², інтервал [{a}, {b}]")
    print(f"Аналітичний результат:  {analytical:.10f}  (8/3)")
    print(f"SciPy quad:             {quad_result:.10f}  (похибка оцінки: {quad_error:.2e})")
    print(f"Метод Монте-Карло:      {mc_result:.10f}  ({num_points:,} точок)")
    print(f"Різниця MC vs quad:     {mc_diff:.6f}  ({mc_relative_error:.4f}%)")
