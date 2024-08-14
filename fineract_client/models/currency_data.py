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

class CurrencyData(object):
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
        'code': 'str',
        'decimal_places': 'int',
        'display_label': 'str',
        'display_symbol': 'str',
        'in_multiples_of': 'int',
        'name': 'str',
        'name_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'decimal_places': 'decimalPlaces',
        'display_label': 'displayLabel',
        'display_symbol': 'displaySymbol',
        'in_multiples_of': 'inMultiplesOf',
        'name': 'name',
        'name_code': 'nameCode'
    }

    def __init__(self, code=None, decimal_places=None, display_label=None, display_symbol=None, in_multiples_of=None, name=None, name_code=None):  # noqa: E501
        """CurrencyData - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._decimal_places = None
        self._display_label = None
        self._display_symbol = None
        self._in_multiples_of = None
        self._name = None
        self._name_code = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if display_label is not None:
            self.display_label = display_label
        if display_symbol is not None:
            self.display_symbol = display_symbol
        if in_multiples_of is not None:
            self.in_multiples_of = in_multiples_of
        if name is not None:
            self.name = name
        if name_code is not None:
            self.name_code = name_code

    @property
    def code(self):
        """Gets the code of this CurrencyData.  # noqa: E501


        :return: The code of this CurrencyData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CurrencyData.


        :param code: The code of this CurrencyData.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def decimal_places(self):
        """Gets the decimal_places of this CurrencyData.  # noqa: E501


        :return: The decimal_places of this CurrencyData.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this CurrencyData.


        :param decimal_places: The decimal_places of this CurrencyData.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

    @property
    def display_label(self):
        """Gets the display_label of this CurrencyData.  # noqa: E501


        :return: The display_label of this CurrencyData.  # noqa: E501
        :rtype: str
        """
        return self._display_label

    @display_label.setter
    def display_label(self, display_label):
        """Sets the display_label of this CurrencyData.


        :param display_label: The display_label of this CurrencyData.  # noqa: E501
        :type: str
        """

        self._display_label = display_label

    @property
    def display_symbol(self):
        """Gets the display_symbol of this CurrencyData.  # noqa: E501


        :return: The display_symbol of this CurrencyData.  # noqa: E501
        :rtype: str
        """
        return self._display_symbol

    @display_symbol.setter
    def display_symbol(self, display_symbol):
        """Sets the display_symbol of this CurrencyData.


        :param display_symbol: The display_symbol of this CurrencyData.  # noqa: E501
        :type: str
        """

        self._display_symbol = display_symbol

    @property
    def in_multiples_of(self):
        """Gets the in_multiples_of of this CurrencyData.  # noqa: E501


        :return: The in_multiples_of of this CurrencyData.  # noqa: E501
        :rtype: int
        """
        return self._in_multiples_of

    @in_multiples_of.setter
    def in_multiples_of(self, in_multiples_of):
        """Sets the in_multiples_of of this CurrencyData.


        :param in_multiples_of: The in_multiples_of of this CurrencyData.  # noqa: E501
        :type: int
        """

        self._in_multiples_of = in_multiples_of

    @property
    def name(self):
        """Gets the name of this CurrencyData.  # noqa: E501


        :return: The name of this CurrencyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrencyData.


        :param name: The name of this CurrencyData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_code(self):
        """Gets the name_code of this CurrencyData.  # noqa: E501


        :return: The name_code of this CurrencyData.  # noqa: E501
        :rtype: str
        """
        return self._name_code

    @name_code.setter
    def name_code(self, name_code):
        """Sets the name_code of this CurrencyData.


        :param name_code: The name_code of this CurrencyData.  # noqa: E501
        :type: str
        """

        self._name_code = name_code

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
        if issubclass(CurrencyData, dict):
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
        if not isinstance(other, CurrencyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
