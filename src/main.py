from textnode import TextNode, TextType
import os
import shutil
import sys
from Markdown_Functions import markdown_to_html_node, extract_title


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_dir("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)


def copy_dir(source, dest):
    if not os.path.exists(source):
        raise Exception("invalid source path!:")
    if os.path.exists(dest):    
        shutil.rmtree(dest)
    os.mkdir(dest)
    copylist = os.listdir(source)
    for d in copylist:
        spath = f"{source}/{d}"
        dpath = f"{dest}/{d}"
        if os.path.isfile(spath):
            shutil.copy(spath, dpath)
        else:
            copy_dir(spath, dpath)
    
def generate_page(from_path, dest_path, template_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown_string = f.read()
    with open(template_path) as t:
        template_string = t.read()
    Pnode = markdown_to_html_node(markdown_string)
    html_string = Pnode.to_html()
    title_string = extract_title(markdown_string)
    template_string = template_string.replace('{{ Title }}', title_string)
    template_string = template_string.replace('{{ Content }}', html_string)
    template_string.replace('href="/', f'href="{basepath}')
    template_string.replace('src="/', f'src="{basepath}')
    with open(dest_path, 'w') as d:
        d.write(template_string)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    for d in content_list:
        content_path = f"{dir_path_content}/{d}"
        destination_path = f"{dest_dir_path}/{d}"
        if os.path.isfile(content_path):
            destination_path = destination_path.replace(".md", ".html")
            generate_page(content_path, destination_path, template_path, basepath)
        else:
            os.mkdir(destination_path)
            generate_pages_recursive(content_path, template_path, destination_path, basepath)
    

main()