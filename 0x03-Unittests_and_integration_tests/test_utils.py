#!/usr/bin/env python3
""" Module for testing utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """tests for the access_netsted_map func"""
    @parameterized.expand([
        ({'x': 2}, ('x',), 2),
        ({'x': {'y': 2}}, ('x',), {'y': 2}),
        ({'x': {'y': 2}}, ('x', 'y'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, "a", KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_key_error(self,
                                         nested_map, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)
