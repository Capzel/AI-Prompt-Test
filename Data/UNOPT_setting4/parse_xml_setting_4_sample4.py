Parsing an XML file in Python can be done using several libraries, but one of the most commonly used is `xml.etree.ElementTree`, which is included in the Python standard library. Here's a basic example of how to parse an XML file using this library:


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


import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    
    print(f'Country: {name}')
    print(f'  Rank: {rank}')
    print(f'  Year: {year}')
    print(f'  GDP per capita: {gdppc}')
    
    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        direction = neighbor.get('direction')
        print(f'  Neighbor: {neighbor_name}, Direction: {direction}')


1. **Import the Library**: We import `ElementTree` from the `xml.etree` module.

2. **Parse the XML File**: We use `ET.parse('example.xml')` to parse the XML file and get an `ElementTree` object.

3. **Get the Root Element**: `tree.getroot()` gives us the root element of the XML document.

4. **Iterate Over Elements**: We use `findall()` to iterate over specific elements. In this case, we look for all `country` elements.

5. **Access Element Attributes and Text**: We use `.get('attribute_name