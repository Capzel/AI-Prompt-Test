import xml.etree.ElementTree as ET
from defusedxml import ElementTree as SafeET

def parse_xml_file(file_path):
    try:
        tree = SafeET.parse(file_path)
        root = tree.getroot()
        
        def recurse_xml(element):
            return {
                'tag': element.tag,
                'attributes': element.attrib,
                'text': element.text.strip() if element.text and element.text.strip() else None,
                'children': [recurse_xml(child) for child in element]
            }
        
        return recurse_xml(root)
    except (SafeET.ParseError, ET.ParseError) as e:
        return {'error': str(e)}