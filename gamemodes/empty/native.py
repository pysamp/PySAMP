#import _pynative
import io
from typing import List, Dict, Any, Optional
import os
import re


_ARGUMENT_TYPES = {
    'i': 'Decimal',
    'd': 'Decimal',
    'f': 'Float',
    'b': 'Boolean',
    's': 'String'
}


class _Argument(object):
    def __init__(self, name: str, arg_type: Optional[str], default: Optional[Any], is_array: Optional[bool] = False, is_reference: Optional[bool] = False):
        self.name = name
        self.arg_type = arg_type
        self.default = default
        self.is_array = is_array
        self.is_reference = is_reference


class _NativeCallable(object):
    def __init__(self, name: str, return_type: str, arguments: List[_Argument]):
        self.name = name
        self.return_type = return_type
        self.arguments = arguments


class _Callback(object):
    def __init__(self, name: str, arguments: str):
        self.name = name
        self.arguments = arguments


definition_regex = re.compile(r"^[ ]*#define[ ]+(?P<name>[a-zA-Z_$][a-zA-Z_$0-9]*)[ ]+(?P<value>.*)((//|/\*).*)?$")
native_regex = re.compile(
    r"^[ ]*native[ ]+((?P<return_type>[a-zA-Z_$0-9]*):)?(?P<name>[a-zA-Z_$][a-zA-Z_$0-9]*)\((?P<arguments>.*)\);$"
)
# argument_regex = re.compile(
#     r"^(?P<is_reference>&)?((?P<type>[a-zA-Z_$0-9]*):)?(?P<name>[a-zA-Z_$][a-zA-Z_$0-9]*)"
#     r"(?P<is_array>(\[\d*\])+)?"
#     r"([ ]*=[ ]*(?P<default>.+))?$"
# )

argument_regex = re.compile(
    r"^(?P<is_reference>&)?((?P<type>[a-zA-Z_$0-9]*):)?([ ]*const[ ]*)?(?P<name>[a-zA-Z_$][a-zA-Z_$0-9]*)"
    r"(?P<is_array>(\[\d*\])+)?"
    r"([ ]*=[ ]*(?P<default>.+))?$"
)


class _NativeInterface(object):
    def __init__(self, file: io.TextIOWrapper):
        self.file: io.TextIOWrapper = file
        self.natives: Dict[str, _NativeCallable] = {}
        self.callbacks: Dict[str, _Callback] = {}
        self.constants: Dict[str, Any] = {}
        self._parse()

    def _parseDefinition(self, line:str) -> bool:
        match = definition_regex.match(line)
        if match:
            name = match.group('name')
            value = match.group('value')
            value = value.strip('()')
            if value.isdecimal():
                value = int(value)
            else:
                try:
                    float_value = float(value)
                    value = float_value
                except ValueError:
                    pass
            self.constants[name] = value
        return match is not None

    def _parseNative(self, line:str):
        match = native_regex.match(line)
        if match:
            name = match.group("name")
            return_type = match.group("return_type")
            arguments = match.group("arguments")
            argument_objects = []
            for argument in arguments.split(','):
                if not argument:
                    continue
                argument = argument.strip()
                a_match = argument_regex.match(argument)
                argument_objects.append(_Argument(a_match.group('name'), a_match.group('type'),
                                a_match.group('default'), not not a_match.group('is_array'),
                                not not a_match.group('is_reference')))
            self.natives[name] = _NativeCallable(name, return_type, argument_objects)
        return match is not None

    def _parse(self):
        for line in self.file:
            if self._parseDefinition(line):
                continue
            if self._parseNative(line):
                continue


    def __getattr__(self, name:str):
        pass


if __name__ == '__main__':
    sample_inc = 'FCNPC.inc'
    if not os.path.isabs(sample_inc):
        sample_inc = os.path.join('../include/', sample_inc)
    with open(sample_inc) as f:
        native = _NativeInterface(f)
        print("Done")
        #TODO use logger
        #TODO correct parser
        #TODO support arrays! FCNPC_AddPointsToMovePath pathid, Float:points[][3], const size = sizeof(points)
        #TODO support defaults
        #TODO support references