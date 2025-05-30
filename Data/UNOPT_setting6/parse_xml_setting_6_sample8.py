Parsing an XML file in Python can be done using several libraries, with `xml.etree.ElementTree`, `lxml`, and `minidom` being some of the most commonly used. Below, I'll demonstrate how to parse an XML file using `xml.etree.ElementTree`, which is included in Python's standard library.

Suppose you have an XML file named `example.xml` with the following content:

<data>
    <item>
        <name>Item1</name>
        <value>123</value>
    </item>
    <item>
        <name>Item2</name>
        <value>456</value>
    </item>
</data>

Here's how you can parse this XML file using `xml.etree.ElementTree`:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

for item in root.findall('item'):
    name = item.find('name').text
    value = item.find('value').text
    print(f'Item Name: {name}, Value: {value}')

1. **Import the library**: `xml.etree.ElementTree` is imported as `ET`.
2. **Parse the XML file**: Use `ET.parse('example.xml')` to parse the file, which returns an ElementTree object.
3. **Get the root element**: Use `tree.getroot()` to access the root element of the XML.
4. **Iterate over elements**: Use `root.findall('item')` to find all `item` elements.
5. **Extract data**: For each `item`, use `.find('tagname').text` to access the text content of the desired sub-elements (`name` and `value` in this case).

This will output:
Item Name: Item1, Value: 123
Item Name: Item2, Value: 456

If you need more advanced XML processing capabilities, you might consider using the `lxml` library, which provides more powerful features but isn't included in the standard library.