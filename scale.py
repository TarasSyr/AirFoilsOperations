# Відкриваємо вхідний файл і зчитуємо його вміст
with open('txt/naca0012_root.txt', 'r') as f:
    lines = f.readlines()

# Масштабуємо кожну точку на 100
scaled_lines = []
for line in lines:
    x, y, z = map(float, line.split())
    scaled_x = x * 0.75
    scaled_y = y * 0.75
    scaled_z = z * 0.75
    scaled_lines.append(f"{scaled_x} {scaled_y} {scaled_z}\n")

# Записуємо результат в новий файл
with open('txt/naca0012_tip.txt', 'w') as f:
    f.writelines(scaled_lines)

print("Файл з масштабованими точками збережено.")
