def convert_selig_to_solidworks(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Пропускаємо перший рядок (назва профілю)
    coords = []
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) >= 2:
            x, y = map(float, parts[:2])
            coords.append((x, y))

    # Видаляємо дубльовану точку (0,0), якщо вона двічі зустрічається
    cleaned = []
    seen = set()
    for i, (x, y) in enumerate(coords):
        key = (round(x, 6), round(y, 6))
        if key not in seen:
            cleaned.append((x, y))
            seen.add(key)

    # Формуємо X Y Z (Z=0)
    with open(output_file, "w") as f:
        for x, y in cleaned:
            f.write(f"{x:.6f} {y:.6f} 0.0\n")

    print(f"Файл збережено у форматі SolidWorks: {output_file}")


# Приклад використання
convert_selig_to_solidworks("txt/naca0009.txt", "txt/naca0009.txt")
