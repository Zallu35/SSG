from htmlnode import HTMLNode, LeafNode


def main():
    LN = LeafNode("a", "Click me!", None, {"href": "https://www.google.com"})
    HN = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com"})
    print(LN)
    print(HN)

main()