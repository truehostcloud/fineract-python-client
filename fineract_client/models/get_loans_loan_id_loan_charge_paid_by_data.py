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

class GetLoansLoanIdLoanChargePaidByData(object):
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
        'amount': 'float',
        'charge_id': 'int',
        'id': 'int',
        'installment_number': 'int',
        'name': 'str',
        'transaction_id': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'charge_id': 'chargeId',
        'id': 'id',
        'installment_number': 'installmentNumber',
        'name': 'name',
        'transaction_id': 'transactionId'
    }

    def __init__(self, amount=None, charge_id=None, id=None, installment_number=None, name=None, transaction_id=None):  # noqa: E501
        """GetLoansLoanIdLoanChargePaidByData - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._charge_id = None
        self._id = None
        self._installment_number = None
        self._name = None
        self._transaction_id = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if charge_id is not None:
            self.charge_id = charge_id
        if id is not None:
            self.id = id
        if installment_number is not None:
            self.installment_number = installment_number
        if name is not None:
            self.name = name
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def amount(self):
        """Gets the amount of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The amount of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetLoansLoanIdLoanChargePaidByData.


        :param amount: The amount of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def charge_id(self):
        """Gets the charge_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The charge_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: int
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this GetLoansLoanIdLoanChargePaidByData.


        :param charge_id: The charge_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: int
        """

        self._charge_id = charge_id

    @property
    def id(self):
        """Gets the id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetLoansLoanIdLoanChargePaidByData.


        :param id: The id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def installment_number(self):
        """Gets the installment_number of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The installment_number of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: int
        """
        return self._installment_number

    @installment_number.setter
    def installment_number(self, installment_number):
        """Sets the installment_number of this GetLoansLoanIdLoanChargePaidByData.


        :param installment_number: The installment_number of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: int
        """

        self._installment_number = installment_number

    @property
    def name(self):
        """Gets the name of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The name of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetLoansLoanIdLoanChargePaidByData.


        :param name: The name of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def transaction_id(self):
        """Gets the transaction_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501


        :return: The transaction_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this GetLoansLoanIdLoanChargePaidByData.


        :param transaction_id: The transaction_id of this GetLoansLoanIdLoanChargePaidByData.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

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
        if issubclass(GetLoansLoanIdLoanChargePaidByData, dict):
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
        if not isinstance(other, GetLoansLoanIdLoanChargePaidByData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
