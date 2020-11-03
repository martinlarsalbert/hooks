import os
from nbconvert import MarkdownExporter
import nbformat


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
    return rel_path

def replace_paths(summary_filename,readme_path='README.md'):

    readme_path=os.path.abspath(readme_path)
    common_prefix = base_path = os.path.commonprefix([readme_path, summary_filename])
    rel_path = os.path.relpath(summary_filename, common_prefix)  # path from README.md to summary.ipynb

    dir_path, filename = os.path.split(summary_filename)
    body, resources = convert_to_markdown(filename=summary_filename)



