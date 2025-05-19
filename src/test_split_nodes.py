import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_multiple_delimiters(self):
        test_cases = [
            # (input_node, delimiter, text_type, expected_result)
            (
                [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)],
                "**", 
                TextType.BOLD,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bolded phrase", TextType.BOLD),
                    TextNode(" in the middle", TextType.TEXT)
                ],
                False
            ),
            (
                [TextNode("This is text with a *italic phrase* in the middle", TextType.TEXT)],
                "*",
                TextType.ITALIC,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("italic phrase", TextType.ITALIC),
                    TextNode(" in the middle", TextType.TEXT)
                ],
                False
                
            ),
            (
                [TextNode("This is text with a _italic phrase_ in the middle", TextType.TEXT)],
                "_",
                TextType.ITALIC,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("italic phrase", TextType.ITALIC),
                    TextNode(" in the middle", TextType.TEXT)
                ],
                False

            ),
            (
                [TextNode("This is text with a `code chunk` in the middle", TextType.TEXT)],
                "`",
                TextType.CODE,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code chunk", TextType.CODE),
                    TextNode(" in the middle", TextType.TEXT)
                ],
                False

            ),
            (
                [TextNode("This is text with a **bolded **phrase** in the middle", TextType.TEXT)],
                "**",
                TextType.BOLD,
                None,
                True

            ),
            (
                [TextNode("This is _text_ with a **bolded phrase** in the middle", TextType.TEXT)],
                "**",
                TextType.BOLD,
                [
                    TextNode("This is _text_ with a ", TextType.TEXT),
                    TextNode("bolded phrase", TextType.BOLD),
                    TextNode(" in the middle", TextType.TEXT)
                ],
                False

            ),
            (
                [TextNode("This is text with a bolded phrase in the middle", TextType.TEXT)],
                "*",
                TextType.ITALIC,
                [TextNode("This is text with a bolded phrase in the middle", TextType.TEXT)],
                False


            ),
            (
                [TextNode("This is text with a **bolded phrase in the middle", TextType.ITALIC)],
                "*",
                TextType.ITALIC,
                [TextNode("This is text with a **bolded phrase in the middle", TextType.ITALIC)],
                False

            ),
            (
                [TextNode("This is text with a **bolded phrase in the middle", TextType.CODE)],
                "*",
                TextType.ITALIC,
                [TextNode("This is text with a **bolded phrase in the middle", TextType.CODE)],
                False
            )
        ]
        
        for input_nodes, delimiter, text_type, expected, should_raise in test_cases:
            if should_raise:
                with self.assertRaises(ValueError):
                    split_nodes_delimiter(input_nodes,delimiter,text_type)
            else: 
                result = split_nodes_delimiter(input_nodes, delimiter, text_type)
                self.assertEqual(len(result), len(expected))
                for i in range(len(result)):
                    self.assertEqual(result[i].text, expected[i].text)
                    self.assertEqual(result[i].text_type, expected[i].text_type)

if __name__ == "__main__":
    unittest.main()