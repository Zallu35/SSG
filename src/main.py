from textnode import TextNode, TextType


def main():
    tnode = TextNode("testing time", TextType.BOLD, "google.com")
    print(tnode)

main()