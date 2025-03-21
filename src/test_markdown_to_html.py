import unittest

from markdown_to_html import markdown_to_html_node

class test_markdown_to_html_nodes(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                )

    def test_list(self):
        md = """
        - This is a list
        - that has some **random**
        - elements but

        1. this _one_ is 
        2. an _ordered_ **list** you
        3. like it?
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ul><li>This is a list</li><li>that has some <b>random</b></li><li>elements but</li></ul>" + 
                "<ol><li>this <i>one</i> is</li><li>an <i>ordered</i> <b>list</b> you</li><li>like it?</li></ol></div>",
                )

    def test_all_types(self):
        md = """
        # following is unordered list:

        - This is a list
        - that has some **random**
        - elements but

        ## following ordered:

        1. this _one_ is 
        2. an _ordered_ **list** you
        3. like it?

        This is **the** ultimate _test_

        ```
        for this will be your **last** _trick_ you 
        devil **shoulder**
        boom
        ```

        >and **finally** a quote!
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><h1>following is unordered list:</h1><ul><li>This is a list</li><li>that has some <b>random</b></li><li>elements but</li></ul>" + 
                "<h2>following ordered:</h2><ol><li>this <i>one</i> is</li><li>an <i>ordered</i> <b>list</b> you</li><li>like it?</li></ol>" + 
                "<p>This is <b>the</b> ultimate <i>test</i></p>" + 
                "<pre><code>for this will be your **last** _trick_ you\ndevil **shoulder**\nboom\n</code></pre>" + 
                "<blockquote>and <b>finally</b> a quote!</blockquote></div>"
                )
    def test_lists(self):
        md = """
            - This is a list
            - with items
            - and _more_ items

            1. This is an `ordered` list
            2. with items
            3. and more items

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
            # this is an h1

            this is paragraph text

            ## this is an h2
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
        > This is a
        > blockquote block

        this is paragraph text

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
