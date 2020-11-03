import pytest
import shutil

import os
from summary.converter import convert_to_markdown, get_relative_path
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

    yield summary_file_path_test, readme_file_name_test


def test_convert_to_markdown(test_repo):

    summary_file_path=test_repo[0]

    body, resources = convert_to_markdown(filename=summary_file_path)

    a=1

def test_get_relative_path(test_repo):

    summary_file_path = test_repo[0]
    readme_path = test_repo[1]

    rel_path = get_relative_path(summary_filename=summary_file_path, readme_path=readme_path)
    assert os.path.abspath(rel_path) == os.path.abspath('path')
