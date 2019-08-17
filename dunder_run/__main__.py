import sys
from typing import get_type_hints

from .parser import ArgumentParser
from .utils import get_function_from_file


def main():
    # Since argv[0] is the path of the lib's entrypoint, we skip it
    filename = sys.argv[1]
    raw_args = sys.argv[2:]

    run_function = get_function_from_file(filename)
    parser = ArgumentParser(description=run_function.__doc__)
    parameters = get_type_hints(run_function)

    for name, annotation in parameters.items():
        parser.add_argument(name, annotation)

    args = parser.parse_args(raw_args)
    run_function(**args)


if __name__ == '__main__':
    main()
