from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph block"
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED_LIST = "unordered_list block"
    ORDERED_LIST = "ordered_list block"


def block_to_block_type(markdown_block):
    markdown_list = markdown_block.split(" ")
    if markdown_list[0] == len(markdown_list[0])*'#':
        return BlockType.HEADING
    if len(markdown_list[0]) >= 3 and markdown_list[0][:3] == '```' and len(markdown_list[-1]) >= 3 and markdown_list[-1][-3:]:
        return BlockType.CODE
    if markdown_list[0][0] == '>':
        return BlockType.QUOTE
    if markdown_list[0] == '-':
        return BlockType.UNORDERED_LIST
    if markdown_list[0] == '1.':
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH



def markdown_to_blocks(markdown):
    markdown_list = markdown.strip().split('\n\n')
    markdown_list_clean = list(map(lambda string: '\n'.join(list(map(lambda string_in_list: string_in_list.strip(), string.split('\n')))), markdown_list))
    return markdown_list_clean

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block[0:2] == '# ':
            return block.strip('# ')

    raise Exception("file has no title (no h1)")


