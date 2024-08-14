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

class PostTellersTellerIdCashiersCashierIdAllocateRequest(object):
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
        'currency_code': 'str',
        'date_format': 'str',
        'locale': 'str',
        'txn_amount': 'float',
        'txn_date': 'date',
        'txn_note': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'date_format': 'dateFormat',
        'locale': 'locale',
        'txn_amount': 'txnAmount',
        'txn_date': 'txnDate',
        'txn_note': 'txnNote'
    }

    def __init__(self, currency_code=None, date_format=None, locale=None, txn_amount=None, txn_date=None, txn_note=None):  # noqa: E501
        """PostTellersTellerIdCashiersCashierIdAllocateRequest - a model defined in Swagger"""  # noqa: E501
        self._currency_code = None
        self._date_format = None
        self._locale = None
        self._txn_amount = None
        self._txn_date = None
        self._txn_note = None
        self.discriminator = None
        if currency_code is not None:
            self.currency_code = currency_code
        if date_format is not None:
            self.date_format = date_format
        if locale is not None:
            self.locale = locale
        if txn_amount is not None:
            self.txn_amount = txn_amount
        if txn_date is not None:
            self.txn_date = txn_date
        if txn_note is not None:
            self.txn_note = txn_note

    @property
    def currency_code(self):
        """Gets the currency_code of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The currency_code of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param currency_code: The currency_code of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def date_format(self):
        """Gets the date_format of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The date_format of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param date_format: The date_format of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def locale(self):
        """Gets the locale of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The locale of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param locale: The locale of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def txn_amount(self):
        """Gets the txn_amount of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The txn_amount of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: float
        """
        return self._txn_amount

    @txn_amount.setter
    def txn_amount(self, txn_amount):
        """Sets the txn_amount of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param txn_amount: The txn_amount of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: float
        """

        self._txn_amount = txn_amount

    @property
    def txn_date(self):
        """Gets the txn_date of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The txn_date of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: date
        """
        return self._txn_date

    @txn_date.setter
    def txn_date(self, txn_date):
        """Sets the txn_date of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param txn_date: The txn_date of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: date
        """

        self._txn_date = txn_date

    @property
    def txn_note(self):
        """Gets the txn_note of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501


        :return: The txn_note of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :rtype: str
        """
        return self._txn_note

    @txn_note.setter
    def txn_note(self, txn_note):
        """Sets the txn_note of this PostTellersTellerIdCashiersCashierIdAllocateRequest.


        :param txn_note: The txn_note of this PostTellersTellerIdCashiersCashierIdAllocateRequest.  # noqa: E501
        :type: str
        """

        self._txn_note = txn_note

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
        if issubclass(PostTellersTellerIdCashiersCashierIdAllocateRequest, dict):
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
        if not isinstance(other, PostTellersTellerIdCashiersCashierIdAllocateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
