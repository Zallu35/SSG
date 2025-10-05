import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from Node_Augmentations import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestNodeAugs(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(new_nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_bad_syntax(self):
        node = TextNode("This is text with `a `code block` word", TextType.PLAIN)
        self.assertRaises(Exception, split_nodes_delimiter)

    def test_eq_italic(self):
        node = TextNode("This is `code` text", TextType.PLAIN)
        node2 = TextNode("This is _italic_ text", TextType.PLAIN)
        node3 = TextNode("This is **skipped** text", TextType.BOLD)
        node4 = TextNode("This is **bold** text", TextType.PLAIN)
        node5 = TextNode("This is **bold text with `code` inside** it", TextType.PLAIN)
        
        new_nodes=split_nodes_delimiter([node2], "_", TextType.ITALIC)
        
        #print(new_nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.PLAIN),
        ])

    def test_eq_bold(self):
        node3 = TextNode("This is **skipped** text", TextType.BOLD)
        node4 = TextNode("This is **bold** text", TextType.PLAIN)
        node5 = TextNode("This is **bold text with `code` inside** it", TextType.PLAIN)
        new_nodes=split_nodes_delimiter([node3, node4, node5], "**", TextType.BOLD)
        # print(new_nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is **skipped** text", TextType.BOLD),
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.PLAIN),
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold text with `code` inside", TextType.BOLD),
            TextNode(" it", TextType.PLAIN),
        ])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image link](https://i.imgur.com/zjjcJKZ.png)"
        )
        print(matches)
        self.assertListEqual([("image link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links (self):
        matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        print(matches)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()