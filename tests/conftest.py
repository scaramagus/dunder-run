import pytest

from dunder_run.parser import ArgumentParser


@pytest.fixture
def parser():
    return ArgumentParser(description='Test parser')
