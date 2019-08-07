import argparse
from inspect import Parameter, signature
from typing import Any, Dict, List, Tuple


class ArgumentParser:

    def __init__(self, description: str):
        self._parser = argparse.ArgumentParser(
            description=description
        )

    def _get_bool_options(self, parameter_name: str) -> Tuple[str, Dict]:
        parameter_name = f'--{parameter_name}'
        kw_options = {
            'action': 'store_const',
            'const': True,
        }
        return parameter_name, kw_options

    def add_argument(self, name: str, annotation: Any):
        if annotation is bool:
            parameter_name, kw_options = self._get_bool_options(name)
        else:
            parameter_name = name
            kw_options = {'type': annotation}

        self._parser.add_argument(parameter_name, **kw_options)

    def parse_args(self, raw_args: List[str]) -> Dict:
        args = self._parser.parse_args(raw_args)
        return vars(args)


