import math

def read_points(filename):
    """Зчитує точки X Y Z (або X Y) з файлу."""
    pts = []
    with open(filename, 'r', encoding='utf-8') as f:
        for ln in f:
            parts = ln.strip().split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    z = float(parts[2]) if len(parts) >= 3 else 0.0
                    pts.append((x, y, z))
                except:
                    pass
    return pts

def chord_angle(points, axis="X"):
    """
    Рахує кут нахилу хорди (лінії від LE до TE)
    відносно заданої осі (X, Y чи Z).
    """
    if not points:
        raise ValueError("Немає точок у файлі")

    # Знаходимо передню та задню кромку (мінімальний та максимальний X)
    le = min(points, key=lambda p: p[0])
    te = max(points, key=lambda p: p[0])

    dx = te[0] - le[0]
    dy = te[1] - le[1]
    dz = te[2] - le[2]

    axis = axis.upper()
    if axis == "X":
        # кут до осі X у площині XY
        angle = math.degrees(math.atan2(dy, dx))
    elif axis == "Y":
        # кут до осі Y у площині YZ
        angle = math.degrees(math.atan2(dz, dy))
    elif axis == "Z":
        # кут до осі Z у площині XZ
        angle = math.degrees(math.atan2(dy, dz))
    else:
        raise ValueError("axis має бути 'X', 'Y' або 'Z'")

    return angle, le, te


# === приклад використання ===
if __name__ == "__main__":
    filename = "txt/clarky_solidworks_25mm_moved.txt"   # твій файл з точками
    axis = ("X"
            "")                         # відносно якої осі рахувати
    pts = read_points(filename)
    angle, le, te = chord_angle(pts, axis)
    print(f"Передня кромка LE = {le}")
    print(f"Задня кромка TE = {te}")
    print(f"Кут нахилу хорди відносно осі {axis} = {angle:.3f}°")
