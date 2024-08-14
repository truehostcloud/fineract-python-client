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

class UpdatePostDatedCheckRequest(object):
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
        'account_no': 'int',
        'amount': 'float',
        '_date': 'date',
        'date_format': 'str',
        'locale': 'str',
        'name': 'str',
        'repayment_date': 'date'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'amount': 'amount',
        '_date': 'date',
        'date_format': 'dateFormat',
        'locale': 'locale',
        'name': 'name',
        'repayment_date': 'repaymentDate'
    }

    def __init__(self, account_no=None, amount=None, _date=None, date_format=None, locale=None, name=None, repayment_date=None):  # noqa: E501
        """UpdatePostDatedCheckRequest - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._amount = None
        self.__date = None
        self._date_format = None
        self._locale = None
        self._name = None
        self._repayment_date = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if amount is not None:
            self.amount = amount
        if _date is not None:
            self._date = _date
        if date_format is not None:
            self.date_format = date_format
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if repayment_date is not None:
            self.repayment_date = repayment_date

    @property
    def account_no(self):
        """Gets the account_no of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The account_no of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: int
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this UpdatePostDatedCheckRequest.


        :param account_no: The account_no of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: int
        """

        self._account_no = account_no

    @property
    def amount(self):
        """Gets the amount of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The amount of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UpdatePostDatedCheckRequest.


        :param amount: The amount of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def _date(self):
        """Gets the _date of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The _date of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this UpdatePostDatedCheckRequest.


        :param _date: The _date of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def date_format(self):
        """Gets the date_format of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The date_format of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this UpdatePostDatedCheckRequest.


        :param date_format: The date_format of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def locale(self):
        """Gets the locale of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The locale of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UpdatePostDatedCheckRequest.


        :param locale: The locale of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The name of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePostDatedCheckRequest.


        :param name: The name of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def repayment_date(self):
        """Gets the repayment_date of this UpdatePostDatedCheckRequest.  # noqa: E501


        :return: The repayment_date of this UpdatePostDatedCheckRequest.  # noqa: E501
        :rtype: date
        """
        return self._repayment_date

    @repayment_date.setter
    def repayment_date(self, repayment_date):
        """Sets the repayment_date of this UpdatePostDatedCheckRequest.


        :param repayment_date: The repayment_date of this UpdatePostDatedCheckRequest.  # noqa: E501
        :type: date
        """

        self._repayment_date = repayment_date

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
        if issubclass(UpdatePostDatedCheckRequest, dict):
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
        if not isinstance(other, UpdatePostDatedCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
