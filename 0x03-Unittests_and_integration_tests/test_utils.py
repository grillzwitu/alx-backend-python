#!/usr/bin/env python3
"""unit test for utils.py
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''class for unittest for nested_map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        '''test for nested_map method'''
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_value):
        '''test for nested_map exceptions'''
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(repr(err.exception), repr(expected_value))


class TestGetJson(unittest.TestCase):
    '''class for unittests for get and get_json methods'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict):
        '''test for expected of get_json method'''
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''class for unittests for memoization'''
    def test_memoize(self):
        '''tests that a_method is only called once'''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
