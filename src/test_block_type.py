import unittest

from block_markdown import BlockType, block_to_block_type

class test_block_to_block_type(unittest.TestCase):
    def test_block_to_heading(self):
        block = "#### this is a heading <h4>"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_block_to_heading2(self):
        block = "# this is a heading <h1>"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


    def test_block_to_code(self):
        block = "```\nthis is a code block yippieeee\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)


    def test_block_to_quote(self):
        block = ">this is a quote block yippieeee"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)


    def test_block_to_unordered_list(self):
        block = "- this is an\n- unordered list\n- block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)


    def test_block_to_ordered_list(self):
        block = "1. this is\n2. ordered list\n3. block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)


    def test_block_to_paragraph(self):
        block = "this is a simple paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
