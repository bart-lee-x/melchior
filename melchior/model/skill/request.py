from dataclasses import dataclass
from typing import Any, List, Dict, Optional

from dataclasses_json import dataclass_json


@dataclass
@dataclass_json
class Intent:
    id: str
    name: str
    extra: Dict[str, Any]


@dataclass
@dataclass_json
class Block:
    id: str
    name: str


@dataclass
@dataclass_json
class User:
    id: str
    type: str
    properties: Dict[str, str]


@dataclass
@dataclass_json
class UserRequest:
    timezone: str
    params: Dict[str, Any]
    block: Block
    utterance: str
    lang: str
    user: User


@dataclass
@dataclass_json
class SkillOption:  # 이거 뭐죠
    isTrusted: bool
    botName: str
    isMini: bool
    isCbt: bool
    botId: str
    timeout: int


@dataclass
@dataclass_json
class Action:
    name: str
    clientExtra: Optional[Dict[str, Any]]
    params: Dict[str, Any]
    id: str
    detailParams: Dict[str, Any]


@dataclass
@dataclass_json
class SkillRequest:
    intent: Intent
    userRequest: UserRequest
    contexts: List[Any]
    skillOption: SkillOption
    action: Action
