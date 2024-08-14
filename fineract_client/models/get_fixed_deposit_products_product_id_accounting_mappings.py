# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetFixedDepositProductsProductIdAccountingMappings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fee_receivable_account': 'GetFixedDepositProductsGlAccount',
        'income_from_fee_account': 'GetFixedDepositProductsGlAccount',
        'income_from_penalty_account': 'GetFixedDepositProductsGlAccount',
        'interest_on_savings_account': 'GetFixedDepositProductsGlAccount',
        'interest_payable_account': 'GetFixedDepositProductsGlAccount',
        'penalty_receivable_account': 'GetFixedDepositProductsGlAccount',
        'savings_control_account': 'GetFixedDepositProductsGlAccount',
        'savings_reference_account': 'GetFixedDepositProductsGlAccount',
        'transfers_in_suspense_account': 'GetFixedDepositProductsGlAccount'
    }

    attribute_map = {
        'fee_receivable_account': 'feeReceivableAccount',
        'income_from_fee_account': 'incomeFromFeeAccount',
        'income_from_penalty_account': 'incomeFromPenaltyAccount',
        'interest_on_savings_account': 'interestOnSavingsAccount',
        'interest_payable_account': 'interestPayableAccount',
        'penalty_receivable_account': 'penaltyReceivableAccount',
        'savings_control_account': 'savingsControlAccount',
        'savings_reference_account': 'savingsReferenceAccount',
        'transfers_in_suspense_account': 'transfersInSuspenseAccount'
    }

    def __init__(self, fee_receivable_account=None, income_from_fee_account=None, income_from_penalty_account=None, interest_on_savings_account=None, interest_payable_account=None, penalty_receivable_account=None, savings_control_account=None, savings_reference_account=None, transfers_in_suspense_account=None):  # noqa: E501
        """GetFixedDepositProductsProductIdAccountingMappings - a model defined in Swagger"""  # noqa: E501
        self._fee_receivable_account = None
        self._income_from_fee_account = None
        self._income_from_penalty_account = None
        self._interest_on_savings_account = None
        self._interest_payable_account = None
        self._penalty_receivable_account = None
        self._savings_control_account = None
        self._savings_reference_account = None
        self._transfers_in_suspense_account = None
        self.discriminator = None
        if fee_receivable_account is not None:
            self.fee_receivable_account = fee_receivable_account
        if income_from_fee_account is not None:
            self.income_from_fee_account = income_from_fee_account
        if income_from_penalty_account is not None:
            self.income_from_penalty_account = income_from_penalty_account
        if interest_on_savings_account is not None:
            self.interest_on_savings_account = interest_on_savings_account
        if interest_payable_account is not None:
            self.interest_payable_account = interest_payable_account
        if penalty_receivable_account is not None:
            self.penalty_receivable_account = penalty_receivable_account
        if savings_control_account is not None:
            self.savings_control_account = savings_control_account
        if savings_reference_account is not None:
            self.savings_reference_account = savings_reference_account
        if transfers_in_suspense_account is not None:
            self.transfers_in_suspense_account = transfers_in_suspense_account

    @property
    def fee_receivable_account(self):
        """Gets the fee_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The fee_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._fee_receivable_account

    @fee_receivable_account.setter
    def fee_receivable_account(self, fee_receivable_account):
        """Sets the fee_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param fee_receivable_account: The fee_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._fee_receivable_account = fee_receivable_account

    @property
    def income_from_fee_account(self):
        """Gets the income_from_fee_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The income_from_fee_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._income_from_fee_account

    @income_from_fee_account.setter
    def income_from_fee_account(self, income_from_fee_account):
        """Sets the income_from_fee_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param income_from_fee_account: The income_from_fee_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._income_from_fee_account = income_from_fee_account

    @property
    def income_from_penalty_account(self):
        """Gets the income_from_penalty_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The income_from_penalty_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._income_from_penalty_account

    @income_from_penalty_account.setter
    def income_from_penalty_account(self, income_from_penalty_account):
        """Sets the income_from_penalty_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param income_from_penalty_account: The income_from_penalty_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._income_from_penalty_account = income_from_penalty_account

    @property
    def interest_on_savings_account(self):
        """Gets the interest_on_savings_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The interest_on_savings_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._interest_on_savings_account

    @interest_on_savings_account.setter
    def interest_on_savings_account(self, interest_on_savings_account):
        """Sets the interest_on_savings_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param interest_on_savings_account: The interest_on_savings_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._interest_on_savings_account = interest_on_savings_account

    @property
    def interest_payable_account(self):
        """Gets the interest_payable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The interest_payable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._interest_payable_account

    @interest_payable_account.setter
    def interest_payable_account(self, interest_payable_account):
        """Sets the interest_payable_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param interest_payable_account: The interest_payable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._interest_payable_account = interest_payable_account

    @property
    def penalty_receivable_account(self):
        """Gets the penalty_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The penalty_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._penalty_receivable_account

    @penalty_receivable_account.setter
    def penalty_receivable_account(self, penalty_receivable_account):
        """Sets the penalty_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param penalty_receivable_account: The penalty_receivable_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._penalty_receivable_account = penalty_receivable_account

    @property
    def savings_control_account(self):
        """Gets the savings_control_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The savings_control_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._savings_control_account

    @savings_control_account.setter
    def savings_control_account(self, savings_control_account):
        """Sets the savings_control_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param savings_control_account: The savings_control_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._savings_control_account = savings_control_account

    @property
    def savings_reference_account(self):
        """Gets the savings_reference_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The savings_reference_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._savings_reference_account

    @savings_reference_account.setter
    def savings_reference_account(self, savings_reference_account):
        """Sets the savings_reference_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param savings_reference_account: The savings_reference_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._savings_reference_account = savings_reference_account

    @property
    def transfers_in_suspense_account(self):
        """Gets the transfers_in_suspense_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501


        :return: The transfers_in_suspense_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :rtype: GetFixedDepositProductsGlAccount
        """
        return self._transfers_in_suspense_account

    @transfers_in_suspense_account.setter
    def transfers_in_suspense_account(self, transfers_in_suspense_account):
        """Sets the transfers_in_suspense_account of this GetFixedDepositProductsProductIdAccountingMappings.


        :param transfers_in_suspense_account: The transfers_in_suspense_account of this GetFixedDepositProductsProductIdAccountingMappings.  # noqa: E501
        :type: GetFixedDepositProductsGlAccount
        """

        self._transfers_in_suspense_account = transfers_in_suspense_account

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetFixedDepositProductsProductIdAccountingMappings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetFixedDepositProductsProductIdAccountingMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
