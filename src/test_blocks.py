import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
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

        def test_markdown_to_blocks_extra_newlines(self):
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

        def test_markdown_to_blocks_trailing_newline(self):
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

        def test_markdown_to_blocks_whitespace(self):
            md = """
    This is **bolded** paragraph   

    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line    

   - This is a list
- with items
- and whitespace    
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items\n- and whitespace",
                ],
            )

class TestBlockToBlockType(unittest.TestCase):
     def test_paragraph(self):
        block = "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
     def test_heading(self):
        block = "### Heading three"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
     def test_heading_with_linefeed(self):
        block = "### Heading three\nsome other test"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
     def test_code(self):
        block = "```\n# This is a code block\nwith:\n    some(code)\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
     def test_quote(self):
        block = "> This is a quote block\n> With a nice quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
     def test_quote_no_space(self):
        block = ">This is a quote block\n>With a nice quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
     def test_unordered_list(self):
        block = "- This is a list block\n- With no order"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
     def test_ordered_list(self):
        block = "1. This is a list block\n2. With an order\n3. ..."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
     def test_ordered_list_not_starting_at_one(self):
        block = "328. This is a list block\n329. With an order\n330. ..."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
     def test_ordered_list_out_of_order(self):
        block = "2. This is a list block\n1. With a wrong order\n3. ..."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()