from dataclasses import dataclass

from dataclasses_json import dataclass_json

from melchior.validator.validator import Validator


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
class SimpleText(Validator):
    text: str
