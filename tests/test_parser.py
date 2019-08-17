from typing import List

import pytest

from dunder_run.parser import ArgumentParser


def test_parse_list_of_args(parser):
    with pytest.raises(NotImplementedError):
        parser.add_argument('numbers', List[int])


def test_parse_boolean(parser):
    parser.add_argument('activated', bool)

    args = parser.parse_args(['--activated'])
    assert args['activated']


def test_parse_boolean_not_provided(parser):
    parser.add_argument('deactivated', bool)

    args = parser.parse_args([])
    assert not args['deactivated']


def test_parse_int(parser):
    parser.add_argument('number', int)

    args = parser.parse_args(['4'])
    assert args['number'] == 4


def test_parse_not_supported_type(parser):
    with pytest.raises(ValueError):
        parser.add_argument('whatever', dict)
