from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    PLAIN = "Plain"
    ITALIC = "Italic"
    BOLD = "Bold"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    tag_type = {
        "Plain": None,
        "Bold": "b",
        "Italic": "i",
        "Code": "code",
        "Link": "a",
        "Image": "img",
    }
    if text_node.text_type.value == "Link":
        return LeafNode(tag_type["Link"], text_node.text, {"href": text_node.url})
    if text_node.text_type.value == "Image":
        return LeafNode(tag_type["Image"], "", {"src": text_node.url, "alt": text_node.text})
    return LeafNode(tag_type[text_node.text_type.value], text_node.text)