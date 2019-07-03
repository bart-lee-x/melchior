from dataclasses import dataclass, asdict
from dataclasses_json import dataclass_json

from melchior.validator.validator import Validator


@dataclass
@dataclass_json
class SimpleText(Validator):
    text: str
