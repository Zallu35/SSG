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

