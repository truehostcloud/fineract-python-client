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

class PutTellersTellerIdCashiersCashierIdResponseChanges(object):
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
        'description': 'str',
        'end_date': 'date',
        'locale': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'description': 'description',
        'end_date': 'endDate',
        'locale': 'locale'
    }

    def __init__(self, date_format=None, description=None, end_date=None, locale=None):  # noqa: E501
        """PutTellersTellerIdCashiersCashierIdResponseChanges - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._description = None
        self._end_date = None
        self._locale = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if locale is not None:
            self.locale = locale

    @property
    def date_format(self):
        """Gets the date_format of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501


        :return: The date_format of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PutTellersTellerIdCashiersCashierIdResponseChanges.


        :param date_format: The date_format of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def description(self):
        """Gets the description of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501


        :return: The description of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutTellersTellerIdCashiersCashierIdResponseChanges.


        :param description: The description of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501


        :return: The end_date of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PutTellersTellerIdCashiersCashierIdResponseChanges.


        :param end_date: The end_date of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def locale(self):
        """Gets the locale of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501


        :return: The locale of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutTellersTellerIdCashiersCashierIdResponseChanges.


        :param locale: The locale of this PutTellersTellerIdCashiersCashierIdResponseChanges.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(PutTellersTellerIdCashiersCashierIdResponseChanges, dict):
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
        if not isinstance(other, PutTellersTellerIdCashiersCashierIdResponseChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
