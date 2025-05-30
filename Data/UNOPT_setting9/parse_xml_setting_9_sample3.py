To parse an XML file in Python, you can use several libraries, but one of the most commonly used is `xml.etree.ElementTree`, which is included in the Python standard library. Here's a basic example of how to use it:

Let's assume you have an XML file named `example.xml` with the following content:

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


Here's how you can parse this XML file using `xml.etree.ElementTree`:

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


- **Importing the Library**: We import `xml.etree.ElementTree` as `ET`.
- **Parsing the XML**: We use `ET.parse('example.xml')` to load and parse the XML file.
- **Getting the Root Element**: `tree.getroot()` returns the root element of the XML.
- **Iterating Over Elements**: We use `root.findall('country')` to find all `