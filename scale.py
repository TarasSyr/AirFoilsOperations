# Відкриваємо вхідний файл і зчитуємо його вміст
with open('txt/naca0012.txt', 'r') as f:
    lines = f.readlines()

# Масштабуємо кожну точку на 100
scaled_lines = []
for line in lines:
    x, y, z = map(float, line.split())
    scaled_x = x * 200
    scaled_y = y * 200
    scaled_z = z * 200
    scaled_lines.append(f"{scaled_x} {scaled_y} {scaled_z}\n")

# Записуємо результат в новий файл
with open('txt/naca0012.txt', 'w') as f:
    f.writelines(scaled_lines)

print("Файл з масштабованими точками збережено.")
