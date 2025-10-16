from enum import Enum
from textnode import *
from htmlnode import *
from Node_Augmentations import text_to_textnodes


def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    out_list = []
    for block in block_list:
        if block.strip() == "":
            continue
        out_list.append(block.strip())
    return out_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE =  "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    if text[0] == "#":
        return BlockType.HEADING
    if (text[0:3] == "```") and (text[-3:] == "```"):
        return BlockType.CODE
    if text[0] == ">":
        scantext = text.split("\n")
        for line in scantext:
            if line[0] != ">":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if text[0:2] == "- ":
        scantext = text.split("\n")
        for line in scantext:
            if line[0:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if text[1:3] == ". ":
        scantext = text.split("\n")
        checkorder = []
        for line in scantext:
            if not line[0].isdigit() or (line[1:3] != ". "):
                return BlockType.PARAGRAPH
            checkorder.append(line[0])
        for i in range(len(checkorder)):
            if checkorder[i] != str(i+1):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    mkd_blocks = markdown_to_blocks(markdown)
    child_list = []
    for block in mkd_blocks:
        btype = block_to_block_type(block)
        if btype == BlockType.PARAGRAPH:
            child_list.extend(paragraph_ParentNode(block))
        if btype == BlockType.HEADING:
            child_list.append(heading_ParentNode(block))
        if btype == BlockType.CODE:
            child_list.append(code_ParentNode(block))
        if btype == BlockType.QUOTE:
            child_list.extend(quote_ParentNode(block))
        if btype == BlockType.UNORDERED_LIST:
            child_list.append(unorderedlist_ParentNode(block))
        if btype == BlockType.ORDERED_LIST:
            child_list.append(orderedlist_ParentNode(block))
    return ParentNode("div", child_list)
    
def heading_ParentNode(text):
    counter = 6
    num = 0
    while counter != 0:
        num = text.count("#", 0, counter)
        if num == text.count("#", 0, num):
            counter = 0
        else:
            counter = num
    chtextnodes = text_to_textnodes(text.lstrip("# "))
    chhtmlnodes = []
    for node in chtextnodes:
        chhtmlnodes.append(text_node_to_html_node(node))
    return ParentNode(f"h{num}", chhtmlnodes)

def quote_ParentNode(text):
    newtext = text.split("\n")
    textlist = []
    for line in newtext:
        textlist.append(line.lstrip(">").strip())
    endtext = " ".join(textlist)
    chtextnodes = text_to_textnodes(endtext)
    chhtmlnodes = []
    for node in chtextnodes:
        chhtmlnodes.append(text_node_to_html_node(node))
    return [ParentNode("blockquote", chhtmlnodes)]

def paragraph_ParentNode(text):
    newtext = text.replace("\n", " ")
    #PNlist = []
    #for line in newtext:
    chtextnodes = text_to_textnodes(newtext)
    chhtmlnodes = []
    for node in chtextnodes:
        chhtmlnodes.append(text_node_to_html_node(node))
        #PNlist.append(ParentNode("p", chhtmlnodes))
    return [ParentNode("p", chhtmlnodes)]

def code_ParentNode(text):
    stext = text.strip("`").lstrip("\n")
    LNode = text_node_to_html_node(TextNode(stext, TextType.CODE))
    return ParentNode("pre", [LNode])

def unorderedlist_ParentNode(text):
    nodelist = []
    tl = text.split("\n")
    for line in tl:
        new_text = line.lstrip("- ")
        chtextnodes = text_to_textnodes(new_text)
        chhtmlnodes = []
        for node in chtextnodes:
            chhtmlnodes.append(text_node_to_html_node(node))
        nodelist.append(ParentNode("li", chhtmlnodes))
    return ParentNode("ul", nodelist)

def orderedlist_ParentNode(text):
    nodelist = []
    tl = text.split("\n")
    for line in tl:
        new_text = line[3:]
        chtextnodes = text_to_textnodes(new_text)
        chhtmlnodes = []
        for node in chtextnodes:
            chhtmlnodes.append(text_node_to_html_node(node))
        nodelist.append(ParentNode("li", chhtmlnodes))
    return ParentNode("ol", nodelist)

def extract_title(markdown):
    parts = markdown.split("\n")
    if not parts[0].startswith("# "):
        raise Exception("No Title Found!")
    return parts[0].lstrip("# ")