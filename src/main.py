import os
import shutil
from pathlib import Path
import sys

from textnode import *
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def copy_content(src_path="static/", dst_path="public/"):
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
        print(f"Cleared {dst_path}")
    os.mkdir(dst_path)
    items = os.listdir(src_path)
    for item in items:
        joined_src_path = os.path.join(src_path, item)
        joined_dst_path = os.path.join(dst_path, item)
        if os.path.isfile(joined_src_path):
            print(f"Copying {joined_src_path} -> {joined_dst_path}")
            shutil.copy(joined_src_path, joined_dst_path)
        else:
            copy_content(joined_src_path, joined_dst_path)

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page: {from_path} -> {dest_path} using {template_path}")
    with open(from_path, 'r') as content_file:
        md_content = content_file.read()
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    filled_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(filled_template)

def generate_pages_recursively(dir_path_content="content/", template_path="template.html", dest_dir_path="public/", basepath="/"):
    items = os.listdir(dir_path_content)
    for item in items:
        joined_src_path = os.path.join(dir_path_content, item)
        joined_dst_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(joined_src_path):
            joined_dst_path = joined_dst_path.removesuffix(".md")
            joined_dst_path += ".html"
            generate_page(joined_src_path, template_path, joined_dst_path, basepath)
        else:
            generate_pages_recursively(joined_src_path, template_path, joined_dst_path, basepath)

def main():
    arguments = sys.argv
    if len(arguments) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if not basepath.endswith("/"):
        raise Exception(f"Basepath {basepath} does not end with a '/'")
    print(f"Basepath will be: {basepath}")
    copy_content("static/", "docs/")
    generate_pages_recursively("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()