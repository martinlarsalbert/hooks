import pytest
import shutil

import os
from summary.converter import convert_to_markdown, get_relative_path, find_paths, append_paths, append_new_body
import tests

summary_file_name = 'summary.ipynb'
readme_file_name = 'README.md'

@pytest.fixture
def summary_file_path():
    yield os.path.join(tests.path,summary_file_name)

@pytest.fixture
def readme_file_path():
    yield os.path.join(tests.path,readme_file_name)

@pytest.fixture
def test_repo(tmpdir, summary_file_path, readme_file_path):

    sub_directory_path = os.path.join(str(tmpdir),'path')
    os.mkdir(sub_directory_path)

    summary_file_path_test = os.path.join(sub_directory_path,summary_file_name)
    shutil.copyfile(summary_file_path, summary_file_path_test)

    readme_file_name_test = os.path.join(str(tmpdir), readme_file_name)
    shutil.copyfile(readme_file_name, readme_file_name_test)

    retval = os.getcwd()
    os.chdir(str(tmpdir))

    yield summary_file_path_test, readme_file_name_test

    os.chdir(retval)

def test_convert_to_markdown(test_repo):

    summary_file_path=test_repo[0]

    body, resources = convert_to_markdown(filename=summary_file_path)

    a=1

def test_get_relative_path(test_repo):

    summary_file_path = test_repo[0]
    readme_path = test_repo[1]

    rel_path = get_relative_path(summary_filename=summary_file_path, readme_path=readme_path)
    assert os.path.abspath(rel_path) == os.path.abspath('path')

def test_get_relative_path2(test_repo):

    summary_file_path = os.path.abspath(r'notebooks/summary')
    readme_path = r''

    rel_path = get_relative_path(summary_filename=summary_file_path, readme_path=readme_path)
    assert os.path.abspath(rel_path) == os.path.abspath('notebooks')

def test_find_paths():

    s = r"""
    [test.ipynb](notebooks/test.ipynb)
    jadajada
    [test2.ipynb](notebooks/test2.ipynb)
    [test2.ipynb](notebooks/test2.ipynb)
    """

    paths = find_paths(body=s)
    assert len(paths)==2
    assert r'notebooks/test.ipynb' in paths
    assert r'notebooks/test2.ipynb' in paths

def test_append_paths():

    s = r"""
[test.ipynb](notebooks/test.ipynb)
jadajada
[test2.ipynb](notebooks/test2.ipynb)
"""

    new_body = append_paths(rel_path='rel', body=s)

    s_expected = r"""
[test.ipynb](rel/notebooks/test.ipynb)
jadajada
[test2.ipynb](rel/notebooks/test2.ipynb)
"""

    assert new_body == s_expected

def test_append_new_body(test_repo):

    summary_file_path = test_repo[0]
    readme_path = test_repo[1]

    new_s_readme = append_new_body(summary_filename=summary_file_path, readme_path=readme_path)

