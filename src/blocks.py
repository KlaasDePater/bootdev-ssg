def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    split = markdown.split("\n\n")
    for s in split:
        if len(s) > 0 and s != "\n":
            blocks.append(s.strip())
    return blocks