import unittest
from textnode import TextNode, TextType
from split_nodes import*

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


class TestSplitNodesImage(unittest.TestCase):

    def test_split_images(self):
        test_cases = [
            (
                [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)],
                [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            
                ],
            ),
            (
                [TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another",TextType.TEXT)],
                [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
                ]
            ),
            (
                [TextNode("![image](https://i.imgur.com/zjjcJKZ.png)",TextType.TEXT)],
                [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                ]
            ),           
                
            
            (
                [TextNode("this is just some text to confirm that nothing has changed here",TextType.TEXT)],
                [TextNode("this is just some text to confirm that nothing has changed here",TextType.TEXT)]
            )    
            ]

        for input_nodes, expected, in test_cases:
                result = split_nodes_image(input_nodes)
                self.assertEqual(len(result), len(expected))
                for i in range(len(result)):
                    self.assertEqual(result[i].text, expected[i].text)
                    self.assertEqual(result[i].text_type, expected[i].text_type)
                    if result[i].text_type == TextType.IMAGE:
                        self.assertEqual(result[i].url, expected[i].url)




class TestSplitNodesLink(unittest.TestCase):

    def test_split_link(self):
        test_cases = [
            (
                [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)],
                [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
            ),
             (
                [TextNode("[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)],
                [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
            ),
            (
                [TextNode("[to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)],
                [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                ]
            ),
            (
                [TextNode("this is just some text to confirm that nothing has changed here",TextType.TEXT)],
                [TextNode("this is just some text to confirm that nothing has changed here",TextType.TEXT)],
            ),
                       
        ]



        for input_nodes, expected, in test_cases:
                result = split_nodes_link(input_nodes)
                self.assertEqual(len(result), len(expected))
                for i in range(len(result)):
                    self.assertEqual(result[i].text, expected[i].text)
                    self.assertEqual(result[i].text_type, expected[i].text_type)
                    if result[i].text_type == TextType.LINK:
                        self.assertEqual(result[i].url, expected[i].url)


if __name__ == "__main__":
    unittest.main()
