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
from fineract_client.apis.client_identifier_api import ClientIdentifierApi  # noqa: E501
from fineract_client.rest import ApiException


class TestClientIdentifierApi(unittest.TestCase):
    """ClientIdentifierApi unit test stubs"""

    def setUp(self):
        self.api = ClientIdentifierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_client_identifier(self):
        """Test case for create_client_identifier

        Create an Identifier for a Client  # noqa: E501
        """
        pass

    def test_delete_client_identifier(self):
        """Test case for delete_client_identifier

        Delete a Client Identifier  # noqa: E501
        """
        pass

    def test_new_client_identifier_details(self):
        """Test case for new_client_identifier_details

        Retrieve Client Identifier Details Template  # noqa: E501
        """
        pass

    def test_retrieve_all_client_identifiers(self):
        """Test case for retrieve_all_client_identifiers

        List all Identifiers for a Client  # noqa: E501
        """
        pass

    def test_retrieve_client_identifiers(self):
        """Test case for retrieve_client_identifiers

        Retrieve a Client Identifier  # noqa: E501
        """
        pass

    def test_update_client_identifer(self):
        """Test case for update_client_identifer

        Update a Client Identifier  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
