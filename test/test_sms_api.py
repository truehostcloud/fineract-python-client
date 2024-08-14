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
from fineract_client.apis.sms_api import SMSApi  # noqa: E501
from fineract_client.rest import ApiException


class TestSMSApi(unittest.TestCase):
    """SMSApi unit test stubs"""

    def setUp(self):
        self.api = SMSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create2(self):
        """Test case for create2

        """
        pass

    def test_delete6(self):
        """Test case for delete6

        """
        pass

    def test_retrieve_all10(self):
        """Test case for retrieve_all10

        """
        pass

    def test_retrieve_all_sms_by_status(self):
        """Test case for retrieve_all_sms_by_status

        """
        pass

    def test_retrieve_one6(self):
        """Test case for retrieve_one6

        """
        pass

    def test_update3(self):
        """Test case for update3

        """
        pass


if __name__ == '__main__':
    unittest.main()
