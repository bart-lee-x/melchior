from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from dataclasses_json import dataclass_json


# https://i.kakao.com/docs/skill-response-format
from melchior.model.template.output.component import Component, Carousel, BasicCard, SimpleImage, SimpleText


@dataclass
@dataclass_json
class Template:
    outputs: List[Component]
    quickReplies: Optional[List[Any]] = None


class TemplateBuilder:

    outputs = []

    def add(self, output: Union[SimpleText, SimpleImage, BasicCard, Carousel]):
        self.outputs.append(TemplateBuilder._warp_component(output))
        return self

    def build(self) -> Template:
        return Template(outputs=self.outputs, quickReplies=[])

    @staticmethod
    def _warp_component(output: Union[SimpleText, SimpleImage, BasicCard, Carousel]) -> Component:
        if type(output) is SimpleText:
            return Component(simpleText=output)
        elif type(output) is SimpleImage:
            return Component(simpleImage=output)
        else:
            return Component


@dataclass
@dataclass_json
class SkillResponse:
    template: Template
    context: object
    control: object  # context -> control
    data: Dict[str, Any] = dict
    version: str = "2.0"
