from split_nodes import *



def text_to_textnodes(text):
    running_list = [TextNode(text,TextType.TEXT,None)]
    delimiters = {"**":TextType.BOLD,"*":TextType.ITALIC,"_":TextType.ITALIC,"`":TextType.CODE}
    running_list = split_nodes_image(running_list)
    running_list = split_nodes_link(running_list)
    for key, value in delimiters.items():
        running_list = (split_nodes_delimiter(running_list,key,value))
    return running_list






