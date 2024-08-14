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

class PutFloatingRatesFloatingRateIdRequest(object):
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
        'is_active': 'bool',
        'is_base_lending_rate': 'bool',
        'name': 'str',
        'rate_periods': 'list[PostFloatingRatesRatePeriods]'
    }

    attribute_map = {
        'is_active': 'isActive',
        'is_base_lending_rate': 'isBaseLendingRate',
        'name': 'name',
        'rate_periods': 'ratePeriods'
    }

    def __init__(self, is_active=None, is_base_lending_rate=None, name=None, rate_periods=None):  # noqa: E501
        """PutFloatingRatesFloatingRateIdRequest - a model defined in Swagger"""  # noqa: E501
        self._is_active = None
        self._is_base_lending_rate = None
        self._name = None
        self._rate_periods = None
        self.discriminator = None
        if is_active is not None:
            self.is_active = is_active
        if is_base_lending_rate is not None:
            self.is_base_lending_rate = is_base_lending_rate
        if name is not None:
            self.name = name
        if rate_periods is not None:
            self.rate_periods = rate_periods

    @property
    def is_active(self):
        """Gets the is_active of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501


        :return: The is_active of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this PutFloatingRatesFloatingRateIdRequest.


        :param is_active: The is_active of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_base_lending_rate(self):
        """Gets the is_base_lending_rate of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501


        :return: The is_base_lending_rate of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_base_lending_rate

    @is_base_lending_rate.setter
    def is_base_lending_rate(self, is_base_lending_rate):
        """Sets the is_base_lending_rate of this PutFloatingRatesFloatingRateIdRequest.


        :param is_base_lending_rate: The is_base_lending_rate of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :type: bool
        """

        self._is_base_lending_rate = is_base_lending_rate

    @property
    def name(self):
        """Gets the name of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501


        :return: The name of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutFloatingRatesFloatingRateIdRequest.


        :param name: The name of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate_periods(self):
        """Gets the rate_periods of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501


        :return: The rate_periods of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :rtype: list[PostFloatingRatesRatePeriods]
        """
        return self._rate_periods

    @rate_periods.setter
    def rate_periods(self, rate_periods):
        """Sets the rate_periods of this PutFloatingRatesFloatingRateIdRequest.


        :param rate_periods: The rate_periods of this PutFloatingRatesFloatingRateIdRequest.  # noqa: E501
        :type: list[PostFloatingRatesRatePeriods]
        """

        self._rate_periods = rate_periods

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
        if issubclass(PutFloatingRatesFloatingRateIdRequest, dict):
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
        if not isinstance(other, PutFloatingRatesFloatingRateIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
