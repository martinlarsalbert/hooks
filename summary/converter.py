import os
from nbconvert import MarkdownExporter
import nbformat
import re

class BadLinkError(ValueError):pass

def convert_to_markdown(filename):

    with open(filename, mode='r') as file:
        notebook_str=file.read()

    notebook = nbformat.reads(notebook_str, as_version=4)

    markdown_exporter = MarkdownExporter()

    (body, resources) = markdown_exporter.from_notebook_node(notebook)

    return (body, resources)

def get_relative_path(summary_filename,readme_path):

    _,summary_name = os.path.split(summary_filename)
    readme_path = os.path.abspath(readme_path)
    common_prefix = base_path = os.path.commonprefix([readme_path, summary_filename])
    rel_path = os.path.relpath(summary_filename, common_prefix)  # path from README.md to summary.ipynb
    rel_path=rel_path.replace(summary_name,'')
    rel_path = rel_path.replace("\\","/")

    return rel_path[0:-1]

def find_paths(body:str)->list:
    paths = re.findall(pattern=r'\]\(([^)]*)', string=body)
    paths = list(set(paths))  # only uniques
    return paths

def append_paths(rel_path:str,body:str, verify_paths=True)->str:
    """
    Links looking like:
    (example.ipynb)[notebooks/example.ipynb]
    Will be changed to:
    (example.ipynb)[{rel_path}/notebooks/example.ipynb]
    """
    new_body = str(body)
    paths = find_paths(body=body)

    missing = []
    for path in paths:
        if 'http' in path:
            continue  # Skipping urls.

        new_path = '%s/%s' % (rel_path,path)
        if verify_paths:
            if not os.path.exists(new_path):
                missing.append(new_path)

        pat = r'(%s)'
        new_body = re.sub(pattern=pat%path, repl=new_path, string=new_body)

    if verify_paths:
        if len(missing)>0:
            raise BadLinkError('The follwing paths are invalid:\n%s' % missing)

    return new_body

def replace_paths(summary_filename,readme_path='README.md', verify_paths=True):

    body, resources = convert_to_markdown(filename=summary_filename)
    rel_path = get_relative_path(summary_filename, readme_path)
    new_body = append_paths(rel_path=rel_path, body=body, verify_paths=verify_paths)
    return new_body

def append_new_body(summary_filename,readme_path='README_.md', verify_paths=True):

    new_body = replace_paths(summary_filename=summary_filename, readme_path=readme_path,verify_paths=verify_paths)

    with open(readme_path, mode='r') as file:
        s_readme = file.read()

    new_s_readme = '%s\n%s' % (s_readme ,new_body)

    return new_s_readme






