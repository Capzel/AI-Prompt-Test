Parsing an XML file in Python can be done using several libraries, but one of the most commonly used is the built-in `xml.etree.ElementTree` module. Below is a basic example demonstrating how to parse an XML file using this module.

Suppose you have an XML file named `example.xml` with the following content:

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

Here is how you can parse this XML file using `xml.etree.ElementTree`:

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
        print(f'  Neighbor: {neighbor_name} ({direction})')


- **Import the module:** We start by importing `xml.etree.ElementTree` as `ET`.
- **Parse the XML file:** `ET.parse('example.xml')` reads the XML file and returns an `ElementTree` object.
- **Get the root element:** `tree.getroot()` gets the root element of the XML.
- **Iterate through elements:** Using `findall()`, we loop through each `<country>` element. We use `get()` to access attributes and `find()` to access child elements' text.
- **Nested iteration:** We also iterate