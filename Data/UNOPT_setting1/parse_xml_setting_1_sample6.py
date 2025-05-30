To parse an XML file in Python, you can use the `xml.etree.ElementTree` module in the standard library. Here's a basic example of how to do it:

Suppose you have an XML file named `example.xml` with the following content:

<?xml version="1.0"?>
<data>
    <items>
        <item name="item1" value="value1" />
        <item name="item2" value="value2" />
    </items>
    <info>
        <description>A simple XML file</description>
        <version>1.0</version>
    </info>
</data>

Here's Python code to parse this XML file and print its contents:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')

root = tree.getroot()

print(f"Root tag: {root.tag}")

print("\nItems:")
for item in root.find('items'):
    print(f"Name: {item.attrib['name']}, Value: {item.attrib['value']}")

info = root.find('info')
description = info.find('description').text
version = info.find('version').text

print("\nInfo Section:")
print(f"Description: {description}")
print(f"Version: {version}")

1. **Parsing the XML:** The `ET.parse('filename')` function is used to read and parse your XML file into an ElementTree object.
2. **Getting the Root Element:** `getroot()` retrieves the root element of the parsed XML.
3. **Navigating the XML Tree:** You can then navigate through elements and access attributes using methods like `find()` (which returns the first matching subelement) and `findall()` (which returns all matching subelements).
4. **Accessing Attributes and Text:** Attributes are dictionary-like (`item.attrib['name']`), and the textual content of an element can be accessed with `.text`.

This method is great for small to moderately-sized XML files.