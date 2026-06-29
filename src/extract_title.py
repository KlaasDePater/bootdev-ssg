import re

def extract_title(markdown: str) -> str:
    split = markdown.split("\n\n")
    if len(split) == 0:
        raise Exception("Markdown content is empty")
    match_title = re.findall(r"^#\ (.+)", split[0])
    if not match_title:
        raise Exception("Markdown content has no properly formatted header")
    return match_title[0]