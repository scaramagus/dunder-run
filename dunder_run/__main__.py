import argparse
import inspect
import sys

from .utils import get_dunder_run_from_file


def main():
    sys.argv.pop(0)

    run_function = get_dunder_run_from_file(sys.argv[0])
    parser = argparse.ArgumentParser(description=run_function.__doc__)

    signature = inspect.signature(run_function)
    parameters = signature.parameters.values()

    for parameter in parameters:
        annotation = getattr(parameter, 'annotation', str)

        if annotation is bool:
            parameter_name = f'--{parameter.name}'
            kw_options = {
                'action': 'store_const',
                'const': True,
            }
        else:
            parameter_name = parameter.name
            kw_options = {'type': annotation}

        parser.add_argument(parameter_name, **kw_options)

    args = vars(parser.parse_args())
    run_function(**args)


if __name__ == '__main__':
    main()
