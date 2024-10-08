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
from fineract_client.apis.general_ledger_account_api import GeneralLedgerAccountApi  # noqa: E501
from fineract_client.rest import ApiException


class TestGeneralLedgerAccountApi(unittest.TestCase):
    """GeneralLedgerAccountApi unit test stubs"""

    def setUp(self):
        self.api = GeneralLedgerAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_gl_account1(self):
        """Test case for create_gl_account1

        Create a General Ledger Account  # noqa: E501
        """
        pass

    def test_delete_gl_account1(self):
        """Test case for delete_gl_account1

        Delete a GL Account  # noqa: E501
        """
        pass

    def test_get_gl_accounts_template(self):
        """Test case for get_gl_accounts_template

        """
        pass

    def test_post_gl_accounts_template(self):
        """Test case for post_gl_accounts_template

        """
        pass

    def test_retreive_account(self):
        """Test case for retreive_account

        Retrieve a General Ledger Account  # noqa: E501
        """
        pass

    def test_retrieve_all_accounts(self):
        """Test case for retrieve_all_accounts

        List General Ledger Accounts  # noqa: E501
        """
        pass

    def test_retrieve_new_account_details(self):
        """Test case for retrieve_new_account_details

        Retrieve GL Accounts Template  # noqa: E501
        """
        pass

    def test_update_gl_account1(self):
        """Test case for update_gl_account1

        Update a GL Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
