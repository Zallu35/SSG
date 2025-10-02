import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    #HTMLNode tests (mine, before I realized how unittest actually works)
    def test_one(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "key2": "value2", "Three": "This ought to be enough"})
        print(node.props_to_html())

    def test_two(self):
        cnode1 = HTMLNode(tag="a", value="I'm a child!")
        cnode2 = HTMLNode(tag="p", value="I'm hungry")
        node2 = HTMLNode(tag="h1", value="I don't really know what I'm doing and that's okay", children=[cnode1, cnode2], props={"don't": "ask"})
        print(node2)
        print(cnode1, cnode2)

    #soultion file tests (for reference)
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    #LeafNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        print(node.props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), '<b>Hello, world!</b>')

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), '<i>Hello, world!</i>')

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "Hello, world!")
        self.assertEqual(node.to_html(), '<code>Hello, world!</code>')

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), 'Hello, world!')

    def test_leaf_to_html_fail(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)


    #ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()