import numpy as np

def load_airfoil(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                x, y, z = map(float, parts[:3])
                data.append([x, y, z])
    return np.array(data)

def save_airfoil(filename, coords):
    with open(filename, "w") as f:
        for p in coords:
            f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f}\n")

def get_plane_normal(points):
    """Обчислює нормаль до площини за трьома точками профілю."""
    p1, p2, p3 = points[0], points[len(points)//2], points[-1]
    v1 = p2 - p1
    v2 = p3 - p1
    normal = np.cross(v1, v2)
    normal /= np.linalg.norm(normal)
    return normal

def shift_airfoil(points, distance):
    normal = get_plane_normal(points)
    return points + normal * distance

# ==== Використання ====
root = load_airfoil("txt/naca0012_root.txt")
tip = shift_airfoil(root, -20.0)   # зміщуємо на 200 мм по нормалі

save_airfoil("txt/naca0012_root-.txt", tip)
print("Збережено файл tip airfoil у naca0012_tip.txt")
