# Ім'я вхідного та вихідного файлів
input_file = "txt/n0009sm.txt"  # Вхідний файл із двома координатами
output_file = "txt/points_with_z.txt"  # Вихідний файл із доданою третьою координатою

# Читання з вхідного файлу
with open(input_file, "r") as infile:
    lines = infile.readlines()

# Додавання координати z = 0
with open(output_file, "w") as outfile:
    for line in lines:
        x, y = map(float, line.split())  # Читання x і y
        z = 0.0  # Значення координати z
        outfile.write(f"{x:.6f} {y:.6f} {z:.6f}\n")  # Запис у новий файл

print(f"Координата z = 0 додана. Результат записано в {output_file}.")
