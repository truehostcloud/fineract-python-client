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

class PutLoansLoanIdCollateral(object):
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
        'client_collateral_id': 'int',
        'quantity': 'float'
    }

    attribute_map = {
        'client_collateral_id': 'clientCollateralId',
        'quantity': 'quantity'
    }

    def __init__(self, client_collateral_id=None, quantity=None):  # noqa: E501
        """PutLoansLoanIdCollateral - a model defined in Swagger"""  # noqa: E501
        self._client_collateral_id = None
        self._quantity = None
        self.discriminator = None
        if client_collateral_id is not None:
            self.client_collateral_id = client_collateral_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def client_collateral_id(self):
        """Gets the client_collateral_id of this PutLoansLoanIdCollateral.  # noqa: E501


        :return: The client_collateral_id of this PutLoansLoanIdCollateral.  # noqa: E501
        :rtype: int
        """
        return self._client_collateral_id

    @client_collateral_id.setter
    def client_collateral_id(self, client_collateral_id):
        """Sets the client_collateral_id of this PutLoansLoanIdCollateral.


        :param client_collateral_id: The client_collateral_id of this PutLoansLoanIdCollateral.  # noqa: E501
        :type: int
        """

        self._client_collateral_id = client_collateral_id

    @property
    def quantity(self):
        """Gets the quantity of this PutLoansLoanIdCollateral.  # noqa: E501


        :return: The quantity of this PutLoansLoanIdCollateral.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PutLoansLoanIdCollateral.


        :param quantity: The quantity of this PutLoansLoanIdCollateral.  # noqa: E501
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
        if issubclass(PutLoansLoanIdCollateral, dict):
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
        if not isinstance(other, PutLoansLoanIdCollateral):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
