import pytest

from dunder_run.utils import get_function_from_file
from .utils import sample_functions


def test_get_dunder_function_default():
    filename = 'tests/utils/sample_functions.py'

    func = get_function_from_file(filename)
    assert func.__doc__ == sample_functions.main.__doc__


def test_get_dunder_function_custom():
    filename = 'tests/utils/sample_functions.py:main'

    func = get_function_from_file(filename)
    assert func.__doc__ == sample_functions.main.__doc__


def test_get_dunder_function_not_found():
    filename = 'tests/utils/sample_functions.py:not_found'

    with pytest.raises(AttributeError):
        get_function_from_file(filename)
