import math

# Завантаження точок із файлу
input_file = "scaled_output_tail.txt"
output_file = "rotated_points_tail_x.txt"

points = []
with open(input_file, "r") as f:
    for line in f:
        x, y, z = map(float, line.split())
        points.append((x, y, z))

# Функція для обертання точки навколо Z на 90 градусів
def rotate_point_around_z(x, y, z, angle=90):
    angle_rad = math.radians(angle)
    x_new = -y  # cos(90) = 0, sin(90) = 1
    y_new = x   # cos(90) = 0, sin(90) = 1
    z_new = z   # Z не змінюється
    return x_new, y_new, z_new

# Функція для обертання точки навколо осі X на 90 градусів
def rotate_point_around_x(x, y, z, angle=90):
    angle_rad = math.radians(angle)
    y_new = -z  # cos(90) = 0, sin(90) = 1
    z_new = y   # cos(90) = 0, sin(90) = 1
    x_new = x   # X не змінюється
    return x_new, y_new, z_new

# Функція для обертання точки навколо осі Y на 90 градусів
def rotate_point_around_y(x, y, z, angle=90):
    angle_rad = math.radians(angle)
    x_new = z  # cos(90) = 0, sin(90) = 1
    y_new = y  # Y не змінюється
    z_new = -x # cos(90) = 0, sin(90) = 1
    return x_new, y_new, z_new

# Обертання всіх точок
rotated_points = [rotate_point_around_x(x, y, z) for x, y, z in points]

# Запис результату у файл
with open(output_file, "w") as f:
    for x, y, z in rotated_points:
        f.write(f"{x:.6f} {y:.6f} {z:.6f}\n")

print(f"Обертання завершено. Результати записано в {output_file}")
