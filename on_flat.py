import numpy as np

# ---------- Параметри, які можна підкрутити ----------
WIN =  nine = 7           # розмір ковзного вікна (непарне число 7–13 зазвичай ок)
SAVE_AS = "txt/clarky_solidworks_25mm_moved_flat.txt"

# ---------- Завантаження даних ----------
data = np.loadtxt("txt/clarky_solidworks_25mm_moved.txt")  # очікується N x 3
if data.shape[1] < 2:
    raise ValueError("Очікую принаймні 2 колонки (X, Y). У тебе менше.")

xy = data[:, :2].copy()
z  = data[:, 2] if data.shape[1] >= 3 else np.zeros(len(data))

x = xy[:,0]
y = xy[:,1]
N = len(xy)

# ---------- Знайти хвостову кромку (TE) як мінімум X ----------
idx_te = int(np.argmin(x))  # у твоїх даних TE ~ x = -250
# Нижня поверхня: від TE до кінця (типова нумерація як у тебе)
lower = xy[idx_te:, :]
if len(lower) < 5:
    # Фолбек: якщо дані в іншому порядку — беремо нижні 35% за Y
    y_thr = np.percentile(y, 35)
    lower = xy[y <= y_thr]
    if len(lower) < 5:
        raise ValueError("Не вдалося виділити нижню поверхню. Перевір порядок точок.")

# ---------- Ковзне вікно: знаходимо майже-горизонтальну ділянку ----------
L = len(lower)
if L <= WIN:
    WIN = max(5, L - 1 - (L % 2 == 0))  # підлаштуємо розмір вікна

best_i = None
best_abs_slope = None
best_mean_y = None

for i in range(0, L - WIN + 1):
    seg = lower[i:i+WIN]
    # Лінійна апроксимація Y = m*X + b
    m, b = np.polyfit(seg[:,0], seg[:,1], 1)
    abs_m = abs(m)
    mean_y = seg[:,1].mean()
    # Критерій: мінімальний |нахил|, при рівних – нижчий середній Y
    if (best_abs_slope is None or
        abs_m < best_abs_slope or
        (np.isclose(abs_m, best_abs_slope, rtol=1e-3, atol=1e-6) and mean_y < best_mean_y)):
        best_i = i
        best_abs_slope = abs_m
        best_mean_y = mean_y
        best_m, best_b = m, b

if best_i is None:
    raise RuntimeError("Не знайшов плоску ділянку на нижній поверхні.")

# ---------- Кут повороту (в протилежний бік нахилу) ----------
angle = np.arctan(best_m)
R = np.array([[ np.cos(-angle), -np.sin(-angle)],
              [ np.sin(-angle),  np.cos(-angle)]])

xy_rot = xy @ R.T

# ---------- “Поставити на стіл”: мінімальний Y -> 0 ----------
xy_rot[:,1] -= xy_rot[:,1].min()

# ---------- Повернути Z та зберегти ----------
out = np.column_stack([xy_rot, z])
np.savetxt(SAVE_AS, out, fmt="%.6f")

# Для контролю:
deg = np.degrees(angle)
print(f"Виявлений кут нахилу нижньої полиці: {deg:.4f}°")
print(f"Збережено: {SAVE_AS}; рядків: {len(out)}")
