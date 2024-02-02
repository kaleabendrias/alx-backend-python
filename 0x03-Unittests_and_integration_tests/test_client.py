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

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        '''self descriptive'''
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))
