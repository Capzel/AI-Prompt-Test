To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the standard library. Here's a basic example of how to parse an XML file using this module:

Suppose you have an XML file named `example.xml` with the following content:

<?xml version="1.0"?>
<data>
    <item>
        <name>Item 1</name>
        <value>10</value>
    </item>
    <item>
        <name>Item 2</name>
        <value>20</value>
    </item>
</data>

Here's how you can parse this XML file in Python:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

for item in root.findall('item'):
    name = item.find('name').text
    value = item.find('value').text
    
    print(f'Name: {name}, Value: {value}')


1. **Import the Module**: First, import the `ElementTree` module from the `xml.etree` package.

2. **Parse the XML File**: Use `ET.parse('example.xml')` to load and parse the XML file. This returns an `ElementTree` object.

3. **Get the Root Element**: Use `tree.getroot()` to get the root element of the XML document.

4. **Find Elements**: Use `root.findall('item')` to find all `item` elements under the root. This returns a list of elements.

5. **Access Element Text**: For each `item`, use `item.find('name').text` and `item.find('value').text` to access the text content of the `name` and `value` sub-elements.

6. **Print the Results**: Print the name and value for each item.

This example demonstrates basic XML parsing. If you need to handle more complex XML structures or namespaces, you might need to use additional features of the `ElementTree` module or consider using other libraries like `lxml` or `xmltodict` for more advanced use cases.