To safely parse an XML file using `xml.etree.ElementTree`, it's important to be aware of potential security issues such as XML External Entity (XXE) attacks. In Python's standard library, `xml.etree.ElementTree` does not support external entities, which makes it safer by default. However, it's still good practice to handle files carefully and ensure that the file path is valid and the file exists.

Here's a safe implementation of the `parse_xml_file` function:

import os
import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse XML file: {e}")


1. **File Existence Check**: Before attempting to parse, the function checks if the file exists to prevent errors.
2. **Error Handling**: It handles parsing errors gracefully by catching `ET.ParseError` and raising a more descriptive error.
3. **Security Considerations**: By using `xml.etree.ElementTree`, which does not process external entities, the function is inherently safer against XXE attacks.