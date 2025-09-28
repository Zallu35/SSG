from enum import Enum

class TextType(Enum):
    Plain = "Plain"
    Italic = "Italic"
    Bold = "Bold"
    Code = "Code"
    Link = "Link"
    Image = "Image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"({self.text}, {self.text_type.value}, {self.url})"