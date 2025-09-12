import csv

input_path = "txt/clarky-il.csv"
output_path = "txt/clarky-il.txt"

coords = []

with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)
    # пропускаємо перші 3 рядки (заголовок/службова інфа)
    for i, row in enumerate(reader):
        if i < 3:
            continue
        if len(row) >= 2:
            try:
                x = float(row[0])
                y = float(row[1])
                coords.append(f"{x} {y} 0.0\n")
            except ValueError:
                pass

with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(coords)

print(f"Готово! Дані записано у {output_path}")
