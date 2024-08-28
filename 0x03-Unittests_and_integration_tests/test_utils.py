#!/usr/bin/env python3
""" unit test """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, MagicMock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ test class for nested map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test case"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ test case """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ class TestGetJson """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """Test output of get_json is equal to test_payload"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response) as mock:
            self.assertEqual(get_json(url), test_payload)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
