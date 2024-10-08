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
from fineract_client.apis.guarantors_api import GuarantorsApi  # noqa: E501
from fineract_client.rest import ApiException


class TestGuarantorsApi(unittest.TestCase):
    """GuarantorsApi unit test stubs"""

    def setUp(self):
        self.api = GuarantorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_template(self):
        """Test case for accounts_template

        """
        pass

    def test_create_guarantor(self):
        """Test case for create_guarantor

        """
        pass

    def test_delete_guarantor(self):
        """Test case for delete_guarantor

        """
        pass

    def test_get_guarantor_template(self):
        """Test case for get_guarantor_template

        """
        pass

    def test_new_guarantor_template(self):
        """Test case for new_guarantor_template

        """
        pass

    def test_post_guarantor_template(self):
        """Test case for post_guarantor_template

        """
        pass

    def test_retrieve_guarantor_details(self):
        """Test case for retrieve_guarantor_details

        """
        pass

    def test_retrieve_guarantor_details1(self):
        """Test case for retrieve_guarantor_details1

        """
        pass

    def test_update_guarantor(self):
        """Test case for update_guarantor

        """
        pass


if __name__ == '__main__':
    unittest.main()
