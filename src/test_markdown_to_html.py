import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_multi(self):
        md = """
This is **bolded**.
This is a [link](https://boot.dev)
This is an ![image](https://boot.dev/logo.svg)

```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is <b>bolded</b>.<br>This is a <a href="https://boot.dev">link</a><br>This is an <img src="https://boot.dev/logo.svg" alt="image"></p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>',
        )

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
            "<div><p>This is <b>bolded</b> paragraph<br>text in a p<br>tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
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

    def test_heading1(self):
        md = "# This is a **heading** with _markup_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>heading</b> with <i>markup</i></h1></div>",
        )

    def test_heading3(self):
        md = "### This is a **heading** with _markup_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a <b>heading</b> with <i>markup</i></h3></div>",
        )

    def test_quotes(self):
        md = """
>This is **bolded** paragraph
>text in a blockquote
>tag here

> This is another quote with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph<br>text in a blockquote<br>tag here</blockquote><blockquote>This is another quote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item #1
- **Item #2**
- _Item_ #3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item #1</li><li><b>Item #2</b></li><li><i>Item</i> #3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Item #1
2. **Item #2**
3. _Item_ #3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item #1</li><li><b>Item #2</b></li><li><i>Item</i> #3</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()