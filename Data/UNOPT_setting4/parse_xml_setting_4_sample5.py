To parse an XML file in Python, you can use the `xml.etree.ElementTree` module, which is part of the standard library. Here's a step-by-step guide on how to do it:

1. **Import the ElementTree module**: You need to import the module to work with XML data.

2. **Load the XML file**: Use `ElementTree.parse()` to load and parse the XML file.

3. **Get the root element**: Once the XML is parsed, you can get the root element of the XML tree.

4. **Navigate through the XML tree**: You can iterate over elements, access their attributes, and get their text content.

Here's an example:

Suppose you have an XML file named `example.xml` with the following content:

<library>
    <book id="1">
        <title>Python Programming</title>
        <author>John Doe</author>
    </book>
    <book id="2">
        <title>Data Science Handbook</title>
        <author>Jane Smith</author>
    </book>
</library>

You can parse and extract information from this XML file using the following Python code:

import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')

root = tree.getroot()

for book in root.findall('book'):
    book_id = book.get('id')
    
    title = book.find('title').text
    author = book.find('author').text
    
    print(f'Book ID: {book_id}')
    print(f'Title: {title}')
    print(f'Author: {author}')
    print('---')


- **`ET.parse('example.xml')`**: This loads and parses the XML file into an `ElementTree` object.
- **`tree.getroot()`**: This retrieves the root element of the XML tree, which is `<library>` in this case.
- **`root.findall('book')`**: This finds all `<book>` elements under the root.
- **`book.get('id')`**: This retrieves the value of the `id` attribute of the `<book>` element.
- **`book.find('title').text`**: This finds the `<title>` element within `<book>` and retrieves its text content.
- **`book.find('author').text`**: Similarly, this retrieves the text content of the `<author>` element.

This code will output:

Book ID: 1
Title: Python Programming
Author: John Doe
---
Book ID: 2