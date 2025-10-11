import unittest
from Markdown_Functions import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node

class TestMkdFuncs(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line   

  

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_types_heading(self):
        dummystring = "##I just need to know how this works"
        self.assertEqual(block_to_block_type(dummystring), BlockType.HEADING)
        
    def test_block_types_code(self):
        dummystring = "```I just need to know how this works```"
        self.assertEqual(block_to_block_type(dummystring), BlockType.CODE)

    def test_block_types_quote(self):
        dummystring = ">I just need to know how this works\n>second line testing"
        self.assertEqual(block_to_block_type(dummystring), BlockType.QUOTE)

    def test_block_types_unordered_list(self):
        dummystring = "- I just need to know how this works\n- This should work nicely"
        self.assertEqual(block_to_block_type(dummystring), BlockType.UNORDERED_LIST)

    def test_block_types_ordered_list(self):
        dummystring = "1. I just need to know how this works\n2. Final logic check"
        self.assertEqual(block_to_block_type(dummystring), BlockType.ORDERED_LIST)

    def test_block_types_paragraph1(self):
        dummystring = "Everything else is a paragraph"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_block_types_paragraph2(self):
        dummystring = "```So lets make things fail`"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_block_types_paragraph3(self):
        dummystring = ">improper formatting\n is fun!"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_block_types_paragraph4(self):
        dummystring = "- I really like it when shit\n- doesn't work how\n I want it to :D"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_block_types_paragraph5(self):
        dummystring = "1. Write more tests or\n2. you'll be disappointed\n. in yourself!"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_block_types_paragraph6(self):
        dummystring = "1. What if EVERYTHING else\n3. is actually just a paragraph\n2. somewhere...?"
        self.assertEqual(block_to_block_type(dummystring), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_header(self):
        md = """
# I'm testing headers

## I# also want to test stupid headers
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>I'm testing headers</h1><h2>I# also want to test stupid headers</h2></div>",
        )

    def test_quote(self):
        md = """
>I'm testing quotes
>I think this is gonna work!
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>I'm testing quotes I think this is gonna work!</blockquote></div>",
        )

    def test_ul(self):
        md = """
- I'm testing headers
- I# also want to test stupid headers
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>I'm testing headers</li><li>I# also want to test stupid headers</li></ul></div>",
        )

    def test_ol(self):
        md = """
1. I'm testing headers
2. I# also want to test stupid headers
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>I'm testing headers</li><li>I# also want to test stupid headers</li></ol></div>",
        )