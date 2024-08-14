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
from fineract_client.apis.self_share_products_api import SelfShareProductsApi  # noqa: E501
from fineract_client.rest import ApiException


class TestSelfShareProductsApi(unittest.TestCase):
    """SelfShareProductsApi unit test stubs"""

    def setUp(self):
        self.api = SelfShareProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_all_products1(self):
        """Test case for retrieve_all_products1

        """
        pass

    def test_retrieve_product1(self):
        """Test case for retrieve_product1

        """
        pass


if __name__ == '__main__':
    unittest.main()
