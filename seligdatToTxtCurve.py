# Проста програма для перетворення координат у формат XYZ
# і видалення рядків з буквами

input_file = "txt/seligdatfile.txt"        # вхідний файл з координатами
output_file = "txt/naca0012.txt"   # вихідний файл для SolidWorks

with open(input_file, "r") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    for line in lines:
        # Пропускаємо рядки, де є букви
        if any(ch.isalpha() for ch in line):
            continue
        parts = line.strip().split()
        if len(parts) >= 2:  # якщо є принаймні два числа
            x = parts[0]
            y = parts[1]
            z = "0"
            f.write(f"{x}\t{y}\t{z}\n")

print("Готово! Результат у файлі", output_file)
