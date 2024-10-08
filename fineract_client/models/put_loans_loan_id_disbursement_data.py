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

class PutLoansLoanIdDisbursementData(object):
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
        'date_format': 'str',
        'expected_disbursement_date': 'str',
        'interest_type': 'int',
        'is_equal_amortization': 'bool',
        'locale': 'str',
        'net_disbursal_amount': 'float',
        'principal': 'float'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'expected_disbursement_date': 'expectedDisbursementDate',
        'interest_type': 'interestType',
        'is_equal_amortization': 'isEqualAmortization',
        'locale': 'locale',
        'net_disbursal_amount': 'netDisbursalAmount',
        'principal': 'principal'
    }

    def __init__(self, date_format=None, expected_disbursement_date=None, interest_type=None, is_equal_amortization=None, locale=None, net_disbursal_amount=None, principal=None):  # noqa: E501
        """PutLoansLoanIdDisbursementData - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._expected_disbursement_date = None
        self._interest_type = None
        self._is_equal_amortization = None
        self._locale = None
        self._net_disbursal_amount = None
        self._principal = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if expected_disbursement_date is not None:
            self.expected_disbursement_date = expected_disbursement_date
        if interest_type is not None:
            self.interest_type = interest_type
        if is_equal_amortization is not None:
            self.is_equal_amortization = is_equal_amortization
        if locale is not None:
            self.locale = locale
        if net_disbursal_amount is not None:
            self.net_disbursal_amount = net_disbursal_amount
        if principal is not None:
            self.principal = principal

    @property
    def date_format(self):
        """Gets the date_format of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The date_format of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PutLoansLoanIdDisbursementData.


        :param date_format: The date_format of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def expected_disbursement_date(self):
        """Gets the expected_disbursement_date of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The expected_disbursement_date of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: str
        """
        return self._expected_disbursement_date

    @expected_disbursement_date.setter
    def expected_disbursement_date(self, expected_disbursement_date):
        """Sets the expected_disbursement_date of this PutLoansLoanIdDisbursementData.


        :param expected_disbursement_date: The expected_disbursement_date of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: str
        """

        self._expected_disbursement_date = expected_disbursement_date

    @property
    def interest_type(self):
        """Gets the interest_type of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The interest_type of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: int
        """
        return self._interest_type

    @interest_type.setter
    def interest_type(self, interest_type):
        """Sets the interest_type of this PutLoansLoanIdDisbursementData.


        :param interest_type: The interest_type of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: int
        """

        self._interest_type = interest_type

    @property
    def is_equal_amortization(self):
        """Gets the is_equal_amortization of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The is_equal_amortization of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: bool
        """
        return self._is_equal_amortization

    @is_equal_amortization.setter
    def is_equal_amortization(self, is_equal_amortization):
        """Sets the is_equal_amortization of this PutLoansLoanIdDisbursementData.


        :param is_equal_amortization: The is_equal_amortization of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: bool
        """

        self._is_equal_amortization = is_equal_amortization

    @property
    def locale(self):
        """Gets the locale of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The locale of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutLoansLoanIdDisbursementData.


        :param locale: The locale of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def net_disbursal_amount(self):
        """Gets the net_disbursal_amount of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The net_disbursal_amount of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: float
        """
        return self._net_disbursal_amount

    @net_disbursal_amount.setter
    def net_disbursal_amount(self, net_disbursal_amount):
        """Sets the net_disbursal_amount of this PutLoansLoanIdDisbursementData.


        :param net_disbursal_amount: The net_disbursal_amount of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: float
        """

        self._net_disbursal_amount = net_disbursal_amount

    @property
    def principal(self):
        """Gets the principal of this PutLoansLoanIdDisbursementData.  # noqa: E501


        :return: The principal of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :rtype: float
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this PutLoansLoanIdDisbursementData.


        :param principal: The principal of this PutLoansLoanIdDisbursementData.  # noqa: E501
        :type: float
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
        if issubclass(PutLoansLoanIdDisbursementData, dict):
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
        if not isinstance(other, PutLoansLoanIdDisbursementData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
