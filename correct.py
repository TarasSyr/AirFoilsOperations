import math
import csv

inp = "txt/naca0009.txt"
outp = "txt/naca0009.txt"

def dist(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

# зчитуємо csv (будь-який роздільник)
with open(inp, "r", encoding="utf-8", errors="ignore") as f:
    sniffer = csv.Sniffer()
    sample = f.read(2048)
    f.seek(0)
    dialect = sniffer.sniff(sample, delimiters=",; \t")
    reader = csv.reader(f, dialect)
    rows = list(reader)

# пропускаємо перші 3 службові рядки
pts = []
for i, row in enumerate(rows):
    if i < 3:
        continue
    if len(row) >= 2:
        try:
            x = float(row[0]); y = float(row[1])
            pts.append((x,y))
        except:
            pass

# 1) прибираємо точні дублікати підряд
clean = []
for p in pts:
    if not clean or (p[0]!=clean[-1][0] or p[1]!=clean[-1][1]):
        clean.append(p)

# 2) обрізаємо на першому великому стрибку (евристика)
#    поріг підбери під свої одиниці; тут 5% від макс. розмаху по X
xs = [p[0] for p in clean]
thr = 0.05*(max(xs)-min(xs) if xs else 1.0)

trimmed = [clean[0]]
for i in range(1,len(clean)):
    if dist(clean[i], clean[i-1]) > thr:
        # вважаємо, що почалося друге коло/стрибок — зупиняємось
        break
    trimmed.append(clean[i])

# 3) прибираємо дубль TE (0,0,0) якщо є більше одного разу
#    залишимо тільки першу появу
seen_zeros = False
final = []
for x,y in trimmed:
    if abs(x) < 1e-12 and abs(y) < 1e-12:
        if seen_zeros:
            continue
        seen_zeros = True
    final.append((x,y))

# 4) запис у TXT X Y Z
with open(outp, "w", encoding="utf-8") as f:
    for x,y in final:
        f.write(f"{x} {y} 0.0\n")

print("OK:", outp, "точок:", len(final))
