import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Union, Tuple, Callable

from dataclasses_json import dataclass_json


def remove_null_value_field(cls):
    def remove_nulls(d):
        return {k: v for k, v in d.items() if v is not None}

    def to_json(self,
                *,
                skipkeys: bool = False,
                ensure_ascii: bool = True,
                check_circular: bool = True,
                allow_nan: bool = True,
                indent: Optional[Union[int, str]] = None,
                separators: Tuple[str, str] = None,
                default: Callable = None,
                sort_keys: bool = False,
                **kw) -> str:
        return json.dumps(remove_nulls(asdict(self)),
                          skipkeys=skipkeys,
                          ensure_ascii=ensure_ascii,
                          check_circular=check_circular,
                          allow_nan=allow_nan,
                          indent=indent,
                          separators=separators,
                          default=default,
                          sort_keys=sort_keys,
                          **kw)

    cls.to_json = to_json
    return cls


@dataclass
@dataclass_json
class Link:
    web: str
    mobile: str = None
    pc: str = None
    mac: str = None
    ios: str = None
    android: str = None


@remove_null_value_field
@dataclass
@dataclass_json
class Thumbnail:
    imageUrl: str
    link: Link
    fixedRatio: bool
    width: int
    height: int


@dataclass()
@dataclass_json
class Profile:
    text: str


@dataclass
@dataclass_json
class Button:
    text: str  # TODO

