from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node, text_to_textnodes

def remove_newlines(string):
    return ' '.join(string.split('\n'))

def text_to_children(markdown_block):
    text_nodes = text_to_textnodes(remove_newlines(markdown_block))
    return list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))

def markdown_heading_to_html_heading(heading_block):
   return f"h{len(heading_block.split(' ')[0])}" 

def markdown_list_to_html_list(list_block, ordered):
    if ordered:

        return ParentNode("ol", 
                          list(map(lambda leafnode: ParentNode("li", leafnode), 
                                   list(map(lambda text: text_to_children(text), 
                                            list(map(lambda word: word.strip('0123456789. '), 
                                                     list_block.split('\n'))))))))
    return ParentNode("ul", 
                      list(map(lambda leafnode: ParentNode("li", leafnode), 
                                list(map(lambda text: text_to_children(text), 
                                         list(map(lambda word: word.strip('- '), 
                                                  list_block.split('\n'))))))))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_of_div = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                children_of_div.append(ParentNode("p", text_to_children(block)))

            case BlockType.HEADING:
                children_of_div.append(ParentNode(markdown_heading_to_html_heading(block), text_to_children(block.lstrip('# '))))

            case BlockType.QUOTE:
                children_of_div.append(ParentNode("blockquote", text_to_children(" ".join(list(map(lambda line: line.lstrip('> '), block.split('\n')))))))

            case BlockType.UNORDERED_LIST:
                children_of_div.append(markdown_list_to_html_list(block, False))

            case BlockType.ORDERED_LIST:
                children_of_div.append(markdown_list_to_html_list(block, True))

            case BlockType.CODE:
                children_of_div.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, block.strip('```').lstrip())])]))

    html_node = ParentNode("div", children_of_div)
    return html_node











