import numpy as np

def load_airfoil(filename):
    """Завантажує координати з файлу (x,y[,z])."""
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                x, y = float(parts[0]), float(parts[1])
                # додаємо z=0 якщо його немає
                z = float(parts[2]) if len(parts) == 3 else 0.0
                data.append([x, y, z])
    return np.array(data)

def save_airfoil(filename, coords):
    """Зберігає координати у файл."""
    with open(filename, "w") as f:
        for p in coords:
            f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f}\n")

def rotate(points, angle_deg):
    """Повертає профіль навколо осі Y на заданий кут (наприклад, 35°)."""
    theta = np.radians(angle_deg)
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0,             1, 0            ],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return points @ R.T

def shift_airfoil(points, angle_deg, distance):
    """
    Зсуває профіль на 'distance' вздовж нормалі
    після повороту на angle_deg.
    """
    # нормаль у локальній системі = (0,0,1)
    n_local = np.array([0, 0, 1])
    theta = np.radians(angle_deg)
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0,             1, 0            ],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    n_global = R @ n_local  # обертання нормалі
    n_global /= np.linalg.norm(n_global)  # нормалізація
    return points + n_global * distance

# ==== Приклад використання ====

root = load_airfoil("root_airfoil.dat")       # координати root
root_rot = rotate(root, 35)                   # обертаємо root на 35°
tip_rot = shift_airfoil(root_rot, 35, 200.0)  # зсуваємо на 200 мм

save_airfoil("tip_airfoil.dat", tip_rot)
