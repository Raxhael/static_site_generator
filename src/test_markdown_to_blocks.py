import unittest
from markdown_to_blocks import markdown_to_blocks


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test_cases = (
"""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""",
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            False
        ),
        (
                """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
                """,
            [
                                "This is **bolded** paragraph",
                                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                                "- This is a list\n- with items",
            ],
            False
        ),
        (
                """
This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
""",
            [
                """
This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""

            ],
            False
        ),
        (
            """


           
""",
            [
                            """


           
""" 

            ],
            False
        )
        
        for input,expected_result,should_raise in test_cases:
            if should_raise:
                with self.assertRaises(ValueError):
                    markdown_to_blocks(input)
            else:
                result = markdown_to_blocks(input)
                self.assertEqual(len(result),len(expected_result))


if __name__ == "__main__":
    unittest.main()        