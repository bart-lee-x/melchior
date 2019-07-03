import json
import unittest

from melchior.model.template.output.component import SimpleText, Component, SimpleImage


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
