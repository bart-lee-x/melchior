from dataclasses import dataclass, asdict
from typing import List

from dataclasses_json import dataclass_json

from melchior.model.template.output.common import Thumbnail, Button


@dataclass
@dataclass_json
class BasicCard:
    title: str
    description: str
    thumbnail: Thumbnail
    buttons: List[Button]

