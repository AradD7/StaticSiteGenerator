import os
import shutil
from generate_public_dir import recursive_move
from block_markdown import extract_title
from markdown_to_html import markdown_to_html_node

dir_path_static = "./static"
dir_path_public = "./public"



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path)
    md_string = md_file.read()
    html_file = open(template_path)
    html_string = html_file.read()
    
    html_content = markdown_to_html_node(md_string).to_html()
    html_title = extract_title(md_string)

    final_html_string = html_string.replace("{{ Title }}", html_title).replace("{{ Content }}", html_content)
    if not(os.path.exists(os.path.dirname(dest_path))):
        os.makedirs(os.path.dirname(dest_path))
    final_html_file = open(dest_path, 'w')
    final_html_file.write(final_html_string)

    md_file.close()
    html_file.close()
    final_html_file.close()
    return None

def generate_page_recursively(from_path, template_path, dest_path):
    if not(os.path.exists(dest_path)):
        os.mkdir(dest_path)
    for entry in os.listdir(from_path):
        if os.path.isfile(os.path.join(from_path, entry)):
            generate_page(os.path.join(from_path, entry), template_path, os.path.join(dest_path, entry.replace(".md", ".html")))

        else:
            generate_page_recursively(os.path.join(from_path, entry), template_path, os.path.join(dest_path, entry))



def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    recursive_move(dir_path_static, dir_path_public)

    generate_page_recursively("./content", "./template.html", "./public")

    

main()
