**Import Statement**
```python
from sh1 import sup
```

**Overview**
The `sup` class is designed to parse HTML content using `BeautifulSoup`. It allows you to extract text, find elements, and retrieve links. All methods support both synchronous and asynchronous processing by setting the `sasync` flag.

### **Class Methods**

1. **`__init__(html)`**:
   - Initializes the `sup` class with an HTML string.
   - **Parameters**:
     - `html (str)`: The HTML content to be parsed.

2. **`get_text_by_class(class_name, sasync=False)`**:
   - Extracts the text from elements with a specific class.
   - **Parameters**:
     - `class_name (str)`: The class name to filter elements.
     - `sasync (bool)`: Set to `True` to run asynchronously.
   - **Returns**:
     - A list of strings containing the text from the selected elements.

3. **`get_text_by_tag(tag_name, sasync=False)`**:
   - Extracts the text from elements with a specific tag.
   - **Parameters**:
     - `tag_name (str)`: The tag name to filter elements.
     - `sasync (bool)`: Set to `True` to run asynchronously.
   - **Returns**:
     - A list of strings containing the text from the selected elements.

4. **`get_links(class_name=None, tag_name="a", sasync=False)`**:
   - Extracts the `href` attributes from anchor tags (or other tags) with a specific class (if provided).
   - **Parameters**:
     - `class_name (str, optional)`: The class name to filter elements. If not provided, it selects all elements by tag.
     - `tag_name (str, optional)`: The tag name to search for links. Default is `"a"`.
     - `sasync (bool)`: Set to `True` to run asynchronously.
   - **Returns**:
     - A list of strings containing the URLs (`href` attributes) from the selected elements.

5. **`find_element(class_name=None, tag_name=None, sasync=False)`**:
   - Finds the first element by class name or tag name.
   - **Parameters**:
     - `class_name (str, optional)`: The class name to filter the elements.
     - `tag_name (str, optional)`: The tag name to filter the elements.
     - `sasync (bool)`: Set to `True` to run asynchronously.
   - **Returns**:
     - The first matching element, or `None` if no match is found.

6. **`find_elements(class_name=None, tag_name=None, sasync=False)`**:
   - Finds all elements by class name or tag name.
   - **Parameters**:
     - `class_name (str, optional)`: The class name to filter the elements.
     - `tag_name (str, optional)`: The tag name to filter the elements.
     - `sasync (bool)`: Set to `True` to run asynchronously.
   - **Returns**:
     - A list of elements matching the class or tag.

### **Asynchronous Execution**
- All methods support asynchronous processing by setting the `sasync` flag to `True`. This utilizes Python’s `asyncio` library to run the methods asynchronously, which can be useful when dealing with large HTML files or when you want to perform non-blocking operations.


```python
from sitehigh.sh1 import sup

# Test HTML content
html_content = """
<html>
    <body>
        <a href="https://example.com">Link 1</a>
        <a href="https://test.com" class="test">Link 2</a>
        <p class="content">This is a paragraph.</p>
        <p class="content">Another paragraph.</p>
    </body>
</html>
"""

# Initialize the class with HTML content
soup_instance = sup(html_content)

# Test 1: Get text by class (synchronous)
text_by_class = soup_instance.get_text_by_class("content")
assert text_by_class == ['This is a paragraph.', 'Another paragraph.']

# Test 2: Get text by class (asynchronous)
text_by_class_async = soup_instance.get_text_by_class("content", sasync=True)
assert text_by_class_async == ['This is a paragraph.', 'Another paragraph.']

# Test 3: Get text by tag (synchronous)
text_by_tag = soup_instance.get_text_by_tag("p")
assert text_by_tag == ['This is a paragraph.', 'Another paragraph.']

# Test 4: Get text by tag (asynchronous)
text_by_tag_async = soup_instance.get_text_by_tag("p", sasync=True)
assert text_by_tag_async == ['This is a paragraph.', 'Another paragraph.']

# Test 5: Get links (synchronous)
links = soup_instance.get_links()
assert links == ['https://example.com', 'https://test.com']

# Test 6: Get links with class filter (asynchronous)
links_async = soup_instance.get_links(class_name="test", sasync=True)
assert links_async == ['https://test.com']

# Test 7: Find first element by tag (synchronous)
first_element = soup_instance.find_element(tag_name="p")
assert str(first_element) == '<p class="content">This is a paragraph.</p>'

# Test 8: Find first element by class (asynchronous)
first_element_async = soup_instance.find_element(class_name="content", sasync=True)
assert str(first_element_async) == '<p class="content">This is a paragraph.</p>'

# Test 9: Find all elements by class (synchronous)
elements = soup_instance.find_elements(class_name="content")
assert len(elements) == 2

# Test 10: Find all elements by class (asynchronous)
elements_async = soup_instance.find_elements(class_name="content", sasync=True)
assert len(elements_async) == 2
