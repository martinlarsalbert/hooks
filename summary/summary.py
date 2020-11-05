import argparse

from typing import Optional
from typing import Sequence
from typing import Set

import os

from summary.converter import append_new_body

def find_summary(filenames:list,summary_name='summary.ipynb')->str:

    for filename in filenames:
        if summary_name in filename:
            return filename

    return None



def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )

    args = parser.parse_args(argv)

    summary_path = find_summary(filenames=args.filenames)
    if summary_path is None:
        return 0

    print('Appending summary.ipynb to README.md')
    print(os.getcwd())

    summary_path = os.path.abspath(summary_path)

    readme_path_head = 'README_.md'  # before appending
    readme_path = 'README.md'        # after appending

    readme_path_head = os.path.abspath(readme_path_head)
    readme_path = os.path.abspath(readme_path)

    new_s_readme = append_new_body(summary_filename=summary_path, readme_path=readme_path_head)
    with open(readme_path, mode='w') as file:
        file.write(new_s_readme)

    return 0

if __name__ == '__main__':
    exit(main())