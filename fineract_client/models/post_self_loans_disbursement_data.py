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

class PostSelfLoansDisbursementData(object):
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
        'approved_principal': 'int',
        'expected_disbursement_date': 'str',
        'principal': 'int'
    }

    attribute_map = {
        'approved_principal': 'approvedPrincipal',
        'expected_disbursement_date': 'expectedDisbursementDate',
        'principal': 'principal'
    }

    def __init__(self, approved_principal=None, expected_disbursement_date=None, principal=None):  # noqa: E501
        """PostSelfLoansDisbursementData - a model defined in Swagger"""  # noqa: E501
        self._approved_principal = None
        self._expected_disbursement_date = None
        self._principal = None
        self.discriminator = None
        if approved_principal is not None:
            self.approved_principal = approved_principal
        if expected_disbursement_date is not None:
            self.expected_disbursement_date = expected_disbursement_date
        if principal is not None:
            self.principal = principal

    @property
    def approved_principal(self):
        """Gets the approved_principal of this PostSelfLoansDisbursementData.  # noqa: E501


        :return: The approved_principal of this PostSelfLoansDisbursementData.  # noqa: E501
        :rtype: int
        """
        return self._approved_principal

    @approved_principal.setter
    def approved_principal(self, approved_principal):
        """Sets the approved_principal of this PostSelfLoansDisbursementData.


        :param approved_principal: The approved_principal of this PostSelfLoansDisbursementData.  # noqa: E501
        :type: int
        """

        self._approved_principal = approved_principal

    @property
    def expected_disbursement_date(self):
        """Gets the expected_disbursement_date of this PostSelfLoansDisbursementData.  # noqa: E501


        :return: The expected_disbursement_date of this PostSelfLoansDisbursementData.  # noqa: E501
        :rtype: str
        """
        return self._expected_disbursement_date

    @expected_disbursement_date.setter
    def expected_disbursement_date(self, expected_disbursement_date):
        """Sets the expected_disbursement_date of this PostSelfLoansDisbursementData.


        :param expected_disbursement_date: The expected_disbursement_date of this PostSelfLoansDisbursementData.  # noqa: E501
        :type: str
        """

        self._expected_disbursement_date = expected_disbursement_date

    @property
    def principal(self):
        """Gets the principal of this PostSelfLoansDisbursementData.  # noqa: E501


        :return: The principal of this PostSelfLoansDisbursementData.  # noqa: E501
        :rtype: int
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this PostSelfLoansDisbursementData.


        :param principal: The principal of this PostSelfLoansDisbursementData.  # noqa: E501
        :type: int
        """

        self._principal = principal

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
        if issubclass(PostSelfLoansDisbursementData, dict):
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
        if not isinstance(other, PostSelfLoansDisbursementData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
