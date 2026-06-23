import unittest
from extract_images_links import extract_markdown_images, extract_markdown_links

class TestExtractImagesOrLinks(unittest.TestCase):
    def test_images(self):
        text = "This is [text] with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) (included)."
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
    def test_links(self):
        text = "This is [text] with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) (included)."
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
    def test_image_combined(self):
        text = "This is [text] with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) (included)."
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
    def test_link_combined(self):
        text = "This is [text] with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) (included)."
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
        ])

if __name__ == "__main__":
    unittest.main()