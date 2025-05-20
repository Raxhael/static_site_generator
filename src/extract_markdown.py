import re

def extract_markdown_images(string):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",string)

def extract_markdown_links(string):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(:with([^\(\)]*)\)", string)
