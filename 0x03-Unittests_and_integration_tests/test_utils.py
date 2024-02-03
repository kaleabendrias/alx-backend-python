#!/usr/bin/env python3
""" Module for testing utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import patch, Mock
from utils import (access_nested_map, get_json)


class TestAccessNestedMap(unittest.TestCase):
    """tests for the access_netsted_map func"""
    @parameterized.expand([
        ({'x': 2}, ('x',), 2),
        ({'x': {'y': 2}}, ('x',), {'y': 2}),
        ({'x': {'y': 2}}, ('x', 'y'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test for the func access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        """Test that a KeyError is raised with the expected message."""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertIn(expected_message, str(context.exception))


class TestGetJson(unittest.TestCase):
    """tests the get_son func"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """tests the get_json func"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """tests memioze func"""
    def test_memoize(self):
        """tests memioze func"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', new_callable=Mock) as mocked:
            instance = TestClass()

            result1 = instance.a_property
            result2 = instance.a_property

            mocked.assert_called_once()

            self.assertEqual(result1, result2)
