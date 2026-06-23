import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This **is** a node", TextType.PLAIN)
        results = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(results, [
            TextNode("This ", TextType.PLAIN),
            TextNode("is", TextType.BOLD),
            TextNode(" a node", TextType.PLAIN)
        ])
    def test_italic(self):
        node = TextNode("This _is_ a node", TextType.PLAIN)
        results = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(results, [
            TextNode("This ", TextType.PLAIN),
            TextNode("is", TextType.ITALIC),
            TextNode(" a node", TextType.PLAIN)
        ])
    def test_code(self):
        node = TextNode("This `is` a node", TextType.PLAIN)
        results = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(results, [
            TextNode("This ", TextType.PLAIN),
            TextNode("is", TextType.CODE),
            TextNode(" a node", TextType.PLAIN)
        ])
    def test_not_plain(self):
        node = TextNode("This **is** a node", TextType.BOLD)
        results = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(results, [TextNode("This **is** a node", TextType.BOLD)])
    def test_multi_node(self):
        nodes = [
            TextNode("This **is** a node", TextType.PLAIN),
            TextNode("This is **also** a node", TextType.PLAIN)
        ]
        results = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(results, [
            TextNode("This ", TextType.PLAIN),
            TextNode("is", TextType.BOLD),
            TextNode(" a node", TextType.PLAIN),
            TextNode("This is ", TextType.PLAIN),
            TextNode("also", TextType.BOLD),
            TextNode(" a node", TextType.PLAIN)
        ])
    def test_unclosed_delimiter(self):
        node = TextNode("Delimiter **unclosed", TextType.PLAIN)
        with self.assertRaises(Exception):
            results = split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()