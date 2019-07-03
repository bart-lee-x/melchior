import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Union, Tuple, Callable

from dataclasses_json import dataclass_json

from melchior.validator.validator import Validator


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


"""
"outputs": [
            {
                "simpleText": {
                    "text": "간단한 텍스트 요소입니다."
                }
            }
        ]
"""


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


@dataclass
@dataclass_json
class SimpleText(Validator):
    text: str


@dataclass
@dataclass_json
class SimpleImage(Validator):
    imageUrl: str
    altText: str = ""


@dataclass
@dataclass_json
class BasicCard:
    title: str
    description: str
    thumbnail: Thumbnail
    buttons: List[Button]


@dataclass
@dataclass_json
class CommerceCard:
    description: str
    thumbnail: Thumbnail
    price: int
    currency: str  # won
    profile: Profile
    buttons: List[Button]  # kakaotalk에서는 1개 이상


@dataclass_json
@dataclass
class HeadItem:
    title: str
    imageUrl: str = None


@dataclass_json
@dataclass
class BodyItem:
    title: str
    description: str
    imageUrl: str
    link: Link


@dataclass
@dataclass_json
class ListCard:
    header: HeadItem
    items: List[BodyItem]
    buttons: List[Button]  # kakaotalk에서는 최대 5개


@dataclass
@dataclass_json
class Carousel:
    type: str
    items: List[Union[BasicCard, CommerceCard]]


@remove_null_value_field
@dataclass_json
@dataclass
class Component:
    simpleText: SimpleText = None
    simpleImage: SimpleImage = None
    basicCard: BasicCard = None
    carousel: Carousel = None
