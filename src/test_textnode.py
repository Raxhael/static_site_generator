import unittest
from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC,"https://www.booties.com")
        node5 = TextNode("This is a text node", TextType.BOLD,"https://www.booties.com")
        node6 = TextNode("This is a text node", TextType.ITALIC,"https://www.booties.com")
        node7 = TextNode("icecream", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node5)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5,node6)
        self.assertNotEqual(node,node7)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode(None,TextType.TEXT)
        node3 = TextNode("Boots is grand",TextType.IMAGE,"https://www.booties.com")
        html_node = text_node_to_html_node(node)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.value, None)
        self.assertEqual(html_node3.props, {'src': 'https://www.booties.com', 'alt': 'Boots is grand'})

        




if __name__ == "__main__":
    unittest.main()