import argparse
import inspect
from importlib import util
from pathlib import Path
import sys
from typing import Callable


class EntrypointNotFoundError(Exception):
    pass


def _get_entrypoint_function(filename: str) -> Callable[..., None]:
    """Extracts the __run__ function from the given Python module.
    """
    path_to_file = Path('.') / filename
    spec = util.spec_from_file_location('__run__', path_to_file)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)

    try:
        return module.__run__
    except AttributeError:
        message = f"__run__ function not found in file '{filename}'"
        raise EntrypointNotFoundError(message) from None


def main():
    sys.argv.pop(0)

    entrypoint_function = _get_entrypoint_function(sys.argv[0])
    parser = argparse.ArgumentParser(description=entrypoint_function.__doc__)

    signature = inspect.signature(entrypoint_function)
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
    entrypoint_function(**args)


if __name__ == '__main__':
    main()
