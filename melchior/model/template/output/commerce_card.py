from dataclasses import dataclass, asdict
from typing import List

from dataclasses_json import dataclass_json

from melchior.model.template.output.common import Thumbnail, Profile, Button


@dataclass
@dataclass_json
class CommerceCard:
    description: str
    thumbnail: Thumbnail
    price: int
    currency: str  # won
    profile: Profile
    buttons: List[Button]  # kakaotalk에서는 1개 이상

