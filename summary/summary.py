import argparse

from typing import Optional
from typing import Sequence
from typing import Set

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

    

    return 0

if __name__ == '__main__':

    exit(main())