class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("has not yet been defined")

    def props_to_html(self):
        if not(self.props):
            return ""

        props_in_html = ""
        for key in self.props:
            props_in_html += f' {key}="{self.props[key]}"'

        return props_in_html

    def __repr__(self):
        return f"HTMLnode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"


class LeafNode(HTMLnode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node cannot have None as value")
        if not(self.tag):
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} />"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLnode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not(self.tag):
            raise ValueError("Parent Node must have tag argument")
        if not(self.children):
            raise ValueError("Parent Node must have children argument")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
             html_string += node.to_html()
        html_string += f"</{self.tag}>"
        return html_string
            










