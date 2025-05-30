To safely parse an XML file using `xml.etree.ElementTree`, it's crucial to avoid vulnerabilities like XML external entity (XXE) attacks. Here's a secure implementation of `parse_xml_file`:

import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    """
    Safely parses an XML file and returns its structured representation.
    
    :param file_path: Path to the XML file.
    :return: An ElementTree Element representing the root of the parsed XML.
    """
    try:
        tree = ET.parse(file_path, parser=ET.XMLParser(resolve_entities=False))
        return tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse XML file: {e}")
    except FileNotFoundError:
        raise ValueError("The specified file was not found.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")


- **XML External Entity (XXE) Protection**: By default, `xml.etree.ElementTree` is safe against XXE, but explicitly disabling entity resolution (`resolve_entities=False`) ensures no external entities are processed.
- **Error Handling**: Handles `ParseError` for XML parsing issues and `FileNotFoundError` for missing files, raising a `ValueError` with descriptive messages.
- **General Exception Handling**: Catches unexpected exceptions to avoid leaking sensitive information.

This approach ensures the XML is parsed securely, while providing meaningful error messages in case of failure.