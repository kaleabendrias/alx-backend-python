#!/usr/bin/env python3
""" Module for testing client module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class to test the client module"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test that GithubOrgClient.org returns the correct value"""
        github_client = GithubOrgClient(org_name)
        github_client.org
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}".
                                              format(org_name))

    def test_public_repos_url(self):
        """Test _public_repos_url property behavior with mocked 'org'"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org_property:
            payload = {"repos_url": "https://github.com/kaleabendrias"}
            mock_org_property.return_value = payload
            test_instance = GithubOrgClient('test')
            result = test_instance._public_repos_url
            self.assertEqual(result, payload["repos_url"])