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
from fineract_client.apis.reschedule_loans_api import RescheduleLoansApi  # noqa: E501
from fineract_client.rest import ApiException


class TestRescheduleLoansApi(unittest.TestCase):
    """RescheduleLoansApi unit test stubs"""

    def setUp(self):
        self.api = RescheduleLoansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_loan_reschedule_request(self):
        """Test case for create_loan_reschedule_request

        Create loan reschedule request  # noqa: E501
        """
        pass

    def test_read_loan_reschedule_request(self):
        """Test case for read_loan_reschedule_request

        Retrieve loan reschedule request by schedule id  # noqa: E501
        """
        pass

    def test_retrieve_all_reschedule_request(self):
        """Test case for retrieve_all_reschedule_request

        Retrieve all reschedule requests  # noqa: E501
        """
        pass

    def test_retrieve_template10(self):
        """Test case for retrieve_template10

        Retrieve all reschedule loan reasons  # noqa: E501
        """
        pass

    def test_update_loan_reschedule_request(self):
        """Test case for update_loan_reschedule_request

        Update loan reschedule request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
