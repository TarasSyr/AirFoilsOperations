import numpy as np

# Завантаження точок профілю (x, y, z)
points = np.loadtxt('txt/naca09_root_chord_wing.txt', delimiter=' ')  # Файл з точками x, y, z

# Знаходження передньої та задньої кромки
leading_edge = points[np.argmin(points[:, 0])]  # Точка з мінімальним x
trailing_edge = points[np.argmax(points[:, 0])]  # Точка з максимальним x

# Формування прямої між передньою та задньою кромками
line = np.array([leading_edge, trailing_edge])

# Збереження лінії у файл
np.savetxt('txt/naca09_root_chord_wing_mid_line.txt', line, delimiter=' ', fmt='%.6f')


print("Line saved to 'txt/naca09_tip_chord_wing_mid_line.txt'")
