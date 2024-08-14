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

class ClientCollateralManagementData(object):
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
        'id': 'int',
        'name': 'str',
        'pct_to_base': 'float',
        'quantity': 'float',
        'total': 'float',
        'total_collateral': 'float',
        'unit_price': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pct_to_base': 'pctToBase',
        'quantity': 'quantity',
        'total': 'total',
        'total_collateral': 'totalCollateral',
        'unit_price': 'unitPrice'
    }

    def __init__(self, id=None, name=None, pct_to_base=None, quantity=None, total=None, total_collateral=None, unit_price=None):  # noqa: E501
        """ClientCollateralManagementData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._pct_to_base = None
        self._quantity = None
        self._total = None
        self._total_collateral = None
        self._unit_price = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if pct_to_base is not None:
            self.pct_to_base = pct_to_base
        if quantity is not None:
            self.quantity = quantity
        if total is not None:
            self.total = total
        if total_collateral is not None:
            self.total_collateral = total_collateral
        if unit_price is not None:
            self.unit_price = unit_price

    @property
    def id(self):
        """Gets the id of this ClientCollateralManagementData.  # noqa: E501


        :return: The id of this ClientCollateralManagementData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientCollateralManagementData.


        :param id: The id of this ClientCollateralManagementData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClientCollateralManagementData.  # noqa: E501


        :return: The name of this ClientCollateralManagementData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientCollateralManagementData.


        :param name: The name of this ClientCollateralManagementData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pct_to_base(self):
        """Gets the pct_to_base of this ClientCollateralManagementData.  # noqa: E501


        :return: The pct_to_base of this ClientCollateralManagementData.  # noqa: E501
        :rtype: float
        """
        return self._pct_to_base

    @pct_to_base.setter
    def pct_to_base(self, pct_to_base):
        """Sets the pct_to_base of this ClientCollateralManagementData.


        :param pct_to_base: The pct_to_base of this ClientCollateralManagementData.  # noqa: E501
        :type: float
        """

        self._pct_to_base = pct_to_base

    @property
    def quantity(self):
        """Gets the quantity of this ClientCollateralManagementData.  # noqa: E501


        :return: The quantity of this ClientCollateralManagementData.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ClientCollateralManagementData.


        :param quantity: The quantity of this ClientCollateralManagementData.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def total(self):
        """Gets the total of this ClientCollateralManagementData.  # noqa: E501


        :return: The total of this ClientCollateralManagementData.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ClientCollateralManagementData.


        :param total: The total of this ClientCollateralManagementData.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_collateral(self):
        """Gets the total_collateral of this ClientCollateralManagementData.  # noqa: E501


        :return: The total_collateral of this ClientCollateralManagementData.  # noqa: E501
        :rtype: float
        """
        return self._total_collateral

    @total_collateral.setter
    def total_collateral(self, total_collateral):
        """Sets the total_collateral of this ClientCollateralManagementData.


        :param total_collateral: The total_collateral of this ClientCollateralManagementData.  # noqa: E501
        :type: float
        """

        self._total_collateral = total_collateral

    @property
    def unit_price(self):
        """Gets the unit_price of this ClientCollateralManagementData.  # noqa: E501


        :return: The unit_price of this ClientCollateralManagementData.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ClientCollateralManagementData.


        :param unit_price: The unit_price of this ClientCollateralManagementData.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

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
        if issubclass(ClientCollateralManagementData, dict):
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
        if not isinstance(other, ClientCollateralManagementData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
