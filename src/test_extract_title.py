import unittest

from block_markdown import extract_title

class test_extract_title(unittest.TestCase):
    def test_title(self):
        md = "# yippie"
        title = extract_title(md)
        self.assertEqual(title, "yippie")

    def test_title2(self):
        md = """
        # Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien

        ## Blog posts

        - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
        - [Why Tom Bombadil Was a Mistake](/blog/tom)
        - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)
        """
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")
