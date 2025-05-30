To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the standard library. Here's a basic example of how to parse an XML file using this module:

First, let's assume you have an XML file named `example.xml` with the following content:

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

You can parse this XML file using the following Python code:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

for item in root.findall('item'):
    name = item.find('name').text
    value = item.find('value').text
    
    print(f'Name: {name}, Value: {value}')


1. **Import the Module**: The `xml.etree.ElementTree` module is imported as `ET`.

2. **Parse the XML File**: The `ET.parse('example.xml')` function reads and parses the XML file, returning an `ElementTree` object.

3. **Get the Root Element**: The `getroot()` method of the `ElementTree` object returns the root element of the XML.

4. **Find Elements**: The `findall('item')` method is used to find all `item` elements under the root. This returns a list of elements.

5. **Access Element Data**: For each `item`, the `find('name')` and `find('value')` methods are used to access the `name` and `value` elements, respectively. The `text` attribute of these elements contains the actual text data.

6. **Print the Data**: The extracted data is printed to the console.

This is a simple example. For more complex XML files, you might need to handle namespaces, attributes, or nested elements. The `xml.etree.ElementTree` module provides various methods to help with these tasks.