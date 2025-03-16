from enum import Enum
from htmlnode import LeafNode
from extract import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    TEXT = "plain text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
     
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception("Text type not supported")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            final_nodes.append(nodes)
            continue
        split_node = []
        special_string = ""
        text_string = ""
        old_string = nodes.text
        i = 0
        while i < len(old_string):
            if old_string[i : i+len(delimiter)] == delimiter:
                if text_string:
                    split_node.append(TextNode(text_string, TextType.TEXT))
                    text_string = ""
                i += len(delimiter)
                while old_string[i : i+len(delimiter)] != delimiter:
                    special_string += old_string[i]
                    i += 1
                split_node.append(TextNode(special_string, text_type))
                special_string = ""
                i += len(delimiter)
            else:
                text_string += old_string[i]
                i += 1
        if text_string:
            split_node.append(TextNode(text_string, TextType.TEXT))
        if special_string:
            raise Exception("md string invalid")
        final_nodes.extend(split_node)
    return final_nodes


def split_nodes_image(old_nodes):
    final_nodes = []
    temp_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            final_nodes.append(nodes)
            continue
        temp_nodes.clear()
        string = nodes.text
        delim_list = extract_markdown_images(string)
        for i in range(len(delim_list)):
            delim = f"![{delim_list[i][0]}]({delim_list[i][1]})"
            splitted_string = string.split(delim)
            if splitted_string[0]:
                temp_nodes.append(TextNode(splitted_string[0], TextType.TEXT))
                temp_nodes.append(TextNode(delim_list[i][0], TextType.IMAGE, delim_list[i][1]))
            else:
                temp_nodes.append(TextNode(delim_list[i][0], TextType.IMAGE, delim_list[i][1]))
            string = splitted_string[1]
        if string:
            temp_nodes.append(TextNode(string, TextType.TEXT))
        final_nodes.extend(temp_nodes)
    return final_nodes


def split_nodes_link(old_nodes):
    final_nodes = []
    temp_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            final_nodes.append(nodes)
            continue
        temp_nodes.clear()
        string = nodes.text
        delim_list = extract_markdown_links(string)
        for i in range(len(delim_list)):
            delim = f"[{delim_list[i][0]}]({delim_list[i][1]})"
            splitted_string = string.split(delim)
            if splitted_string[0]:
                temp_nodes.append(TextNode(splitted_string[0], TextType.TEXT))
                temp_nodes.append(TextNode(delim_list[i][0], TextType.LINK, delim_list[i][1]))
            else:
                temp_nodes.append(TextNode(delim_list[i][0], TextType.LINK, delim_list[i][1]))
            string = splitted_string[1]
        if string:
            temp_nodes.append(TextNode(string, TextType.TEXT))
        final_nodes.extend(temp_nodes)
    return final_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold_node = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic_node = split_nodes_delimiter(bold_node, "_", TextType.ITALIC)
    code_node = split_nodes_delimiter(italic_node, "`", TextType.CODE)
    image_node = split_nodes_image(code_node)
    link_node = split_nodes_link(image_node)
    return link_node
















