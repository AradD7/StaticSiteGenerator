import unittest

from htmlnode import LeafNode, ParentNode


class TestLeafnode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_children2(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_to_html_with_grandchildren2(self):
        grandchild_node1 = LeafNode("b", "grandchild bold")
        grandchild_node2 = LeafNode("h1", "grandchild header1")
        grandchild_node3 = LeafNode("i", "grandchild italic")
        child_node1 = ParentNode("span", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("div", [grandchild_node3])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), 
                         "<div><span><b>grandchild bold</b><h1>grandchild header1</h1></span><div><i>grandchild italic</i></div></div>")


if __name__ == "__main__":
    unittest.main()
