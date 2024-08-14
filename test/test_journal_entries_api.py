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
from fineract_client.apis.journal_entries_api import JournalEntriesApi  # noqa: E501
from fineract_client.rest import ApiException


class TestJournalEntriesApi(unittest.TestCase):
    """JournalEntriesApi unit test stubs"""

    def setUp(self):
        self.api = JournalEntriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_gl_journal_entry(self):
        """Test case for create_gl_journal_entry

        Create \"Balanced\" Journal Entries  # noqa: E501
        """
        pass

    def test_create_reversal_journal_entry(self):
        """Test case for create_reversal_journal_entry

        Update Running balances for Journal Entries  # noqa: E501
        """
        pass

    def test_get_journal_entries_template(self):
        """Test case for get_journal_entries_template

        """
        pass

    def test_post_journal_entries_template(self):
        """Test case for post_journal_entries_template

        """
        pass

    def test_retrieve_all1(self):
        """Test case for retrieve_all1

        List Journal Entries  # noqa: E501
        """
        pass

    def test_retrieve_journal_entries(self):
        """Test case for retrieve_journal_entries

        """
        pass

    def test_retrieve_journal_entry_by_id(self):
        """Test case for retrieve_journal_entry_by_id

        Retrieve a single Entry  # noqa: E501
        """
        pass

    def test_retrieve_opening_balance(self):
        """Test case for retrieve_opening_balance

        """
        pass


if __name__ == '__main__':
    unittest.main()
