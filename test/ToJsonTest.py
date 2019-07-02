import unittest

from melchior.model.template.output.component import SimpleText, Component


class TestToJsonSimple(unittest.TestCase):

    def test_simple(self):
        simple_text = SimpleText('hi')
        print(simple_text.to_json())
        self.assertEqual('hi', simple_text.text)

    def test_component_with_simple_text_only(self):
        simple_text = SimpleText('hell')
        component_with_simple_text = Component(simpleText=simple_text)
        print(component_with_simple_text.to_json())
        self.assertEqual('hell', component_with_simple_text.simpleText.text)
