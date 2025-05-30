To parse an XML file in Python, you commonly use libraries such as `xml.etree.ElementTree`, `minidom` from the `xml.dom` package, or well-known third-party libraries like `lxml` or `BeautifulSoup`. Here's a basic example of how to parse an XML file using `xml.etree.ElementTree`, which is included with Python's standard library.

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
        <rank>2</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>3</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>


Here's how you can parse the XML using `xml.etree.ElementTree` in Python:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

print(f"Root tag: {root.tag}")

for child in root:
    print(f"Child tag: {child.tag}, Attributes: {child.attrib}")

for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text

    print(f"Country: {name}, Rank: {rank}, Year: {year}, GDP per capita: {gdppc}")

    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f"   Neighbor: {neighbor_name}, Direction: {direction}")

- `ET.parse('example.xml')`: Parses the XML file and returns an `ElementTree` object.
- `tree.getroot()`: Returns the root element of the XML tree.
- `root.findall('country')`: Finds all `country` sub-elements under the root.
- `.get('attribute_name')`: Retrieves