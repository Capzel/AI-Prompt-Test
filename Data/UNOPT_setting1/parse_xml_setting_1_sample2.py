To parse an XML file in Python, you can use the built-in `xml.etree.ElementTree` module, which provides a simple and efficient way to read and manipulate XML data. Below is an example of how you can use this module to parse an XML file:

Suppose you have an XML file named `example.xml` with the following content:

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
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
    </country>
</data>

Here's how you can parse this XML file using `xml.etree.ElementTree`:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')

root = tree.getroot()

for country in root.findall('country'):
    name = country.get('name')  # Attribute: name
    rank = country.find('rank').text  # Element: rank
    year = country.find('year').text  # Element: year
    gdppc = country.find('gdppc').text  # Element: gdppc

    print(f"Country: {name}")
    print(f"  Rank: {rank}")
    print(f"  Year: {year}")
    print(f"  GDP per capita: {gdppc}")

    neighbor = country.find('neighbor')
    neighbor_name = neighbor.get('name')
    neighbor_direction = neighbor.get('direction')
    
    print(f"  Neighbor: {neighbor_name} (Direction: {neighbor_direction})")

In this example, we:

1. Used `ET.parse()` to load and parse `example.xml` into an `ElementTree` object.
2. Accessed the root element of the XML structure using `getroot()`.
3. Iterated over all `country` elements found under the root.
4. Extracted attribute values using `element.get('attribute_name')`.
5. Extracted text content of a sub-element using `element.find('sub_element').text`.
6. In this example, iterated the `neighbor`