import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


class test_split_nodes(unittest.TestCase):
    def test_bold_middle(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("bolded phrase", TextType.BOLD),
                                TextNode(" in the middle", TextType.TEXT),
                                ])

    def test_bold_start_end(self):
        node = TextNode("**this sentence** has a lot of **bold words**", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
                                TextNode("this sentence", TextType.BOLD),
                                TextNode(" has a lot of ", TextType.TEXT),
                                TextNode("bold words", TextType.BOLD),
                                ])
    def test_bold_start(self):
        node = TextNode("umm**the beninging**yes is bold only", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
                                TextNode("umm", TextType.TEXT),
                                TextNode("the beninging", TextType.BOLD),
                                TextNode("yes is bold only", TextType.TEXT),
                                ])
    def test_bold_end(self):
        node = TextNode("this sentence ends with **bold words**", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
                                TextNode("this sentence ends with ", TextType.TEXT),
                                TextNode("bold words", TextType.BOLD),
                                ])
    def test_italic(self):
        node = TextNode("_this sentence_ is the _ultimate_ test for _italic_ words, _the big boss_", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), [
                                TextNode("this sentence", TextType.ITALIC),
                                TextNode(" is the ", TextType.TEXT),
                                TextNode("ultimate", TextType.ITALIC),
                                TextNode(" test for ", TextType.TEXT),
                                TextNode("italic", TextType.ITALIC),
                                TextNode(" words, ", TextType.TEXT),
                                TextNode("the big boss", TextType.ITALIC),
                                ])
    def test_code(self):
        node = TextNode("`this sentence` is the `ultimate` test for `code` words, `the big boss`", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [
                                TextNode("this sentence", TextType.CODE),
                                TextNode(" is the ", TextType.TEXT),
                                TextNode("ultimate", TextType.CODE),
                                TextNode(" test for ", TextType.TEXT),
                                TextNode("code", TextType.CODE),
                                TextNode(" words, ", TextType.TEXT),
                                TextNode("the big boss", TextType.CODE),
                                ])


    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
                ], 
            new_nodes)

    def test_split_images2(self):
        node = TextNode(
                "![zeroth image](https://fakeimage.ca/meowmewo.png) This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with text after it!",
                TextType.TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("zeroth image", TextType.IMAGE, "https://fakeimage.ca/meowmewo.png"),
                TextNode(" This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" with text after it!", TextType.TEXT)
                ], 
            new_nodes)


    def test_split_link(self):
        node = TextNode(
                "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
                ], 
            new_nodes)

    def test_split_link2(self):
        node = TextNode(
                "[zeroth image](https://fakeimage.ca/meowmewo.png) This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png) with text after it!",
                TextType.TEXT,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("zeroth image", TextType.LINK, "https://fakeimage.ca/meowmewo.png"),
                TextNode(" This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" with text after it!", TextType.TEXT)
                ], 
            new_nodes)

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev")
                    ],
                nodes)

    def test_text_to_textnode_ultimate_test(self):
        text = "**this** is text `with` all **sorts of** _different_ text ![random image here](https://mewo.ca/noway.jog) `with` _different_ **all** sort [click me!](https://youhack.ca/getout) text and node _yesss!_"
        node = text_to_textnodes(text)
        self.assertListEqual(
                [
                    TextNode("this", TextType.BOLD),
                    TextNode(" is text ", TextType.TEXT),
                    TextNode("with", TextType.CODE),
                    TextNode(" all ", TextType.TEXT),
                    TextNode("sorts of", TextType.BOLD),
                    TextNode(" ", TextType.TEXT),
                    TextNode("different", TextType.ITALIC),
                    TextNode(" text ", TextType.TEXT),
                    TextNode("random image here", TextType.IMAGE, "https://mewo.ca/noway.jog"),
                    TextNode(" ", TextType.TEXT),
                    TextNode("with", TextType.CODE),
                    TextNode(" ", TextType.TEXT),
                    TextNode("different", TextType.ITALIC),
                    TextNode(" ", TextType.TEXT),
                    TextNode("all", TextType.BOLD),
                    TextNode(" sort ", TextType.TEXT),
                    TextNode("click me!", TextType.LINK, "https://youhack.ca/getout"),
                    TextNode(" text and node ", TextType.TEXT),
                    TextNode("yesss!", TextType.ITALIC)
                ],
                node)


if __name__ == "__main__":
    unittest.main()
