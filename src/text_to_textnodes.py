from split_nodes import *



def text_to_textnodes(text):
    running_list = [TextNode(text,TextType.TEXT,None)]
    delimiters = {"**":TextType.BOLD,"*":TextType.ITALIC,"_":TextType.ITALIC,"`":TextType.CODE}
    running_list = split_nodes_image(running_list)
    running_list = split_nodes_link(running_list)
    for key, value in delimiters.items():
        running_list = (split_nodes_delimiter(running_list,key,value))
    print(running_list)
    return running_list







text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](httcs://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
out = text_to_textnodes(text)

