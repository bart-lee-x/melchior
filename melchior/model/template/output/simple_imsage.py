from dataclasses import dataclass, asdict
from dataclasses_json import dataclass_json

from melchior.exceptions import ComponentCreateException
from melchior.validator.validator import Validator


@dataclass
@dataclass_json
class SimpleImage(Validator):

    def __init__(self, imageUrl: str, altText: str = None):

        self.imageUrl = imageUrl
        self.altText = altText

        v_result = Validator.validate_simple_image(self)
        if v_result.is_invalid():  # invalid
            raise ComponentCreateException(v_result)

    imageUrl: str
    altText: str = ""

