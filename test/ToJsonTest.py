import json
import unittest
from pprint import pprint

from melchior.model.skill.request import SkillRequest
from melchior.model.template.output.component import SimpleText, Component, SimpleImage


skillRequestString = """
{
    "intent": {
      "id": "5a25025be821273c3718893c",
      "name": "FALLBACK INTENT",
      "extra": {
        "reason": {
          "code": 1,
          "message": "OK"
        }
      }
    },
    "userRequest": {
      "timezone": "Asia/Seoul",
      "params": {
        "surface": "Kakaotalk.plusfriend"
      },
      "block": {
        "id": "5a25025be821273c3718893c",
        "name": "FALLBACK INTENT"
      },
      "utterance": "아하하허ㅏ라하하",
      "lang": "kr",
      "user": {
        "id": "d09055b49c95a8e6c10fc8d8c01325f50a713971f2ec0b4c91af850e9805890be3",
        "type": "botUserKey",
        "properties": {
          "botUserKey": "d09055b49c95a8e6c10fc8d8c01325f50a713971f2ec0b4c91af850e9805890be3",
          "accountId": "1",
          "plusfriendUserKey": "Bx4i0FQtFSq0",
          "talkUserId": "1"
        }
      }
    },
    "contexts": [],
    "skillOption": {
      "isTrusted": true,
      "botName": " 번역베타",
      "isMini": false,
      "isCbt": true,
      "botId": "5a25021f26c6636625e33537",
      "timeout": 5000
    },
    "bot": {
      "id": "5a25021f26c6636625e33537",
      "name": " 번역베타"
    },
    "action": {
      "name": "번역",
      "clientExtra": null,
      "params": {},
      "id": "5a250244e821273c3718893a",
      "detailParams": {}
    }
  }
"""

class TestToJsonSimple(unittest.TestCase):

    def test_simple(self):
        simple_text = SimpleText('hi')
        self.assertEqual('hi', simple_text.text)

    def test_component_with_simple_text_only(self):
        simple_text = SimpleText('hell')
        component_with_simple_text = Component(simpleText=simple_text)
        self.assertEqual('hell', component_with_simple_text.simpleText.text)

    def test_component_simple_image(self):
        simple_image = SimpleImage(imageUrl='hell')
        component_with_simple_text = Component(simpleImage=simple_image)
        self.assertEqual('hell', component_with_simple_text.simpleImage.imageUrl)

    def test_remove_field_if_null_value(self):
        simple_text = SimpleText('hell')
        component_with_simple_text = Component(simpleText=simple_text)
        self.assertEqual('hell', component_with_simple_text.simpleText.text)

        converted_component = json.loads(component_with_simple_text.to_json())
        self.assertEqual('hell', converted_component['simpleText']['text'])

        with self.assertRaises(KeyError):
            converted_component['simpleImage']


class ValidationTest(unittest.TestCase):

    def test_simple_validation(self):
        simple_text = SimpleText('hi')
        self.assertTrue(simple_text.is_valid())

        simple_image = SimpleImage('hi')
        self.assertFalse(simple_image.is_valid())

        simple_image2 = SimpleImage('http://')
        self.assertTrue(simple_image2.is_valid())


class UsageTest(unittest.TestCase):

    def test_skill_request_can_deserialize_from_chappie(self):
        """
        내가 스킬 서버라면 스킬 요청을 채피로부터 받아서, deserialize 가능해야 한다.
        :return:
        """
        skillRequestString

        skillRequest = SkillRequest.from_json(skillRequestString)
        pprint(skillRequest)
        self.assertEqual("5a25025be821273c3718893c", skillRequest.intent.id)
        self.assertEqual("FALLBACK INTENT", skillRequest.intent.name)
        self.assertEqual(skillRequest.intent.extra["reason"]["code"], 1)
