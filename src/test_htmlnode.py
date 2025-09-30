import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_one(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "key2": "value2", "Three": "This ought to be enough"})
        print(node.props_to_html())

    def test_two(self):
        cnode1 = HTMLNode(tag="a", value="I'm a child!")
        cnode2 = HTMLNode(tag="p", value="I'm hungry")
        node2 = HTMLNode(tag="h1", value="I don't really know what I'm doing and that's okay", children=[cnode1, cnode2], props={"don't": "ask"})
        print(node2)
        print(cnode1, cnode2)

if __name__ == "__main__":
    unittest.main()