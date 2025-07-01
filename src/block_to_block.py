import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if is_match(block,r"^#{1,6} .*"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if is_match(block, r"^> "):
        return BlockType.QUOTE
    if is_match(block, r"^- "):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block) == True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_match(block,pattern):
    lines = block.split("\n")
    for line in lines:
        if not re.match(pattern,line):
            return False
    return True


def is_ordered_list(block):
    lines = block.split("\n")
    counter = 1
    for line in lines:
        expected_pattern = rf"^{counter}\. "
        if not re.match(expected_pattern,line):
            return False
        counter += 1
    return True





