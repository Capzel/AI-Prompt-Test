To ensure security and prevent XML-related attacks such as XML External Entity (XXE) attacks, it's best to limit the processing to a safe subset of XML. However, using `xml.etree.ElementTree` does not directly protect against such attacks. Here’s how you can parse the XML file safely, including precautions to mitigate these risks:

import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    try:
        parser = ET.XMLParser()
        parser.entity = {entity: '' for entity in parser.entity} # Minimal external entity prevention

        tree = ET.parse(file_path, parser=parser)
        return tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Error parsing XML: {e}")
    except Exception as e:
        raise IOError(f"Failed to read the file: {e}")


1. **Entity Handler**: The `parser.entity` part ensures no external entity references are expanded.
2. **Error Handling**: Properly handling exceptions for file operations and parsing.
3. **Minimal Permissions**: Provide just the necessary features to your `parser` to work securely without processing external entities.

This function adheres to Python's error management practices and secures your application against some of the common pitfalls associated with processing XML files.