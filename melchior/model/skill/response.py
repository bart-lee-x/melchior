from dataclasses import dataclass
from dataclasses_json import dataclass_json


# https://i.kakao.com/docs/skill-response-format


@dataclass
@dataclass_json
class SkillResponse:
    version: str
    template: object
    context: object
    data: dict
    control: object  # context -> control


@dataclass
class Template:
    outputs: list
    quickReplies: list
