import unittest
from text_to_text_nodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToToTextNodes(unittest.TestCase):
    def test_string_with_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
    def test_empty(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [])
    def test_plain(self):
        text = "Hoi!"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("Hoi!", TextType.PLAIN)])