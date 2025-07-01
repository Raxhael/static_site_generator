import unittest

from textnode import TextType, TextNode

def markdown_to_blocks(markdown):
    output = []
    running = markdown.split("\n\n")
    for i in running:
        step = i.strip()
        if step != "":
            output.append(step)
    return output



md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
markdown_to_blocks(md)
