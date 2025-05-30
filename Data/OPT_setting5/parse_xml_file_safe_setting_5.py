import xml.etree.ElementTree as ET
from defusedxml.ElementTree import parse

def parse_xml_file(file_path):
    try:
        tree = parse(file_path)
        root = tree.getroot()
        return ET.ElementTree(root)
    except ET.ParseError as e:
        raise ValueError("Failed to parse XML file") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred") from e