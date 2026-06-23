from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_strings = node.text.split(delimiter)
        if len(split_strings) % 2 == 0:
            raise Exception(f"A closing delimiter [{delimiter}] was not found in node [{node.text}]")
        for i in range(0, len(split_strings)):
            # Ignore empty strings that may result from a delimiter doubled or at the beginning or end of the string
            if split_strings[i] == '':
                continue
            # All even strings are outside the delimiter and should be returned as plain text
            if i % 2 == 0:
                new_nodes.append(TextNode(split_strings[i], TextType.PLAIN))
            # All odd strings are inside the delimiter and should be added as the text type defined by the delimiter
            else:
                new_nodes.append(TextNode(split_strings[i], text_type))
    return new_nodes

# IMPROVE: the function should also support spreading the delimiters over multiple nodes. Now each node is supposed to have an even number of delimiters.