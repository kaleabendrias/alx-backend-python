#!/usr/bin/env python3
""" Module for testing client module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url):
        """Unit test for GithubOrgClient.public_repos method."""
        mock_public_repos_url.return_value = "mocked_url"

        with patch('client.get_json', return_value=[{"name":
                                                    "repo1"},
                                                    {"name": "repo2"}]):
            test_instance = GithubOrgClient('test')
            result = test_instance.public_repos()

        expected_result = ["repo1", "repo2"]
        mock_public_repos_url.assert_called_once()
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"some_key": "some_value"}, "my_license", False),
        ({"license": {"other_key": "some_value"}}, "my_license", False),
        ({"some_key": "some_value"}, "other_license", False),
        ({"nested": {"license": {"key": "my_license"}}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Unit test for GithubOrgClient.has_license method."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test to IntegrationGithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get and provide fixtures."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Integration test for GithubOrgClient.public_repos method."""
        test_instance = GithubOrgClient('test')
        result = test_instance.public_repos()
        self.assertEqual(result, self.expected_repos)
