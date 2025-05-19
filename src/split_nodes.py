from textnode import TextType, TextNode


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
