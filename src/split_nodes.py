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
    working_list= old_nodes.copy()
    final_results = []
    while working_list:
        current_node = working_list.pop(0)
        if extract_markdown_images(current_node.text) != []:
            image = extract_markdown_images(current_node.text)
            image_alt = image[0][0]
            image_link = image[0][1]
            sections = current_node.text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                final_results.append(TextNode(sections[0],TextType.TEXT))
            final_results.append(TextNode(image_alt,TextType.IMAGE,image_link))
            if sections[1] != "":
                working_list.insert(0,TextNode(sections[1],TextType.TEXT))
        else:
            final_results.append(current_node)
    return final_results



def split_nodes_link(old_nodes):
    working_list= old_nodes.copy()
    final_results = []
    while working_list:
        current_node = working_list.pop(0)
        if extract_markdown_links(current_node.text) != []:
            links = extract_markdown_links(current_node.text)
            link_alt = links[0][0]
            link_link = links[0][1]
            sections = current_node.text.split(f"[{link_alt}]({link_link})", 1)
            if sections[0] != "":
                final_results.append(TextNode(sections[0],TextType.TEXT))
            final_results.append(TextNode(link_alt,TextType.LINK,link_link))
            if sections[1] != "":
                working_list.insert(0,TextNode(sections[1],TextType.TEXT))
        else:
            final_results.append(current_node)
    return final_results


