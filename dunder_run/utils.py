from importlib import util
from pathlib import Path
from typing import Callable, List


def get_function_from_file(program_name: str) -> Callable[..., None]:
    try:
        filename, function_name = program_name.split(':')
    except ValueError:
        filename = program_name
        function_name = 'main'

    path_to_file = Path(filename)
    spec = util.spec_from_file_location(function_name, path_to_file)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    function = getattr(module, function_name)

    if not function:
        message = f"'{function_name}' function not found in file '{filename}'"
        raise AttributeError(message)

    return function
