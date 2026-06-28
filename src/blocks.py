# Test regex patterns here: https://regexr.com/
import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if len(re.findall(r"^#{1,6}\ .+", block)) > 0 and len(block.split("\n")) == 1:
        return BlockType.HEADING
    if len(re.findall(r"^`{3}|`{3}$", block)) == 2:
        return BlockType.CODE
    split = block.split("\n")
    quote = False
    for s in split:
        if s.startswith(">"):
            quote = True
        else:
            quote = False
            break
    if quote:
        return BlockType.QUOTE
    unordered_list = False
    for s in split:
        if s.startswith("- "):
            unordered_list = True
        else:
            unordered_list = False
            break
    if unordered_list:
        return BlockType.UNORDERED_LIST
    ordered_list = False
    previous_digit = None
    for s in split:
        matches = re.findall(r"^(\d+)\.\ ", s)
        if len(matches) == 0:
            ordered_list = False
            break
        current_digit = int(matches[0])
        if previous_digit:
            if current_digit != previous_digit + 1:
                ordered_list = False
                break
        ordered_list = True
        previous_digit = current_digit
    if ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    split = markdown.split("\n\n")
    for s in split:
        if len(s) > 0 and s != "\n":
            blocks.append(s.strip())
    return blocks