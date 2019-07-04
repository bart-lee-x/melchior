from dataclasses import dataclass

from dataclasses_json import dataclass_json

from melchior.exceptions import ComponentCreateException
from melchior.validator.validator import Validator


@dataclass
@dataclass_json
class SimpleImage(Validator):

    def __init__(self, image_url: str, alt_text: str = None):

        self.imageUrl = image_url
        self.altText = alt_text

        v_result = Validator.validate_simple_image(self)
        if v_result.is_invalid():
            raise ComponentCreateException(v_result)

    imageUrl: str
    altText: str = ""

