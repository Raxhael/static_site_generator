from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) == 1:
            result_list.append(node)
            continue
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown")
        new_node = []
        for index,item in enumerate(split_text):
            if index%2 == 0:
                new_node.append(TextNode(item,TextType.TEXT))
            else:
                new_node.append(TextNode(item, text_type))
        result_list.extend(new_node)
    print(result_list)
    return result_list  


def split_nodes_image(old_nodes):
    for node in old_nodes:
        original_text = node.text
        print(original_text)
        image_parts = extract_markdown_images(original_text)
        print(image_parts)
        image_alt = image_parts[0]
        image_link = image_parts[1]
        sections = original_text.split(f"![{image_alt}]({image_link})")
        print(sections)


node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)

new_nodes = split_nodes_image([node])

