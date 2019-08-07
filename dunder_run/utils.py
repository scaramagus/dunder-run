from importlib import util
from inspect import signature
from pathlib import Path
from typing import Callable, List

from .exceptions import EntrypointNotFoundError


def get_dunder_run_from_file(filename: str) -> Callable[..., None]:
    """Extracts the __run__ function from the given Python module.
    """
    path_to_file = Path(filename)
    spec = util.spec_from_file_location('__run__', path_to_file)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)

    try:
        return module.__run__
    except AttributeError:
        message = f"__run__ function not found in file '{filename}'"
        raise EntrypointNotFoundError(message) from None


def get_parameters(run_function: Callable[..., None]) -> List:
    return signature(run_function).parameters.values()

