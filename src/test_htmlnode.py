import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class test_htmlnode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", None, None,{"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode("<a>", None, None,{"href": "https://www.google.com","target": "_blank"})
        node3 = HTMLNode("<a>", None, None,{"href": "https://www.google.com"})
        
        self.assertEqual(node,node2)
        self.assertNotEqual(node2,node3)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None , "Hello, world!")
        node4 = LeafNode("", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "Hello, world!")
        self.assertEqual(node4.to_html(),"<>Hello, world!</>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        with_props = LeafNode("span", "child", {"class": "my-class"})
        parent_node_with_props = ParentNode("div", [with_props], {"id": "parent-div"})
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertEqual(parent_node_with_props.to_html(), '<div id="parent-div"><span class="my-class">child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()