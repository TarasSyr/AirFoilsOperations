import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import r2_score


def read_coordinates_from_file(filename):
    """Читає координати з файлу."""
    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    return x, y


def find_best_flat_section(x, y, min_points=10, max_points=100, step=5):
    """
    Знаходить найкращу плоску ділянку, перевіряючи різні довжини.
    Повертає індекси точок та параметри найкращої лінії.
    """
    # Знаходимо точки нижньої поверхні
    lower_indices = np.where(y < np.median(y))[0]
    x_lower = x[lower_indices]
    y_lower = y[lower_indices]

    # Сортуємо за x
    sort_idx = np.argsort(x_lower)
    x_lower_sorted = x_lower[sort_idx]
    y_lower_sorted = y_lower[sort_idx]
    original_indices = lower_indices[sort_idx]

    best_r2 = -1
    best_indices = None
    best_slope = 0
    best_intercept = 0
    best_length = 0

    # Перебираємо різні довжини ділянок
    for num_points in range(min_points, min(max_points, len(x_lower_sorted)), step):
        best_section_r2 = -1
        best_section_start = 0

        # Перебираємо різні початкові позиції
        for start_idx in range(0, len(x_lower_sorted) - num_points):
            x_section = x_lower_sorted[start_idx:start_idx + num_points]
            y_section = y_lower_sorted[start_idx:start_idx + num_points]

            # Лінійна регресія для цієї ділянки
            slope, intercept, r_value, p_value, std_err = linregress(x_section, y_section)

            # Обчислюємо R² для якості апроксимації
            y_pred = intercept + slope * x_section
            current_r2 = r2_score(y_section, y_pred)

            if current_r2 > best_section_r2:
                best_section_r2 = current_r2
                best_section_start = start_idx

        # Перевіряємо, чи це найкраща ділянка загалом
        if best_section_r2 > best_r2:
            best_r2 = best_section_r2
            best_start = best_section_start
            best_length = num_points

            # Отримуємо параметри найкращої лінії
            x_best = x_lower_sorted[best_start:best_start + num_points]
            y_best = y_lower_sorted[best_start:best_start + num_points]
            best_slope, best_intercept, _, _, _ = linregress(x_best, y_best)
            best_indices = original_indices[best_start:best_start + num_points]

    return best_indices, best_slope, best_intercept, best_r2


def calculate_line_deviation(x_section, y_section, slope, intercept):
    """Обчислює середнє відхилення точок від лінії."""
    y_pred = intercept + slope * x_section
    deviations = np.abs(y_section - y_pred)
    return np.mean(deviations), np.max(deviations)


def visualize_flat_analysis(x, y, flat_indices, slope, intercept, r2):
    """Візуалізує аналіз плоскої ділянки."""
    plt.figure(figsize=(15, 10))

    # Отримуємо точки плоскої ділянки
    x_flat = x[flat_indices]
    y_flat = y[flat_indices]

    # Обчислюємо відхилення
    mean_dev, max_dev = calculate_line_deviation(x_flat, y_flat, slope, intercept)
    angle_deg = np.degrees(np.arctan(slope))

    # 1. Весь профіль з виділеною плоскою ділянкою
    plt.subplot(2, 2, 1)
    plt.plot(x, y, 'b-', linewidth=2, label='Весь профіль', alpha=0.7)
    plt.scatter(x_flat, y_flat, color='red', s=30,
                label=f'Плоска ділянка ({len(x_flat)} точок)', zorder=5)
    plt.title('Профіль Clark Y з виділеною плоскою ділянкою')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 2. Детальний вигляд плоскої ділянки з лінією регресії
    plt.subplot(2, 2, 2)
    plt.plot(x_flat, y_flat, 'ro-', markersize=4, linewidth=1,
             label='Фактичні точки', alpha=0.8)

    # Лінія регресії
    x_line = np.linspace(min(x_flat), max(x_flat), 100)
    y_line = intercept + slope * x_line
    plt.plot(x_line, y_line, 'g--', linewidth=2,
             label=f'Лінія регресії (y = {slope:.4f}x + {intercept:.4f})')

    plt.title(f'Детальний вигляд плоскої ділянки\n' +
              f'Кут: {angle_deg:.3f}°, R² = {r2:.4f}\n' +
              f'Середнє відхилення: {mean_dev:.6f}, Макс: {max_dev:.6f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # 3. Відхилення точок від лінії
    plt.subplot(2, 2, 3)
    y_pred = intercept + slope * x_flat
    deviations = y_flat - y_pred
    plt.plot(x_flat, deviations, 'bo-', markersize=4, linewidth=1)
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.7)
    plt.title('Відхилення точок від лінії регресії')
    plt.xlabel('X')
    plt.ylabel('Відхилення (Y - Y_pred)')
    plt.grid(True, alpha=0.3)

    # 4. Порівняння: лінія vs фактична крива
    plt.subplot(2, 2, 4)
    plt.plot(x_flat, y_flat, 'ro-', markersize=4, linewidth=1,
             label='Фактична крива', alpha=0.8)
    plt.plot(x_line, y_line, 'g--', linewidth=2, label='Лінія регресії')

    # Зафарбовуємо область між кривою та лінією
    plt.fill_between(x_flat, y_flat, intercept + slope * x_flat,
                     color='yellow', alpha=0.3, label='Різниця')

    plt.title('Порівняння: лінія vs фактична крива\n' +
              f'R² = {r2:.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()

    return angle_deg, mean_dev, max_dev, r2


# Основна частина програми
if __name__ == "__main__":
    # Зчитайте ваш файл з координатами
    input_filename = 'txt/clarky_solidworks_25mm_moved.txt'  # замініть на ім'я вашого файлу
    x, y = read_coordinates_from_file(input_filename)

    print("Аналіз плоскої ділянки профілю Clark Y...")

    try:
        # Знаходимо найкращу плоску ділянку
        flat_indices, slope, intercept, r2 = find_best_flat_section(
            x, y, min_points=20, max_points=100, step=5
        )

        # Візуалізуємо результат
        angle, mean_dev, max_dev, r2 = visualize_flat_analysis(
            x, y, flat_indices, slope, intercept, r2
        )

        print("\n=== РЕЗУЛЬТАТИ АНАЛІЗУ ===")
        print(f"Знайдена плоска ділянка: {len(flat_indices)} точок")
        print(f"Кут нахилу плоскої частини: {angle:.4f}°")
        print(f"Якість апроксимації (R²): {r2:.6f}")
        print(f"Середнє відхилення від лінії: {mean_dev:.8f}")
        print(f"Максимальне відхилення: {max_dev:.8f}")

        if r2 > 0.99:
            print("✓ Відмінне співпадіння з прямою лінією!")
        elif r2 > 0.95:
            print("✓ Добре співпадіння з прямою лінією")
        elif r2 > 0.9:
            print("✓ Задовільне співпадіння")
        else:
            print("⚠ Співпадіння недостатньо добре")

        plt.show()

    except Exception as e:
        print(f"Помилка: {e}")
        print("Можливо, потрібно налаштувати параметри пошуку:")
        print("- min_points: мінімальна кількість точок для аналізу")
        print("- max_points: максимальна кількість точок")
        print("- step: крок перебору довжин ділянок")