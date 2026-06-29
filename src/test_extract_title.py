import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md = "# This is my title"
        title = extract_title(md)
        self.assertEqual(title, "This is my title")

    def test_multi(self):
        md = """# This is my title

```
This is my code
```
"""
        title = extract_title(md)
        self.assertEqual(title, "This is my title")

    def test_empty(self):
        md = ""
        with self.assertRaises(Exception):
            title = extract_title(md)
            
    def test_invalid(self):
        md = "## This is my title"
        with self.assertRaises(Exception):
            title = extract_title(md)

if __name__== "__main__":
    unittest.main()