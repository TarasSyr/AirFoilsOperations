# Ми бачимо, що перші кілька рядків — це заголовок та, можливо, службова інформація.
# SolidWorks "Curve through XYZ" очікує формат: X Y Z (три числа в кожному рядку).
# У нашому випадку Z = 0, бо профіль плоский.

output_path = "txt/clarky-il.txt"

with open("txt/clarky-il.csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

# Пропустимо перші 3 рядки (заголовок і службову інфу)
coords = []
for line in lines[3:]:
    parts = line.strip().split()
    if len(parts) == 2:  # тільки X і Y
        try:
            x, y = map(float, parts)
            coords.append(f"{x} {y} 0.0\n")
        except ValueError:
            pass

# Запишемо у новий файл
with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(coords)

output_path
