import re

def extract_markdown_images(string):
    found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",string)
    return found

def extract_markdown_links(string):
    found = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', string)
    return found 
