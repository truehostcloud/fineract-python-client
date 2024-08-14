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
from fineract_client.apis.client_collateral_management_api import ClientCollateralManagementApi  # noqa: E501
from fineract_client.rest import ApiException


class TestClientCollateralManagementApi(unittest.TestCase):
    """ClientCollateralManagementApi unit test stubs"""

    def setUp(self):
        self.api = ClientCollateralManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_collateral(self):
        """Test case for add_collateral

        Add New Collateral For a Client  # noqa: E501
        """
        pass

    def test_delete_collateral1(self):
        """Test case for delete_collateral1

        Delete Client Collateral  # noqa: E501
        """
        pass

    def test_get_client_collateral(self):
        """Test case for get_client_collateral

        Get Clients Collateral Products  # noqa: E501
        """
        pass

    def test_get_client_collateral_data(self):
        """Test case for get_client_collateral_data

        Get Client Collateral Data  # noqa: E501
        """
        pass

    def test_get_client_collateral_template(self):
        """Test case for get_client_collateral_template

        Get Client Collateral Template  # noqa: E501
        """
        pass

    def test_update_collateral1(self):
        """Test case for update_collateral1

        Update New Collateral of a Client  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
