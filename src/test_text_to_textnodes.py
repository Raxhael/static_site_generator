from text_to_textnodes import text_to_textnodes
from textnode import *
import unittest

class TestTextToTextnode(unittest.TestCase):
    def test_converts(self):
        test_cases = [
            (  
                    "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
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
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                False
            ),
            (
                "This is text with an italic word and a code block and an and a",
                [
                    TextNode("This is text with an italic word and a code block and an and a",TextType.TEXT)
                ],
                False
            ),
            (
                "This is text with an *italic word and a code block and an and a",
                None,
                True
            )
        ]
        for input_text,expected_result,should_raise in test_cases:
            if should_raise:
                with self.assertRaises(ValueError):
                    text_to_textnodes(input_text)
            else:
                result = text_to_textnodes(input_text)
                self.assertEqual(len(result),len(expected_result))


if __name__ == "__main__":
    unittest.main()
