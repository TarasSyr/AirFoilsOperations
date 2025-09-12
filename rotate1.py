import math

def rotate_points(input_file, output_file, axis, angle_degrees):
    """
    Обертає точки на заданий кут навколо вказаної осі.

    input_file: файл з координатами x, y, z
    output_file: файл з обчисленими координатами
    axis: вісь обертання ('x', 'y', 'z')
    angle_degrees: кут обертання в градусах
    """
    # Перетворення кута в радіани
    theta = math.radians(angle_degrees)

    # Читання точок із файлу
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    # Відкриття файлу для запису обернених точок
    with open(output_file, "w") as outfile:
        for line in lines:
            # Зчитування x, y, z
            x, y, z = map(float, line.split())

            # Формули обертання
            if axis == 'x':
                # Обертання навколо осі X
                y_rotated = y * math.cos(theta) - z * math.sin(theta)
                z_rotated = y * math.sin(theta) + z * math.cos(theta)
                x_rotated = x
            elif axis == 'y':
                # Обертання навколо осі Y
                x_rotated = x * math.cos(theta) + z * math.sin(theta)
                z_rotated = -x * math.sin(theta) + z * math.cos(theta)
                y_rotated = y
            elif axis == 'z':
                # Обертання навколо осі Z
                x_rotated = x * math.cos(theta) - y * math.sin(theta)
                y_rotated = x * math.sin(theta) + y * math.cos(theta)
                z_rotated = z
            else:
                raise ValueError("Невірна вісь. Виберіть 'x', 'y' або 'z'.")

            # Запис результату у файл
            outfile.write(f"{x_rotated:.6f} {y_rotated:.6f} {z_rotated:.6f}\n")

    print(f"Точки обернені на {angle_degrees} градусів навколо осі {axis.upper()} і записані в {output_file}.")

# Використання функції
# Вхідний файл із координатами
input_file = "txt/naca09_tip_chord_tail.txt"

# Вихідний файл для обернених координат
output_file = "txt/naca09_tip_chord_tail.txt"

# Виберіть вісь ('x', 'y', 'z') і кут обертання
rotate_points(input_file, output_file, axis='x', angle_degrees=315)  # Наприклад, обертання на 45° навколо осі X
#rotate_points(input_file, output_file, axis='y', angle_degrees=30)  # Наприклад, обертання на 30° навколо осі Y
#rotate_points(input_file, output_file, axis='z', angle_degrees=90)  # Наприклад, обертання на 90° навколо осі Z