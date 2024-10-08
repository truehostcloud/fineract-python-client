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

class PutCollateralProductRequest(object):
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
        'base_price': 'float',
        'currency': 'str',
        'name': 'str',
        'pct_to_base': 'float',
        'quality': 'str',
        'unit_type': 'str'
    }

    attribute_map = {
        'base_price': 'basePrice',
        'currency': 'currency',
        'name': 'name',
        'pct_to_base': 'pctToBase',
        'quality': 'quality',
        'unit_type': 'unitType'
    }

    def __init__(self, base_price=None, currency=None, name=None, pct_to_base=None, quality=None, unit_type=None):  # noqa: E501
        """PutCollateralProductRequest - a model defined in Swagger"""  # noqa: E501
        self._base_price = None
        self._currency = None
        self._name = None
        self._pct_to_base = None
        self._quality = None
        self._unit_type = None
        self.discriminator = None
        if base_price is not None:
            self.base_price = base_price
        if currency is not None:
            self.currency = currency
        if name is not None:
            self.name = name
        if pct_to_base is not None:
            self.pct_to_base = pct_to_base
        if quality is not None:
            self.quality = quality
        if unit_type is not None:
            self.unit_type = unit_type

    @property
    def base_price(self):
        """Gets the base_price of this PutCollateralProductRequest.  # noqa: E501


        :return: The base_price of this PutCollateralProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this PutCollateralProductRequest.


        :param base_price: The base_price of this PutCollateralProductRequest.  # noqa: E501
        :type: float
        """

        self._base_price = base_price

    @property
    def currency(self):
        """Gets the currency of this PutCollateralProductRequest.  # noqa: E501


        :return: The currency of this PutCollateralProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PutCollateralProductRequest.


        :param currency: The currency of this PutCollateralProductRequest.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def name(self):
        """Gets the name of this PutCollateralProductRequest.  # noqa: E501


        :return: The name of this PutCollateralProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutCollateralProductRequest.


        :param name: The name of this PutCollateralProductRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pct_to_base(self):
        """Gets the pct_to_base of this PutCollateralProductRequest.  # noqa: E501


        :return: The pct_to_base of this PutCollateralProductRequest.  # noqa: E501
        :rtype: float
        """
        return self._pct_to_base

    @pct_to_base.setter
    def pct_to_base(self, pct_to_base):
        """Sets the pct_to_base of this PutCollateralProductRequest.


        :param pct_to_base: The pct_to_base of this PutCollateralProductRequest.  # noqa: E501
        :type: float
        """

        self._pct_to_base = pct_to_base

    @property
    def quality(self):
        """Gets the quality of this PutCollateralProductRequest.  # noqa: E501


        :return: The quality of this PutCollateralProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this PutCollateralProductRequest.


        :param quality: The quality of this PutCollateralProductRequest.  # noqa: E501
        :type: str
        """

        self._quality = quality

    @property
    def unit_type(self):
        """Gets the unit_type of this PutCollateralProductRequest.  # noqa: E501


        :return: The unit_type of this PutCollateralProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this PutCollateralProductRequest.


        :param unit_type: The unit_type of this PutCollateralProductRequest.  # noqa: E501
        :type: str
        """

        self._unit_type = unit_type

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
        if issubclass(PutCollateralProductRequest, dict):
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
        if not isinstance(other, PutCollateralProductRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
