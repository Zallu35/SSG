from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType
from Node_Augmentations import split_nodes_image, extract_markdown_images, extract_markdown_links
from Markdown_Functions import markdown_to_blocks, block_to_block_type, markdown_to_html_node, extract_title
#from main import copy_dir, generate_page
import os
import shutil


def general_test():
    LN = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    HN = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com"})
    #print(LN)
    #print(HN)
    node2 = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN,
    )
    sections = node2.text.split(f"![second image](https://i.imgur.com/3elNhQu.png)", 1)
    #print(sections)

    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
    new_nodes = split_nodes_image([node])
    #print(new_nodes)

    #print(extract_markdown_images("this is not an image"))

    blocks = markdown_to_blocks("""
This is **bolded** paragraph

>This is another paragraph with _italic_ text and `code` here
>This is the same paragraph on a new line
>
>extra quote testing

- This is a list
- with items
""")
    #print(blocks)

    #print(block_to_block_type("```this is a test```"))
    dummystring = "- I just need to know how this works\n- Final logic check"
    #print(block_to_block_type(dummystring))

    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    #print(node.to_html())

    #copy_dir("/home/sam/projects/github.com/Zallu35/SSG/public/testsrc", "/home/sam/projects/github.com/Zallu35/SSG/public/testdst")

    print(extract_title("# This is a title!"))
    print(extract_title("# This is a title!\nThis should not be included..."))
    #print(extract_title("#This is imporperly formatted"))
    #print(extract_title("This is NOT a title!"))
    
    #with open("/home/sam/projects/github.com/Zallu35/SSG/content/index.md") as a:
        #writing = a.read()
    #tn1 = markdown_to_html_node(writing)
    #print(tn1)
    #generate_page("/home/sam/projects/github.com/Zallu35/SSG/content/index.md", "/home/sam/projects/github.com/Zallu35/SSG/public/testdir/index.html", "/home/sam/projects/github.com/Zallu35/SSG/template.html")

general_test()