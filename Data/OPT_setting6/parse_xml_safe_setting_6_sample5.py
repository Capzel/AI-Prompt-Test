To ensure secure parsing of XML, it's crucial to avoid vulnerabilities like XML External Entity (XXE) attacks. The `xml.etree.ElementTree` module in Python's standard library provides a safe way to parse XML files, provided we use it correctly. Below is a function `parse_xml_file` that safely parses an XML file using this module:

import xml.etree.ElementTree as ET
from typing import Any

def parse_xml_file(file_path: str) -> Any:
    """
    Safely parse an XML file and return its structured representation.
    
    :param file_path: Path to the XML file to be parsed.
    :return: Structured representation of the XML file.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        return root
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse XML file: {e}")
    except FileNotFoundError:
        raise ValueError("The specified file was not found.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")


- **Security**: The `ElementTree` module in Python's standard library is generally safe against XXE attacks since it doesn't process external entities.
- **Error Handling**: The function handles parsing errors, file not found errors, and any other unexpected exceptions by raising a `ValueError` with a descriptive message.
- **Simplicity**: The function returns the root element of the parsed XML tree. You can extend it to convert the XML into a dictionary or another structured format if needed.
  
By following these practices, you can securely parse XML files in Python.