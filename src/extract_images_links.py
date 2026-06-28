# Test regex patterns here: https://regexr.com/
import re
from textnode import TextNode, TextType

# Define two capture groups, the first will not accept '[' or ']', the second not '(' or ')', but both will accept anything else.
IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# The same as for images, but add a negative lookbehind to prevent capturing images by forbidding the prefix '!'.
LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(IMAGE_REGEX, text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(LINK_REGEX, text)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_text_strings = re.split(LINK_REGEX, node.text)
        if len(split_text_strings) == 1:
            new_nodes.append(node)
            continue
        # Every third string must be plain, the rest is link.
        plain_text_strings = split_text_strings[0::3]
        # We could just use the extracted link descriptions [1::3] and link URLs [2::3], but we didn't write the helpers for nothing.
        links = extract_markdown_links(node.text)
        for i in range(0, len(plain_text_strings) + len(links)):
            # When the counter is even, starting with 0, there should be a plain text node, unless that string is empty.
            if i % 2 == 0:
                if plain_text_strings[i // 2] == '':
                    continue
                new_nodes.append(TextNode(plain_text_strings[i // 2], TextType.PLAIN))
            # When the counter is odd we should add a link node
            else:
                new_nodes.append(TextNode(links[(i - 1) // 2][0], TextType.LINK, links[(i - 1) // 2][1]))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_text_strings = re.split(IMAGE_REGEX, node.text)
        if len(split_text_strings) == 1:
            new_nodes.append(node)
            continue
        # Every third string must be plain, the rest is image.
        plain_text_strings = split_text_strings[0::3]
        images = extract_markdown_images(node.text)
        for i in range(0, len(plain_text_strings) + len(images)):
            # When the counter is even, starting with 0, there should be a plain text node, unless that string is empty.
            if i % 2 == 0:
                if plain_text_strings[i // 2] == '':
                    continue
                new_nodes.append(TextNode(plain_text_strings[i // 2], TextType.PLAIN))
            # When the counter is odd we should add an image node
            else:
                new_nodes.append(TextNode(images[(i - 1) // 2][0], TextType.IMAGE, images[(i - 1) // 2][1]))
    return new_nodes