import unittest
from Markdown_Functions import markdown_to_blocks, BlockType, block_to_block_type

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
