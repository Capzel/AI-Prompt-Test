To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the Python standard library. Here's a step-by-step guide on how to do it:

1. **Import the ElementTree module**: You need to import the `ElementTree` module from `xml.etree`.

2. **Load the XML file**: Use the `parse` function to load and parse the XML file.

3. **Access elements**: Once the XML is parsed, you can access elements using various methods provided by the `ElementTree` module.

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
</data>

Here's how you can parse this XML file in Python:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')

root = tree.getroot()

print(f"Root element: {root.tag}")

for country in root.findall('country'):
    name = country.get('name')
    print(f"\nCountry: {name}")

    rank = country.find('rank').text
    print(f"Rank: {rank}")

    year = country.find('year').text
    print(f"Year: {year}")

    gdppc = country.find('gdppc').text
    print(f"GDP per capita: {gdppc}")

    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f"Neighbor: {neighbor_name}, Direction: {direction}")


- **`ET.parse('example.xml')`**: This loads and parses the XML file into an `ElementTree` object.
- **`tree.getroot()`**: This retrieves the root element