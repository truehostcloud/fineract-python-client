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

class GetSelfLoansLoanIdChargesResponse(object):
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
        'amount_or_percentage': 'float',
        'amount_outstanding': 'float',
        'amount_paid': 'float',
        'amount_percentage_applied_to': 'float',
        'amount_waived': 'float',
        'amount_written_off': 'float',
        'charge_calculation_type': 'GetSelfLoansChargeCalculationType',
        'charge_id': 'int',
        'charge_time_type': 'GetSelfLoansChargeTimeType',
        'currency': 'GetLoanCurrency',
        'id': 'int',
        'name': 'str',
        'penalty': 'bool',
        'percentage': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_or_percentage': 'amountOrPercentage',
        'amount_outstanding': 'amountOutstanding',
        'amount_paid': 'amountPaid',
        'amount_percentage_applied_to': 'amountPercentageAppliedTo',
        'amount_waived': 'amountWaived',
        'amount_written_off': 'amountWrittenOff',
        'charge_calculation_type': 'chargeCalculationType',
        'charge_id': 'chargeId',
        'charge_time_type': 'chargeTimeType',
        'currency': 'currency',
        'id': 'id',
        'name': 'name',
        'penalty': 'penalty',
        'percentage': 'percentage'
    }

    def __init__(self, amount=None, amount_or_percentage=None, amount_outstanding=None, amount_paid=None, amount_percentage_applied_to=None, amount_waived=None, amount_written_off=None, charge_calculation_type=None, charge_id=None, charge_time_type=None, currency=None, id=None, name=None, penalty=None, percentage=None):  # noqa: E501
        """GetSelfLoansLoanIdChargesResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._amount_or_percentage = None
        self._amount_outstanding = None
        self._amount_paid = None
        self._amount_percentage_applied_to = None
        self._amount_waived = None
        self._amount_written_off = None
        self._charge_calculation_type = None
        self._charge_id = None
        self._charge_time_type = None
        self._currency = None
        self._id = None
        self._name = None
        self._penalty = None
        self._percentage = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if amount_or_percentage is not None:
            self.amount_or_percentage = amount_or_percentage
        if amount_outstanding is not None:
            self.amount_outstanding = amount_outstanding
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if amount_percentage_applied_to is not None:
            self.amount_percentage_applied_to = amount_percentage_applied_to
        if amount_waived is not None:
            self.amount_waived = amount_waived
        if amount_written_off is not None:
            self.amount_written_off = amount_written_off
        if charge_calculation_type is not None:
            self.charge_calculation_type = charge_calculation_type
        if charge_id is not None:
            self.charge_id = charge_id
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
        if percentage is not None:
            self.percentage = percentage

    @property
    def amount(self):
        """Gets the amount of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetSelfLoansLoanIdChargesResponse.


        :param amount: The amount of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_or_percentage(self):
        """Gets the amount_or_percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_or_percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_or_percentage

    @amount_or_percentage.setter
    def amount_or_percentage(self, amount_or_percentage):
        """Sets the amount_or_percentage of this GetSelfLoansLoanIdChargesResponse.


        :param amount_or_percentage: The amount_or_percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_or_percentage = amount_or_percentage

    @property
    def amount_outstanding(self):
        """Gets the amount_outstanding of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_outstanding of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_outstanding

    @amount_outstanding.setter
    def amount_outstanding(self, amount_outstanding):
        """Sets the amount_outstanding of this GetSelfLoansLoanIdChargesResponse.


        :param amount_outstanding: The amount_outstanding of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_outstanding = amount_outstanding

    @property
    def amount_paid(self):
        """Gets the amount_paid of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_paid of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this GetSelfLoansLoanIdChargesResponse.


        :param amount_paid: The amount_paid of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_paid = amount_paid

    @property
    def amount_percentage_applied_to(self):
        """Gets the amount_percentage_applied_to of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_percentage_applied_to of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_percentage_applied_to

    @amount_percentage_applied_to.setter
    def amount_percentage_applied_to(self, amount_percentage_applied_to):
        """Sets the amount_percentage_applied_to of this GetSelfLoansLoanIdChargesResponse.


        :param amount_percentage_applied_to: The amount_percentage_applied_to of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_percentage_applied_to = amount_percentage_applied_to

    @property
    def amount_waived(self):
        """Gets the amount_waived of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_waived of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_waived

    @amount_waived.setter
    def amount_waived(self, amount_waived):
        """Sets the amount_waived of this GetSelfLoansLoanIdChargesResponse.


        :param amount_waived: The amount_waived of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_waived = amount_waived

    @property
    def amount_written_off(self):
        """Gets the amount_written_off of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The amount_written_off of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_written_off

    @amount_written_off.setter
    def amount_written_off(self, amount_written_off):
        """Sets the amount_written_off of this GetSelfLoansLoanIdChargesResponse.


        :param amount_written_off: The amount_written_off of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._amount_written_off = amount_written_off

    @property
    def charge_calculation_type(self):
        """Gets the charge_calculation_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The charge_calculation_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: GetSelfLoansChargeCalculationType
        """
        return self._charge_calculation_type

    @charge_calculation_type.setter
    def charge_calculation_type(self, charge_calculation_type):
        """Sets the charge_calculation_type of this GetSelfLoansLoanIdChargesResponse.


        :param charge_calculation_type: The charge_calculation_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: GetSelfLoansChargeCalculationType
        """

        self._charge_calculation_type = charge_calculation_type

    @property
    def charge_id(self):
        """Gets the charge_id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The charge_id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: int
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        """Sets the charge_id of this GetSelfLoansLoanIdChargesResponse.


        :param charge_id: The charge_id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: int
        """

        self._charge_id = charge_id

    @property
    def charge_time_type(self):
        """Gets the charge_time_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The charge_time_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: GetSelfLoansChargeTimeType
        """
        return self._charge_time_type

    @charge_time_type.setter
    def charge_time_type(self, charge_time_type):
        """Sets the charge_time_type of this GetSelfLoansLoanIdChargesResponse.


        :param charge_time_type: The charge_time_type of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: GetSelfLoansChargeTimeType
        """

        self._charge_time_type = charge_time_type

    @property
    def currency(self):
        """Gets the currency of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The currency of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: GetLoanCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetSelfLoansLoanIdChargesResponse.


        :param currency: The currency of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: GetLoanCurrency
        """

        self._currency = currency

    @property
    def id(self):
        """Gets the id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSelfLoansLoanIdChargesResponse.


        :param id: The id of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The name of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetSelfLoansLoanIdChargesResponse.


        :param name: The name of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def penalty(self):
        """Gets the penalty of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The penalty of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this GetSelfLoansLoanIdChargesResponse.


        :param penalty: The penalty of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: bool
        """

        self._penalty = penalty

    @property
    def percentage(self):
        """Gets the percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501


        :return: The percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this GetSelfLoansLoanIdChargesResponse.


        :param percentage: The percentage of this GetSelfLoansLoanIdChargesResponse.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

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
        if issubclass(GetSelfLoansLoanIdChargesResponse, dict):
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
        if not isinstance(other, GetSelfLoansLoanIdChargesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
