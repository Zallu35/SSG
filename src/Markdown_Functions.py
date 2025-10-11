from enum import Enum


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
