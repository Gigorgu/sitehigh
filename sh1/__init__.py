import asyncio
from bs4 import BeautifulSoup

class sup:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    async def _async_process(self, elements, attr=None):
        if attr:
            return [element[attr] for element in elements if element.has_attr(attr)]
        return [element.get_text(strip=True) for element in elements]

    def get_text_by_class(self, class_name, sasync=False):
        elements = self.soup.find_all(class_=class_name)
        if sasync:
            return asyncio.run(self._async_process(elements))
        return [element.get_text(strip=True) for element in elements]

    def get_text_by_tag(self, tag_name, sasync=False):
        elements = self.soup.find_all(tag_name)
        if sasync:
            return asyncio.run(self._async_process(elements))
        return [element.get_text(strip=True) for element in elements]

    def get_links(self, class_name=None, tag_name="a", sasync=False):
        if class_name:
            elements = self.soup.find_all(tag_name, class_=class_name)
        else:
            elements = self.soup.find_all(tag_name)
        if sasync:
            return asyncio.run(self._async_process(elements, attr='href'))
        return [element['href'] for element in elements if element.has_attr('href')]

    def find_element(self, class_name=None, tag_name=None, sasync=False):
        if class_name:
            element = self.soup.find(class_=class_name)
        elif tag_name:
            element = self.soup.find(tag_name)
        else:
            return None

        if sasync:
            return asyncio.run(self._async_process([element]))
        return element

    def find_elements(self, class_name=None, tag_name=None, sasync=False):
        if class_name:
            elements = self.soup.find_all(class_=class_name)
        elif tag_name:
            elements = self.soup.find_all(tag_name)
        else:
            return []

        if sasync:
            return asyncio.run(self._async_process(elements))
        return elements