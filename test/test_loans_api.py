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
from fineract_client.apis.loans_api import LoansApi  # noqa: E501
from fineract_client.rest import ApiException


class TestLoansApi(unittest.TestCase):
    """LoansApi unit test stubs"""

    def setUp(self):
        self.api = LoansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_calculate_loan_schedule_or_submit_loan_application(self):
        """Test case for calculate_loan_schedule_or_submit_loan_application

        Calculate loan repayment schedule | Submit a new Loan Application  # noqa: E501
        """
        pass

    def test_create_loan_delinquency_action(self):
        """Test case for create_loan_delinquency_action

        Adds a new delinquency action for a loan  # noqa: E501
        """
        pass

    def test_create_loan_delinquency_action1(self):
        """Test case for create_loan_delinquency_action1

        Adds a new delinquency action for a loan  # noqa: E501
        """
        pass

    def test_delete_loan_application(self):
        """Test case for delete_loan_application

        Delete a Loan Application  # noqa: E501
        """
        pass

    def test_delete_loan_application1(self):
        """Test case for delete_loan_application1

        Delete a Loan Application  # noqa: E501
        """
        pass

    def test_get_delinquency_tag_history(self):
        """Test case for get_delinquency_tag_history

        Retrieve the Loan Delinquency Tag history using the Loan Id  # noqa: E501
        """
        pass

    def test_get_delinquency_tag_history1(self):
        """Test case for get_delinquency_tag_history1

        Retrieve the Loan Delinquency Tag history using the Loan Id  # noqa: E501
        """
        pass

    def test_get_glim_repayment_template(self):
        """Test case for get_glim_repayment_template

        """
        pass

    def test_get_loan_delinquency_actions(self):
        """Test case for get_loan_delinquency_actions

        Retrieve delinquency actions related to the loan  # noqa: E501
        """
        pass

    def test_get_loan_delinquency_actions1(self):
        """Test case for get_loan_delinquency_actions1

        Retrieve delinquency actions related to the loan  # noqa: E501
        """
        pass

    def test_get_loan_repayment_template(self):
        """Test case for get_loan_repayment_template

        """
        pass

    def test_get_loans_template(self):
        """Test case for get_loans_template

        """
        pass

    def test_glim_state_transitions(self):
        """Test case for glim_state_transitions

        Approve GLIM Application | Undo GLIM Application Approval | Reject GLIM Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal  # noqa: E501
        """
        pass

    def test_modify_loan_application(self):
        """Test case for modify_loan_application

        Modify a loan application  # noqa: E501
        """
        pass

    def test_modify_loan_application1(self):
        """Test case for modify_loan_application1

        Modify a loan application  # noqa: E501
        """
        pass

    def test_post_loan_repayment_template(self):
        """Test case for post_loan_repayment_template

        """
        pass

    def test_post_loan_template(self):
        """Test case for post_loan_template

        """
        pass

    def test_retrieve_all27(self):
        """Test case for retrieve_all27

        List Loans  # noqa: E501
        """
        pass

    def test_retrieve_approval_template(self):
        """Test case for retrieve_approval_template

        """
        pass

    def test_retrieve_approval_template1(self):
        """Test case for retrieve_approval_template1

        """
        pass

    def test_retrieve_loan(self):
        """Test case for retrieve_loan

        Retrieve a Loan  # noqa: E501
        """
        pass

    def test_retrieve_loan1(self):
        """Test case for retrieve_loan1

        Retrieve a Loan  # noqa: E501
        """
        pass

    def test_state_transitions(self):
        """Test case for state_transitions

        Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal  # noqa: E501
        """
        pass

    def test_state_transitions1(self):
        """Test case for state_transitions1

        Approve Loan Application | Recover Loan Guarantee | Undo Loan Application Approval | Assign a Loan Officer | Unassign a Loan Officer | Reject Loan Application | Applicant Withdraws from Loan Application | Disburse Loan Disburse Loan To Savings Account | Undo Loan Disbursal  # noqa: E501
        """
        pass

    def test_template10(self):
        """Test case for template10

        Retrieve Loan Details Template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
