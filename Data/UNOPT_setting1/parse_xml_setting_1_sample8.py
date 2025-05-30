Parsing an XML file in Python can be achieved using several libraries. The most popular ones are `xml.etree.ElementTree`, `minidom`, and `lxml`. Here's an example using each of these libraries:


This is a simple and efficient way to parse XML.

import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for elem in root.findall('element_tag'):
    print(elem.text)


This library is useful if you need a more classical DOM approach. It's included in Python's standard library.

from xml.dom import minidom

xmldoc = minidom.parse('data.xml')

itemlist = xmldoc.getElementsByTagName('item')
print("Number of elements:", len(itemlist))

for s in itemlist:
    print(s.attributes['attribute_name'].value)
    print(s.firstChild.nodeValue)


This is a third-party library that is very powerful and fast for XML processing.

from lxml import etree

tree = etree.parse('data.xml')
root = tree.getroot()

for element in root:
    print(element.tag, element.attrib)

for el in root.xpath(".//element_tag"):
    print(el.text)

For each approach featured above, you'd typically replace `'element_tag'`, `'attribute_name'`, and `'data.xml'` with the actual tag names and paths relevant to your XML file. Before using `lxml`, you need to install it using pip:

pip install lxml

Each library has its own advantages, so you can choose one that best fits your needs based on the complexity of your XML data, required features, and your preference for document object model (DOM) versus streaming interfaces like ElementTree provides.