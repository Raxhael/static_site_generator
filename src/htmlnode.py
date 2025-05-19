from textnode import TextNode, TextType


class HTMLNode():
    def __init__(self,tag=None, value=None, children=None,props=None):
        self.tag = tag
        self.value = value
        if children == None:
            self.children = []
        else:
            self.children = children        
        if props == None:
            self.props = {}
        else:
            self.props = props        
        


    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == {}:
            return ""
        leading = ""
        for item in self.props:
            leading += f' {item}="{self.props[item]}"'
        return leading
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"

    def __eq__(self,other):
        if not isinstance(other, HTMLNode):
            return False
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False
    
class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(tag,value,None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError("No Children passed")
        if self.tag == None:
            raise ValueError("No Tag passed")
        html = f"<{self.tag}"
        if self.props:
            for prop,value in self.props.items():
                html += f' {prop}="{value}"'
        html += ">"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"

        return html        

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url != None:
                return LeafNode("a", text_node.text,{"href":text_node.url})
            raise ValueError("No URL given")
        case TextType.IMAGE:
            if text_node.url == None:
                raise ValueError("No URL provided")
            if text_node.text == None:
                raise ValueError("No Text provided")
            return LeafNode("img", "", {"src":text_node.url, "alt": text_node.text if text_node.text is not None else ""})
    raise ValueError("Incorrect Type")



sample_node = TextNode("hello world", TextType.IMAGE, "www.google.com.")
result = text_node_to_html_node(sample_node)
print(result.tag, result.value, result.props)