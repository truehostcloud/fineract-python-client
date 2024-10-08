# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fineract_client
from fineract_client.apis.users_api import UsersApi  # noqa: E501
from fineract_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create15(self):
        """Test case for create15

        Create a User  # noqa: E501
        """
        pass

    def test_delete23(self):
        """Test case for delete23

        Delete a User  # noqa: E501
        """
        pass

    def test_get_user_template(self):
        """Test case for get_user_template

        """
        pass

    def test_post_users_template(self):
        """Test case for post_users_template

        """
        pass

    def test_retrieve_all41(self):
        """Test case for retrieve_all41

        Retrieve list of users  # noqa: E501
        """
        pass

    def test_retrieve_one31(self):
        """Test case for retrieve_one31

        Retrieve a User  # noqa: E501
        """
        pass

    def test_template22(self):
        """Test case for template22

        Retrieve User Details Template  # noqa: E501
        """
        pass

    def test_update26(self):
        """Test case for update26

        Update a User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
