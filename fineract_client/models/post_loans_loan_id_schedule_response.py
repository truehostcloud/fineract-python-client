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

class PostLoansLoanIdScheduleResponse(object):
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
        'changes': 'PostLoanChanges',
        'loan_id': 'int'
    }

    attribute_map = {
        'changes': 'changes',
        'loan_id': 'loanId'
    }

    def __init__(self, changes=None, loan_id=None):  # noqa: E501
        """PostLoansLoanIdScheduleResponse - a model defined in Swagger"""  # noqa: E501
        self._changes = None
        self._loan_id = None
        self.discriminator = None
        if changes is not None:
            self.changes = changes
        if loan_id is not None:
            self.loan_id = loan_id

    @property
    def changes(self):
        """Gets the changes of this PostLoansLoanIdScheduleResponse.  # noqa: E501


        :return: The changes of this PostLoansLoanIdScheduleResponse.  # noqa: E501
        :rtype: PostLoanChanges
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this PostLoansLoanIdScheduleResponse.


        :param changes: The changes of this PostLoansLoanIdScheduleResponse.  # noqa: E501
        :type: PostLoanChanges
        """

        self._changes = changes

    @property
    def loan_id(self):
        """Gets the loan_id of this PostLoansLoanIdScheduleResponse.  # noqa: E501


        :return: The loan_id of this PostLoansLoanIdScheduleResponse.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this PostLoansLoanIdScheduleResponse.


        :param loan_id: The loan_id of this PostLoansLoanIdScheduleResponse.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

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
        if issubclass(PostLoansLoanIdScheduleResponse, dict):
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
        if not isinstance(other, PostLoansLoanIdScheduleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
