import pytest

from dunder_run.exceptions import EntrypointNotFoundError
from dunder_run.utils import get_dunder_run_from_file


def test_get_dunder_function():
    filename = 'tests/utils/example_file.py'
    func = get_dunder_run_from_file(filename)
    assert func.__doc__.strip() == 'Test function.'


def test_get_dunder_function_not_found():
    filename = 'tests/utils/empty_file.py'
    with pytest.raises(EntrypointNotFoundError):
        func = get_dunder_run_from_file(filename)
