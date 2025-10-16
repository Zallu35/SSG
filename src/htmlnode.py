class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not yet implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_list=""
        for k in self.props:
            props_list += f' {k}="{self.props[k]}"'
        return props_list

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Nodes MUST have a value!")
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Nodes MUST have a tag")
        if not self.children:
            raise ValueError("Parent Node missing children")
        m=""
        for child in self.children:
            m+= child.to_html()
        return f"<{self.tag}>{m}</{self.tag}>"