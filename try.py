# Відкриваємо вхідний файл і зчитуємо його вміст
with open('txt/naca09_tip_chord_wing.txt', 'r') as f:
    lines = f.readlines()

# Масштабуємо кожну точку на 100, зменшуємо x в 2.5 рази і зсуваємо координати
transformed_lines = []
for line in lines:
    x, y, z = map(float, line.split())

    # Зміщення та зміна координат
    new_x = x+350    # Зменшення x в 2.5 рази і зсув на 150
    new_y = y  # y залишаємо без змін
    new_z = z+600  # Зсув по z на 500

    transformed_lines.append(f"{new_x} {new_y} {new_z}\n")

# Записуємо результат в новий файл
with open('txt/naca09_tip_chord_wing.txt', 'w') as f:
    f.writelines(transformed_lines)

print("Файл з трансформованими точками збережено.")
