To parse an XML file in Python, you can use several libraries, but one of the most common and built-in options is the `xml.etree.ElementTree` module. Here's a simple example to help you get started with parsing an XML file using this module.

Suppose you have an XML file named `example.xml`:

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

Here's how you can parse this XML file using `xml.etree.ElementTree`:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

print(f"Root tag: {root.tag}")

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



1. **Import the Module**: Import `xml.etree.ElementTree` as `ET`.
2. **Parse the File**: Use `ET.parse('example.xml')` to load and parse the XML file.
3. **Get the Root Element**: Use `tree.getroot()` to get the root element of the XML structure.
4. **Iterate Over Elements**: Use methods like `findall` and `find` to iterate over elements and