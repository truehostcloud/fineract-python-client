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

class GetProductsCharges(object):
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
        'active': 'bool',
        'amount': 'int',
        'charge_applies_to': 'GetChargeAppliesTo',
        'charge_calculation_type': 'GetChargeCalculationType',
        'charge_payment_mode': 'GetChargePaymentMode',
        'charge_time_type': 'GetChargeTimeType',
        'currency': 'GetChargesCurrency',
        'id': 'int',
        'name': 'str',
        'penalty': 'bool'
    }

    attribute_map = {
        'active': 'active',
        'amount': 'amount',
        'charge_applies_to': 'chargeAppliesTo',
        'charge_calculation_type': 'chargeCalculationType',
        'charge_payment_mode': 'chargePaymentMode',
        'charge_time_type': 'chargeTimeType',
        'currency': 'currency',
        'id': 'id',
        'name': 'name',
        'penalty': 'penalty'
    }

    def __init__(self, active=None, amount=None, charge_applies_to=None, charge_calculation_type=None, charge_payment_mode=None, charge_time_type=None, currency=None, id=None, name=None, penalty=None):  # noqa: E501
        """GetProductsCharges - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._amount = None
        self._charge_applies_to = None
        self._charge_calculation_type = None
        self._charge_payment_mode = None
        self._charge_time_type = None
        self._currency = None
        self._id = None
        self._name = None
        self._penalty = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if amount is not None:
            self.amount = amount
        if charge_applies_to is not None:
            self.charge_applies_to = charge_applies_to
        if charge_calculation_type is not None:
            self.charge_calculation_type = charge_calculation_type
        if charge_payment_mode is not None:
            self.charge_payment_mode = charge_payment_mode
        if charge_time_type is not None:
            self.charge_time_type = charge_time_type
        if currency is not None:
            self.currency = currency
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if penalty is not None:
            self.penalty = penalty

    @property
    def active(self):
        """Gets the active of this GetProductsCharges.  # noqa: E501


        :return: The active of this GetProductsCharges.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GetProductsCharges.


        :param active: The active of this GetProductsCharges.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def amount(self):
        """Gets the amount of this GetProductsCharges.  # noqa: E501


        :return: The amount of this GetProductsCharges.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetProductsCharges.


        :param amount: The amount of this GetProductsCharges.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def charge_applies_to(self):
        """Gets the charge_applies_to of this GetProductsCharges.  # noqa: E501


        :return: The charge_applies_to of this GetProductsCharges.  # noqa: E501
        :rtype: GetChargeAppliesTo
        """
        return self._charge_applies_to

    @charge_applies_to.setter
    def charge_applies_to(self, charge_applies_to):
        """Sets the charge_applies_to of this GetProductsCharges.


        :param charge_applies_to: The charge_applies_to of this GetProductsCharges.  # noqa: E501
        :type: GetChargeAppliesTo
        """

        self._charge_applies_to = charge_applies_to

    @property
    def charge_calculation_type(self):
        """Gets the charge_calculation_type of this GetProductsCharges.  # noqa: E501


        :return: The charge_calculation_type of this GetProductsCharges.  # noqa: E501
        :rtype: GetChargeCalculationType
        """
        return self._charge_calculation_type

    @charge_calculation_type.setter
    def charge_calculation_type(self, charge_calculation_type):
        """Sets the charge_calculation_type of this GetProductsCharges.


        :param charge_calculation_type: The charge_calculation_type of this GetProductsCharges.  # noqa: E501
        :type: GetChargeCalculationType
        """

        self._charge_calculation_type = charge_calculation_type

    @property
    def charge_payment_mode(self):
        """Gets the charge_payment_mode of this GetProductsCharges.  # noqa: E501


        :return: The charge_payment_mode of this GetProductsCharges.  # noqa: E501
        :rtype: GetChargePaymentMode
        """
        return self._charge_payment_mode

    @charge_payment_mode.setter
    def charge_payment_mode(self, charge_payment_mode):
        """Sets the charge_payment_mode of this GetProductsCharges.


        :param charge_payment_mode: The charge_payment_mode of this GetProductsCharges.  # noqa: E501
        :type: GetChargePaymentMode
        """

        self._charge_payment_mode = charge_payment_mode

    @property
    def charge_time_type(self):
        """Gets the charge_time_type of this GetProductsCharges.  # noqa: E501


        :return: The charge_time_type of this GetProductsCharges.  # noqa: E501
        :rtype: GetChargeTimeType
        """
        return self._charge_time_type

    @charge_time_type.setter
    def charge_time_type(self, charge_time_type):
        """Sets the charge_time_type of this GetProductsCharges.


        :param charge_time_type: The charge_time_type of this GetProductsCharges.  # noqa: E501
        :type: GetChargeTimeType
        """

        self._charge_time_type = charge_time_type

    @property
    def currency(self):
        """Gets the currency of this GetProductsCharges.  # noqa: E501


        :return: The currency of this GetProductsCharges.  # noqa: E501
        :rtype: GetChargesCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetProductsCharges.


        :param currency: The currency of this GetProductsCharges.  # noqa: E501
        :type: GetChargesCurrency
        """

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this GetProductsCharges.  # noqa: E501


        :return: The id of this GetProductsCharges.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductsCharges.


        :param id: The id of this GetProductsCharges.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetProductsCharges.  # noqa: E501


        :return: The name of this GetProductsCharges.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductsCharges.


        :param name: The name of this GetProductsCharges.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def penalty(self):
        """Gets the penalty of this GetProductsCharges.  # noqa: E501


        :return: The penalty of this GetProductsCharges.  # noqa: E501
        :rtype: bool
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this GetProductsCharges.


        :param penalty: The penalty of this GetProductsCharges.  # noqa: E501
        :type: bool
        """

        self._penalty = penalty

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
        if issubclass(GetProductsCharges, dict):
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
        if not isinstance(other, GetProductsCharges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
