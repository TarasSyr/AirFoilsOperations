import xml.etree.ElementTree as ET

# Вказуємо шлях до вашого XML файлу
xml_file = "C:\\Users\\Taras\Desktop\\mh50_geo.xml"

# Завантажуємо XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Простір імен, який використовується в XML
namespace = {'airfoil': 'http://www.mh-aerotools.de/airfoil-schema'}

# Витягуємо всі точки з елементів <coordinates> та <point>
points = []
for point in root.findall(".//airfoil:coordinates//airfoil:point", namespace):
    x = point.find('airfoil:x', namespace).text
    y = point.find('airfoil:y', namespace).text
    z = point.find('airfoil:z', namespace).text
    points.append(f"{x} {y} {z}")  # Форматуємо у вигляді x y z

# Записуємо координати в текстовий файл
with open('output_points.txt', 'w') as f:
    for point in points:
        f.write(point + '\n')

print("Точки успішно записані у файл output_points.txt")
