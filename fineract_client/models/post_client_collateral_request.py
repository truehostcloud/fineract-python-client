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

class PostClientCollateralRequest(object):
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
        'collateral_id': 'int',
        'locale': 'str',
        'quantity': 'float'
    }

    attribute_map = {
        'collateral_id': 'collateralId',
        'locale': 'locale',
        'quantity': 'quantity'
    }

    def __init__(self, collateral_id=None, locale=None, quantity=None):  # noqa: E501
        """PostClientCollateralRequest - a model defined in Swagger"""  # noqa: E501
        self._collateral_id = None
        self._locale = None
        self._quantity = None
        self.discriminator = None
        if collateral_id is not None:
            self.collateral_id = collateral_id
        if locale is not None:
            self.locale = locale
        if quantity is not None:
            self.quantity = quantity

    @property
    def collateral_id(self):
        """Gets the collateral_id of this PostClientCollateralRequest.  # noqa: E501


        :return: The collateral_id of this PostClientCollateralRequest.  # noqa: E501
        :rtype: int
        """
        return self._collateral_id

    @collateral_id.setter
    def collateral_id(self, collateral_id):
        """Sets the collateral_id of this PostClientCollateralRequest.


        :param collateral_id: The collateral_id of this PostClientCollateralRequest.  # noqa: E501
        :type: int
        """

        self._collateral_id = collateral_id

    @property
    def locale(self):
        """Gets the locale of this PostClientCollateralRequest.  # noqa: E501


        :return: The locale of this PostClientCollateralRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostClientCollateralRequest.


        :param locale: The locale of this PostClientCollateralRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def quantity(self):
        """Gets the quantity of this PostClientCollateralRequest.  # noqa: E501


        :return: The quantity of this PostClientCollateralRequest.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PostClientCollateralRequest.


        :param quantity: The quantity of this PostClientCollateralRequest.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

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
        if issubclass(PostClientCollateralRequest, dict):
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
        if not isinstance(other, PostClientCollateralRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
