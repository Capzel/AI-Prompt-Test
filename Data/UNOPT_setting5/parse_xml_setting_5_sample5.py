To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the standard library. Here's a basic example of how to parse an XML file using this module:

1. **Read the XML file**: First, you need to load the XML file into your program.
2. **Parse the XML**: Use `ElementTree` to parse the XML data.
3. **Navigate the XML tree**: Access elements and their attributes.

Here's a step-by-step example:

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

    print(f"\nCountry: {name}")
    print(f"  Rank: {rank}")
    print(f"  Year: {year}")
    print(f"  GDP per capita: {gdppc}")

    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f"  Neighbor: {neighbor_name} (Direction: {direction})")


- **`ET.parse('example.xml')`**: This loads and parses the XML file, returning an `ElementTree` object.
- **`tree.getroot()`**: This retrieves the