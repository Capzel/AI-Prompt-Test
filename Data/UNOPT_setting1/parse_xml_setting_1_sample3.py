To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the standard library. Below, I will provide an example of how to read and parse an XML file using this module.

Let's say you have the following XML file named `example.xml`:

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

Here’s how you can parse this XML file in Python:

import xml.etree.ElementTree as ET

try:
    tree = ET.parse('example.xml')
    root = tree.getroot()
except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
except FileNotFoundError:
    print("The file example.xml was not found.")

print(f"Root Element: {root.tag}")

for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    print(f"Country: {name}, Rank: {rank}, Year: {year}, GDP per Capita: {gdppc}")

    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f"  Neighbor: {neighbor_name}, Direction: {direction}")



- **`ET.parse('example.xml')`:** This loads and parses the XML from a file.
- **`.getroot()`:** Returns the root element of the XML document.
- **`root.tag`:** Gives you the tag name of the root element.
- **`root.findall('country')`:** Finds all direct