To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the Python standard library. Here's a step-by-step guide on how to do it:

1. **Import the ElementTree module**: First, you need to import the `ElementTree` module.

2. **Parse the XML file**: Use the `parse()` function to read and parse the XML file.

3. **Get the root element**: Once the XML is parsed, you can get the root element of the XML tree.

4. **Navigate through the XML tree**: You can iterate over the elements and access their attributes and text.

Here's an example:

Suppose you have an XML file named `example.xml` with the following content:

<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
   </book>
</catalog>

Here's how you can parse this XML file in Python:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')

root = tree.getroot()

print(f"Root element: {root.tag}")

for book in root.findall('book'):
    book_id = book.get('id')
    print(f"\nBook ID: {book_id}")

    author = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text

    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Genre: {genre}")
    print(f"Price: {price}")
    print(f"Publish Date: {publish_date}")
    print(f"Description: {description}")
``