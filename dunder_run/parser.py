import argparse
from typing import Any, Dict, List, Tuple, Union


ArgumentType = Union[
    str, int, bool,
    List[str], List[int],
]


class ArgumentParser:

    def __init__(self, description: str):
        self._parser = argparse.ArgumentParser(
            description=description
        )

    def _get_list_options(self, parameter_name: str, item_type: Union[str, int]) -> Tuple[str, Dict]:
        raise NotImplementedError('Argument list is in the works!')

    def add_argument(self, name: str, annotation: ArgumentType):
        if annotation in (list, List[str], List[int]):
            item_type = annotation.__args__[0]  # Yes, that's how you access item types...
            parameter_name, kw_options = self._get_list_options(name, item_type)
        elif annotation is bool:
            parameter_name = f'--{name}'
            kw_options = {'action': 'store_true'}
        elif annotation in (str, int):
            # Integers and strings get the simplest treatment
            parameter_name = name
            kw_options = {'type': annotation}
        else:
            raise ValueError(f'Unsupported annotation type "{annotation}"')

        self._parser.add_argument(parameter_name, **kw_options)

    def parse_args(self, raw_args: List[str]) -> Dict:
        args = self._parser.parse_args(raw_args)
        return vars(args)


