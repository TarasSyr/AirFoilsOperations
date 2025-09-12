# Відкриваємо вхідний файл і зчитуємо його вміст
with open('txt/clarky_flat_final.txt', 'r') as f:
    lines = f.readlines()

# Масштабуємо кожну точку на 100, зменшуємо x в 2.5 рази і зсуваємо координати
transformed_lines = []
for line in lines:
    x, y, z = map(float, line.split())

    # Зміщення та зміна координат
    new_x = x
    new_y = y - 25
    new_z = z + 5
    transformed_lines.append(f"{new_x} {new_y} {new_z}\n")

# Записуємо результат в новий файл
with open('txt/clarky_flat_final.txt', 'w') as f:
    f.writelines(transformed_lines)

print("Файл з трансформованими точками збережено.")
