import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("a", "This is text", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

    def test_repr(self):
        node = HTMLNode("a", "This is text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, This is text, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_repr_child(self):
        child = HTMLNode()
        node = HTMLNode("a", "This is text", [child], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, This is text, [HTMLNode(None, None, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src": "img_girl.jpg", "alt": "Girl in a jacket", "width": "500", "height": "600"})
        self.assertEqual(node.to_html(), '<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">')

    def test_empty_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_tag(self):
        node = LeafNode(None, "Hello!")
        self.assertEqual(node.to_html(), "Hello!")

    def test_empty_string_tag(self):
        node = LeafNode("", "Hello!")
        self.assertEqual(node.to_html(), "Hello!")

    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_child_with_props(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://www.google.com">Click me!</a></div>')

    def test_to_html_with_props_and_child_with_props(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<a href="https://www.google.com"><a href="https://www.google.com">Click me!</a></a>')

    def test_parent_to_html_multichild(self):
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

    def test_empty_tag(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("p", [])
        with self.assertRaisesRegex(ValueError, "^(?!Tag is empty).*$"):
            node.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()