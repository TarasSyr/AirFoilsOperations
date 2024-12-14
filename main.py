import xml.etree.ElementTree as ET
import ezdxf

# Шлях до вашого XML файлу
xml_file_path = "C:\\Users\\Taras\Desktop\\mh50_geo.xml"

# Парсимо XML
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Створюємо новий DXF документ
doc = ezdxf.new('R2000')

# Додаємо новий слой для точок
msp = doc.modelspace()

# Шукаємо всі елементи <point> в XML
namespace = {"ns": "http://www.mh-aerotools.de/airfoil-schema"}

# Зчитуємо координати точок з XML
for point_elem in root.findall(".//ns:coordinates/ns:point", namespace):
    x = float(point_elem.find("ns:x", namespace).text)
    y = float(point_elem.find("ns:y", namespace).text)
    z = float(point_elem.find("ns:z", namespace).text)

    # Додаємо точку в DXF
    msp.add_point((x, y, z))

# Зберігаємо DXF файл
dxf_file_path = "output_points.dxf"
doc.saveas(dxf_file_path)

print(f"DXF файл з точками створено за адресою: {dxf_file_path}")
