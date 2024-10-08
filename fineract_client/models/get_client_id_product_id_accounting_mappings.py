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

class GetClientIdProductIdAccountingMappings(object):
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
        'share_equity_id': 'GetShareAccountsShareEquityId',
        'income_from_fee_account_id': 'GetShareAccountsIncomeFromFeeAccountId',
        'share_reference_id': 'GetShareAccountsShareReferenceId',
        'share_suspense_id': 'GetShareAccountsShareSuspenseId'
    }

    attribute_map = {
        'share_equity_id': 'ShareEquityId',
        'income_from_fee_account_id': 'incomeFromFeeAccountId',
        'share_reference_id': 'shareReferenceId',
        'share_suspense_id': 'shareSuspenseId'
    }

    def __init__(self, share_equity_id=None, income_from_fee_account_id=None, share_reference_id=None, share_suspense_id=None):  # noqa: E501
        """GetClientIdProductIdAccountingMappings - a model defined in Swagger"""  # noqa: E501
        self._share_equity_id = None
        self._income_from_fee_account_id = None
        self._share_reference_id = None
        self._share_suspense_id = None
        self.discriminator = None
        if share_equity_id is not None:
            self.share_equity_id = share_equity_id
        if income_from_fee_account_id is not None:
            self.income_from_fee_account_id = income_from_fee_account_id
        if share_reference_id is not None:
            self.share_reference_id = share_reference_id
        if share_suspense_id is not None:
            self.share_suspense_id = share_suspense_id

    @property
    def share_equity_id(self):
        """Gets the share_equity_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501


        :return: The share_equity_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :rtype: GetShareAccountsShareEquityId
        """
        return self._share_equity_id

    @share_equity_id.setter
    def share_equity_id(self, share_equity_id):
        """Sets the share_equity_id of this GetClientIdProductIdAccountingMappings.


        :param share_equity_id: The share_equity_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :type: GetShareAccountsShareEquityId
        """

        self._share_equity_id = share_equity_id

    @property
    def income_from_fee_account_id(self):
        """Gets the income_from_fee_account_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501


        :return: The income_from_fee_account_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :rtype: GetShareAccountsIncomeFromFeeAccountId
        """
        return self._income_from_fee_account_id

    @income_from_fee_account_id.setter
    def income_from_fee_account_id(self, income_from_fee_account_id):
        """Sets the income_from_fee_account_id of this GetClientIdProductIdAccountingMappings.


        :param income_from_fee_account_id: The income_from_fee_account_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :type: GetShareAccountsIncomeFromFeeAccountId
        """

        self._income_from_fee_account_id = income_from_fee_account_id

    @property
    def share_reference_id(self):
        """Gets the share_reference_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501


        :return: The share_reference_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :rtype: GetShareAccountsShareReferenceId
        """
        return self._share_reference_id

    @share_reference_id.setter
    def share_reference_id(self, share_reference_id):
        """Sets the share_reference_id of this GetClientIdProductIdAccountingMappings.


        :param share_reference_id: The share_reference_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :type: GetShareAccountsShareReferenceId
        """

        self._share_reference_id = share_reference_id

    @property
    def share_suspense_id(self):
        """Gets the share_suspense_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501


        :return: The share_suspense_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :rtype: GetShareAccountsShareSuspenseId
        """
        return self._share_suspense_id

    @share_suspense_id.setter
    def share_suspense_id(self, share_suspense_id):
        """Sets the share_suspense_id of this GetClientIdProductIdAccountingMappings.


        :param share_suspense_id: The share_suspense_id of this GetClientIdProductIdAccountingMappings.  # noqa: E501
        :type: GetShareAccountsShareSuspenseId
        """

        self._share_suspense_id = share_suspense_id

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
        if issubclass(GetClientIdProductIdAccountingMappings, dict):
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
        if not isinstance(other, GetClientIdProductIdAccountingMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
