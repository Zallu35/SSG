import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from Node_Augmentations import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


class TestNodeAugs(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #print(new_nodes)
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
        #print(matches)
        self.assertListEqual([("image link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links (self):
        matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        #print(matches)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_full_conversion(self):
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(test_text), [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

if __name__ == "__main__":
    unittest.main()