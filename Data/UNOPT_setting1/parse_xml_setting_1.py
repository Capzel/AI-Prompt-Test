import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

file_path = 'yourfile.xml'
root = parse_xml(file_path)

for child in root:
    print(child.tag, child.attrib)