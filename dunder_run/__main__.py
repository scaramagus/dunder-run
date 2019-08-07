import inspect
import sys

from .parser import ArgumentParser
from .utils import get_dunder_run_from_file, get_parameters


def main():
    # Since argv[0] is the path of the lib's entrypoint, we skip it
    filename = sys.argv[1]
    raw_args = sys.argv[2:]

    run_function = get_dunder_run_from_file(filename)
    parser = ArgumentParser(description=run_function.__doc__)
    parameters = get_parameters(run_function)

    for parameter in parameters:
        parser.add_argument(parameter.name, parameter.annotation)

    args = parser.parse_args(raw_args)
    run_function(**args)


if __name__ == '__main__':
    main()
