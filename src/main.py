from textnode import TextNode, TextType
import os
import shutil


def main():
    tnode = TextNode("testing time", TextType.BOLD, "google.com")
    print(tnode)
    copy_dir("/home/sam/projects/github.com/Zallu35/SSG/static", "/home/sam/projects/github.com/Zallu35/SSG/public")


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
    


main()