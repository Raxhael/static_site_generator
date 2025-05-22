import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links



class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        with self.assertRaises(Exception):
            extract_markdown_images("(https://i.imgur.com/zjjcJKZ.png)")
        with self.assertRaises(Exception):
            extract_markdown_images("This is text with an ![[image]((https://i.imgur.com/zjjcJKZ.png)")




def test_extract_markdown_Links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], matches)
        with self.assertRaises(Exception):
            extract_markdown_links("This is text with a link to boot dev]dev) and [to youtube](https://www.youtube.com/@bootdotdev)") 
        with self.assertRaises(Exception):
            extract_markdown_links("This is text with a link [to boot dev]dev) and [to youtube](https://www.youtube.com/@bootdotdev)")








if __name__== "__main__":
    unittest.main()
