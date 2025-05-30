To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the Python standard library. Here's a step-by-step guide on how to do it:

1. **Import the ElementTree module**: First, you need to import the module.

2. **Parse the XML file**: Use the `parse` function to read the XML file and get the root element.

3. **Navigate the XML tree**: Once you have the root element, you can navigate through the XML tree using various methods provided by the ElementTree API.

Here's an example to illustrate these steps:

Suppose you have an XML file named `example.xml` with the following content:

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E" />
        <neighbor name="Switzerland" direction="W" />
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N" />
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W" />
        <neighbor name="Colombia" direction="E" />
    </country>
</data>

Here's how you can parse this XML file in Python:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

print(f"Root element: {root.tag}")

for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    
    print(f"Country: {name}")
    print(f"  Rank: {rank}")
    print(f"  Year: {year}")
    print(f"  GDP per capita: {gdppc}")
    
    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f"  Neighbor: {neighbor_name}, Direction: {direction}")



- **`ET.parse('example.xml')`**: This function reads the XML file and returns