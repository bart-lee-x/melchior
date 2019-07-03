from dataclasses import dataclass, asdict
from typing import List

from dataclasses_json import dataclass_json

from melchior.model.template.output.common import Link, Button


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

