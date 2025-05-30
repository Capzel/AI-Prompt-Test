import xml.etree.ElementTree as ET
import os

def parse_xml_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("The specified file does not exist")

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return ET.ElementTree(root)
    except ET.ParseError as e:
        raise ValueError("Failed to parse XML") from e