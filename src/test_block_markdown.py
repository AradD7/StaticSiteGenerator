import unittest

from block_markdown import markdown_to_blocks

class test_block_md(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """

        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                    ],
                )

    def test_markdown_to_blocks2(self):
        md = """
            
                this is another _italic_ paragraph

        which is just insane
        split in multiple
        paragraphs with each one
        has more that enough

        -you know
        -just like
        -insane

        which is like
        dude!

        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                [
                    "this is another _italic_ paragraph",
                    "which is just insane\nsplit in multiple\nparagraphs with each one\nhas more that enough",
                    "-you know\n-just like\n-insane",
                    "which is like\ndude!"
                ],
                blocks)

    def test_markdown_to_blocks_edge1(self):
        md = " "
        blocks = markdown_to_blocks(md)
        self.assertEqual([""], blocks)

    def test_markdown_to_blocks_edge2(self):
        md = "one liner         "
        blocks = markdown_to_blocks(md)
        self.assertEqual(["one liner"], blocks)
