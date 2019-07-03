import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Union, Tuple, Callable

from dataclasses_json import dataclass_json

from melchior.model.template.output.basic_card import BasicCard
from melchior.model.template.output.commerce_card import CommerceCard
from melchior.model.template.output.common import remove_null_value_field
from melchior.model.template.output.simple_imsage import SimpleImage
from melchior.model.template.output.simple_text import SimpleText




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
