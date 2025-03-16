import unittest

from htmlnode import HTMLnode

class TestHTMLnode(unittest.TestCase):
    def test_rep(self):
        node = HTMLnode("a", 
                        props = {"href": "https://www.google.com", "target": "_blank"}
                        )
        output = "HTMLnode(tag = a, value = None, children = None, props = {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(f"{node}", output)

    def test_props_to_html(self):
        node = HTMLnode("a", props = {"href": "https://www.google.com", "target": "_blank"})
        output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), output)

    def test_props_to_html_edge(self):
        node = HTMLnode("h1", "howdy hoe")
        output = ""
        self.assertEqual(node.props_to_html(), output)
       

if __name__ == "__main__":
    unittest.main()
