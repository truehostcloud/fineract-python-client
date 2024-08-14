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

class PutTaxesComponentsTaxComponentIdRequest(object):
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
        'locale': 'str',
        'name': 'str',
        'percentage': 'float',
        'start_date': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'locale': 'locale',
        'name': 'name',
        'percentage': 'percentage',
        'start_date': 'startDate'
    }

    def __init__(self, date_format=None, locale=None, name=None, percentage=None, start_date=None):  # noqa: E501
        """PutTaxesComponentsTaxComponentIdRequest - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._locale = None
        self._name = None
        self._percentage = None
        self._start_date = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if start_date is not None:
            self.start_date = start_date

    @property
    def date_format(self):
        """Gets the date_format of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501


        :return: The date_format of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PutTaxesComponentsTaxComponentIdRequest.


        :param date_format: The date_format of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def locale(self):
        """Gets the locale of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501


        :return: The locale of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutTaxesComponentsTaxComponentIdRequest.


        :param locale: The locale of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501


        :return: The name of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutTaxesComponentsTaxComponentIdRequest.


        :param name: The name of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501


        :return: The percentage of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this PutTaxesComponentsTaxComponentIdRequest.


        :param percentage: The percentage of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def start_date(self):
        """Gets the start_date of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501


        :return: The start_date of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PutTaxesComponentsTaxComponentIdRequest.


        :param start_date: The start_date of this PutTaxesComponentsTaxComponentIdRequest.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(PutTaxesComponentsTaxComponentIdRequest, dict):
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
        if not isinstance(other, PutTaxesComponentsTaxComponentIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
