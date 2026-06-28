from htmlnode import HTMLNode, ParentNode, LeafNode
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_to_text_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode
import re

def text_nodes_to_children(text_nodes: list[TextNode]) -> list[HTMLNode]:
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def markdown_to_html_node(markdown: str) -> HTMLNode:
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks: 
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block = block.replace("\n","<br>")
                p_nodes = text_to_textnodes(block)
                children.append(ParentNode("p", text_nodes_to_children(p_nodes)))
            case BlockType.CODE:
                block = block.replace("```\n","").replace("\n```","\n")
                children.append(ParentNode("pre", [LeafNode("code", block)]))
            case BlockType.HEADING:
                num_hashtags = len(re.findall(r"#{1,6}", block)[0])
                block = block.strip("# ")
                h_nodes = text_to_textnodes(block)
                children.append(ParentNode(f"h{num_hashtags}", text_nodes_to_children(h_nodes)))
            case BlockType.QUOTE:
                block = re.sub(r">\ {0,1}", "", block)
                block = block.replace("\n","<br>")
                q_nodes = text_to_textnodes(block)
                children.append(ParentNode("blockquote", text_nodes_to_children(q_nodes)))
            case BlockType.UNORDERED_LIST:
                list_items = block.split("\n")
                list_items_children = []
                for list_item in list_items:
                    list_item = list_item.removeprefix("- ")
                    li_nodes = text_to_textnodes(list_item)
                    list_items_children.append(ParentNode("li", text_nodes_to_children(li_nodes)))
                children.append(ParentNode("ul", list_items_children))
            case BlockType.ORDERED_LIST:
                list_items = block.split("\n")
                list_items_children = []
                for list_item in list_items:
                    list_item = re.sub(r"^\d+\.\ ", "", list_item)
                    li_nodes = text_to_textnodes(list_item)
                    list_items_children.append(ParentNode("li", text_nodes_to_children(li_nodes)))
                children.append(ParentNode("ol", list_items_children))
    return ParentNode("div", children)