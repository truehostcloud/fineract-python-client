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
from fineract_client.apis.teller_cash_management_api import TellerCashManagementApi  # noqa: E501
from fineract_client.rest import ApiException


class TestTellerCashManagementApi(unittest.TestCase):
    """TellerCashManagementApi unit test stubs"""

    def setUp(self):
        self.api = TellerCashManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_allocate_cash_to_cashier(self):
        """Test case for allocate_cash_to_cashier

        Allocate Cash To Cashier  # noqa: E501
        """
        pass

    def test_create_cashier(self):
        """Test case for create_cashier

        Create Cashiers  # noqa: E501
        """
        pass

    def test_create_teller(self):
        """Test case for create_teller

        Create teller  # noqa: E501
        """
        pass

    def test_delete_cashier(self):
        """Test case for delete_cashier

        Delete Cashier  # noqa: E501
        """
        pass

    def test_delete_teller(self):
        """Test case for delete_teller

        """
        pass

    def test_find_cashier_data(self):
        """Test case for find_cashier_data

        Retrieve a cashier  # noqa: E501
        """
        pass

    def test_find_teller(self):
        """Test case for find_teller

        Retrieve tellers  # noqa: E501
        """
        pass

    def test_find_transaction_data(self):
        """Test case for find_transaction_data

        """
        pass

    def test_get_cashier_data1(self):
        """Test case for get_cashier_data1

        List Cashiers  # noqa: E501
        """
        pass

    def test_get_cashier_template(self):
        """Test case for get_cashier_template

        Find Cashiers  # noqa: E501
        """
        pass

    def test_get_cashier_txn_template(self):
        """Test case for get_cashier_txn_template

        Retrieve Cashier Transaction Template  # noqa: E501
        """
        pass

    def test_get_journal_data(self):
        """Test case for get_journal_data

        """
        pass

    def test_get_teller_data(self):
        """Test case for get_teller_data

        List all tellers  # noqa: E501
        """
        pass

    def test_get_transaction_data(self):
        """Test case for get_transaction_data

        """
        pass

    def test_get_transactions_for_cashier(self):
        """Test case for get_transactions_for_cashier

        Retrieve Cashier Transaction  # noqa: E501
        """
        pass

    def test_get_transactions_wtih_summary_for_cashier(self):
        """Test case for get_transactions_wtih_summary_for_cashier

        Transactions Wtih Summary For Cashier  # noqa: E501
        """
        pass

    def test_settle_cash_from_cashier(self):
        """Test case for settle_cash_from_cashier

        Settle Cash From Cashier  # noqa: E501
        """
        pass

    def test_update_cashier(self):
        """Test case for update_cashier

        Update Cashier  # noqa: E501
        """
        pass

    def test_update_teller(self):
        """Test case for update_teller

        Update teller  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
