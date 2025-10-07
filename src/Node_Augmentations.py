import re
from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_node_list.append(node)
            continue
        if node.text.count(delimiter) %2 != 0:
            raise Exception("Invalid syntax, mismatched delimiters!")
        new_values = node.text.split(delimiter)
        counter=1
        for value in new_values:
            tt=TextType.PLAIN
            if counter %2 == 0:
                tt = text_type
            new_node_list.append(TextNode(value, tt))
            counter +=1
    return new_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_node_list.append(node)
            continue
        if extract_markdown_images(node.text) is None:
            new_node_list.append(node)
            continue
        image_list = extract_markdown_images(node.text)
        text_value = ["filler text", node.text]
        for image in image_list:
            text_value = text_value[1].split(f"![{image[0]}]({image[1]})", 1)
            if text_value[0] != "":
                new_node_list.append(TextNode(text_value[0], TextType.PLAIN))
            new_node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
        last_value = node.text.split(f"![{image_list[-1][0]}]({image_list[-1][1]})", 1)
        if last_value[-1] != "":
            new_node_list.append(TextNode(text_value[-1], TextType.PLAIN))
    return new_node_list
        

def split_nodes_link(old_nodes):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_node_list.append(node)
            continue
        if extract_markdown_links(node.text) is None:
            new_node_list.append(node)
            continue
        link_list = extract_markdown_links(node.text)
        text_value = ["filler text", node.text]
        for link in link_list:
            text_value = text_value[1].split(f"[{link[0]}]({link[1]})", 1)
            if text_value[0] != "":
                new_node_list.append(TextNode(text_value[0], TextType.PLAIN))
            new_node_list.append(TextNode(link[0], TextType.LINK, link[1]))
        last_value = node.text.split(f"[{link_list[-1][0]}]({link_list[-1][1]})", 1)
        if last_value[-1] != "":
            new_node_list.append(TextNode(text_value[-1], TextType.PLAIN))
    return new_node_list
