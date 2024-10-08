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
from fineract_client.apis.account_transfers_api import AccountTransfersApi  # noqa: E501
from fineract_client.rest import ApiException


class TestAccountTransfersApi(unittest.TestCase):
    """AccountTransfersApi unit test stubs"""

    def setUp(self):
        self.api = AccountTransfersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create4(self):
        """Test case for create4

        Create new Transfer  # noqa: E501
        """
        pass

    def test_retrieve_all18(self):
        """Test case for retrieve_all18

        List account transfers  # noqa: E501
        """
        pass

    def test_retrieve_one9(self):
        """Test case for retrieve_one9

        Retrieve account transfer  # noqa: E501
        """
        pass

    def test_template5(self):
        """Test case for template5

        Retrieve Account Transfer Template  # noqa: E501
        """
        pass

    def test_template_refund_by_transfer(self):
        """Test case for template_refund_by_transfer

        Retrieve Refund of an Active Loan by Transfer Template  # noqa: E501
        """
        pass

    def test_template_refund_by_transfer_post(self):
        """Test case for template_refund_by_transfer_post

        Refund of an Active Loan by Transfer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
