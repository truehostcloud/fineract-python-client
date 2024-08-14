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

class GetProductsTypeProductIdResponse(object):
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
        'accounting_mapping_options': 'GetProductsAccountingMappingOptions',
        'accounting_mappings': 'GetProductsAccountingMappings',
        'accounting_rule': 'GetProductsAccountingRule',
        'allow_dividend_calculation_for_inactive_clients': 'bool',
        'charge_options': 'list[GetProductsCharges]',
        'charges': 'list[GetProductsCharges]',
        'currency': 'GetProductsCurrency',
        'currency_options': 'list[GetChargesCurrency]',
        'description': 'str',
        'id': 'int',
        'lock_period_type_enum': 'GetLockPeriodTypeEnum',
        'lockin_period': 'int',
        'lockin_period_frequency_type_options': 'list[GetProductsMinimumActivePeriodFrequencyTypeOptions]',
        'market_price': 'list[GetProductsMarketPrice]',
        'maximum_shares': 'int',
        'minimum_active_period': 'int',
        'minimum_active_period_for_dividends_type_enum': 'GetLockPeriodTypeEnum',
        'minimum_active_period_frequency_type_options': 'list[GetProductsMinimumActivePeriodFrequencyTypeOptions]',
        'minimum_shares': 'int',
        'name': 'str',
        'nominal_shares': 'int',
        'share_capital': 'int',
        'short_name': 'str',
        'total_shares': 'int',
        'total_shares_issued': 'int',
        'unit_price': 'int'
    }

    attribute_map = {
        'accounting_mapping_options': 'accountingMappingOptions',
        'accounting_mappings': 'accountingMappings',
        'accounting_rule': 'accountingRule',
        'allow_dividend_calculation_for_inactive_clients': 'allowDividendCalculationForInactiveClients',
        'charge_options': 'chargeOptions',
        'charges': 'charges',
        'currency': 'currency',
        'currency_options': 'currencyOptions',
        'description': 'description',
        'id': 'id',
        'lock_period_type_enum': 'lockPeriodTypeEnum',
        'lockin_period': 'lockinPeriod',
        'lockin_period_frequency_type_options': 'lockinPeriodFrequencyTypeOptions',
        'market_price': 'marketPrice',
        'maximum_shares': 'maximumShares',
        'minimum_active_period': 'minimumActivePeriod',
        'minimum_active_period_for_dividends_type_enum': 'minimumActivePeriodForDividendsTypeEnum',
        'minimum_active_period_frequency_type_options': 'minimumActivePeriodFrequencyTypeOptions',
        'minimum_shares': 'minimumShares',
        'name': 'name',
        'nominal_shares': 'nominalShares',
        'share_capital': 'shareCapital',
        'short_name': 'shortName',
        'total_shares': 'totalShares',
        'total_shares_issued': 'totalSharesIssued',
        'unit_price': 'unitPrice'
    }

    def __init__(self, accounting_mapping_options=None, accounting_mappings=None, accounting_rule=None, allow_dividend_calculation_for_inactive_clients=None, charge_options=None, charges=None, currency=None, currency_options=None, description=None, id=None, lock_period_type_enum=None, lockin_period=None, lockin_period_frequency_type_options=None, market_price=None, maximum_shares=None, minimum_active_period=None, minimum_active_period_for_dividends_type_enum=None, minimum_active_period_frequency_type_options=None, minimum_shares=None, name=None, nominal_shares=None, share_capital=None, short_name=None, total_shares=None, total_shares_issued=None, unit_price=None):  # noqa: E501
        """GetProductsTypeProductIdResponse - a model defined in Swagger"""  # noqa: E501
        self._accounting_mapping_options = None
        self._accounting_mappings = None
        self._accounting_rule = None
        self._allow_dividend_calculation_for_inactive_clients = None
        self._charge_options = None
        self._charges = None
        self._currency = None
        self._currency_options = None
        self._description = None
        self._id = None
        self._lock_period_type_enum = None
        self._lockin_period = None
        self._lockin_period_frequency_type_options = None
        self._market_price = None
        self._maximum_shares = None
        self._minimum_active_period = None
        self._minimum_active_period_for_dividends_type_enum = None
        self._minimum_active_period_frequency_type_options = None
        self._minimum_shares = None
        self._name = None
        self._nominal_shares = None
        self._share_capital = None
        self._short_name = None
        self._total_shares = None
        self._total_shares_issued = None
        self._unit_price = None
        self.discriminator = None
        if accounting_mapping_options is not None:
            self.accounting_mapping_options = accounting_mapping_options
        if accounting_mappings is not None:
            self.accounting_mappings = accounting_mappings
        if accounting_rule is not None:
            self.accounting_rule = accounting_rule
        if allow_dividend_calculation_for_inactive_clients is not None:
            self.allow_dividend_calculation_for_inactive_clients = allow_dividend_calculation_for_inactive_clients
        if charge_options is not None:
            self.charge_options = charge_options
        if charges is not None:
            self.charges = charges
        if currency is not None:
            self.currency = currency
        if currency_options is not None:
            self.currency_options = currency_options
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if lock_period_type_enum is not None:
            self.lock_period_type_enum = lock_period_type_enum
        if lockin_period is not None:
            self.lockin_period = lockin_period
        if lockin_period_frequency_type_options is not None:
            self.lockin_period_frequency_type_options = lockin_period_frequency_type_options
        if market_price is not None:
            self.market_price = market_price
        if maximum_shares is not None:
            self.maximum_shares = maximum_shares
        if minimum_active_period is not None:
            self.minimum_active_period = minimum_active_period
        if minimum_active_period_for_dividends_type_enum is not None:
            self.minimum_active_period_for_dividends_type_enum = minimum_active_period_for_dividends_type_enum
        if minimum_active_period_frequency_type_options is not None:
            self.minimum_active_period_frequency_type_options = minimum_active_period_frequency_type_options
        if minimum_shares is not None:
            self.minimum_shares = minimum_shares
        if name is not None:
            self.name = name
        if nominal_shares is not None:
            self.nominal_shares = nominal_shares
        if share_capital is not None:
            self.share_capital = share_capital
        if short_name is not None:
            self.short_name = short_name
        if total_shares is not None:
            self.total_shares = total_shares
        if total_shares_issued is not None:
            self.total_shares_issued = total_shares_issued
        if unit_price is not None:
            self.unit_price = unit_price

    @property
    def accounting_mapping_options(self):
        """Gets the accounting_mapping_options of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The accounting_mapping_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetProductsAccountingMappingOptions
        """
        return self._accounting_mapping_options

    @accounting_mapping_options.setter
    def accounting_mapping_options(self, accounting_mapping_options):
        """Sets the accounting_mapping_options of this GetProductsTypeProductIdResponse.


        :param accounting_mapping_options: The accounting_mapping_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetProductsAccountingMappingOptions
        """

        self._accounting_mapping_options = accounting_mapping_options

    @property
    def accounting_mappings(self):
        """Gets the accounting_mappings of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The accounting_mappings of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetProductsAccountingMappings
        """
        return self._accounting_mappings

    @accounting_mappings.setter
    def accounting_mappings(self, accounting_mappings):
        """Sets the accounting_mappings of this GetProductsTypeProductIdResponse.


        :param accounting_mappings: The accounting_mappings of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetProductsAccountingMappings
        """

        self._accounting_mappings = accounting_mappings

    @property
    def accounting_rule(self):
        """Gets the accounting_rule of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The accounting_rule of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetProductsAccountingRule
        """
        return self._accounting_rule

    @accounting_rule.setter
    def accounting_rule(self, accounting_rule):
        """Sets the accounting_rule of this GetProductsTypeProductIdResponse.


        :param accounting_rule: The accounting_rule of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetProductsAccountingRule
        """

        self._accounting_rule = accounting_rule

    @property
    def allow_dividend_calculation_for_inactive_clients(self):
        """Gets the allow_dividend_calculation_for_inactive_clients of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The allow_dividend_calculation_for_inactive_clients of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dividend_calculation_for_inactive_clients

    @allow_dividend_calculation_for_inactive_clients.setter
    def allow_dividend_calculation_for_inactive_clients(self, allow_dividend_calculation_for_inactive_clients):
        """Sets the allow_dividend_calculation_for_inactive_clients of this GetProductsTypeProductIdResponse.


        :param allow_dividend_calculation_for_inactive_clients: The allow_dividend_calculation_for_inactive_clients of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: bool
        """

        self._allow_dividend_calculation_for_inactive_clients = allow_dividend_calculation_for_inactive_clients

    @property
    def charge_options(self):
        """Gets the charge_options of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The charge_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetProductsCharges]
        """
        return self._charge_options

    @charge_options.setter
    def charge_options(self, charge_options):
        """Sets the charge_options of this GetProductsTypeProductIdResponse.


        :param charge_options: The charge_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetProductsCharges]
        """

        self._charge_options = charge_options

    @property
    def charges(self):
        """Gets the charges of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The charges of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetProductsCharges]
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this GetProductsTypeProductIdResponse.


        :param charges: The charges of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetProductsCharges]
        """

        self._charges = charges

    @property
    def currency(self):
        """Gets the currency of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The currency of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetProductsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetProductsTypeProductIdResponse.


        :param currency: The currency of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetProductsCurrency
        """

        self._currency = currency

    @property
    def currency_options(self):
        """Gets the currency_options of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The currency_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetChargesCurrency]
        """
        return self._currency_options

    @currency_options.setter
    def currency_options(self, currency_options):
        """Sets the currency_options of this GetProductsTypeProductIdResponse.


        :param currency_options: The currency_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetChargesCurrency]
        """

        self._currency_options = currency_options

    @property
    def description(self):
        """Gets the description of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The description of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetProductsTypeProductIdResponse.


        :param description: The description of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The id of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductsTypeProductIdResponse.


        :param id: The id of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lock_period_type_enum(self):
        """Gets the lock_period_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The lock_period_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetLockPeriodTypeEnum
        """
        return self._lock_period_type_enum

    @lock_period_type_enum.setter
    def lock_period_type_enum(self, lock_period_type_enum):
        """Sets the lock_period_type_enum of this GetProductsTypeProductIdResponse.


        :param lock_period_type_enum: The lock_period_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetLockPeriodTypeEnum
        """

        self._lock_period_type_enum = lock_period_type_enum

    @property
    def lockin_period(self):
        """Gets the lockin_period of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The lockin_period of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._lockin_period

    @lockin_period.setter
    def lockin_period(self, lockin_period):
        """Sets the lockin_period of this GetProductsTypeProductIdResponse.


        :param lockin_period: The lockin_period of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._lockin_period = lockin_period

    @property
    def lockin_period_frequency_type_options(self):
        """Gets the lockin_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The lockin_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetProductsMinimumActivePeriodFrequencyTypeOptions]
        """
        return self._lockin_period_frequency_type_options

    @lockin_period_frequency_type_options.setter
    def lockin_period_frequency_type_options(self, lockin_period_frequency_type_options):
        """Sets the lockin_period_frequency_type_options of this GetProductsTypeProductIdResponse.


        :param lockin_period_frequency_type_options: The lockin_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetProductsMinimumActivePeriodFrequencyTypeOptions]
        """

        self._lockin_period_frequency_type_options = lockin_period_frequency_type_options

    @property
    def market_price(self):
        """Gets the market_price of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The market_price of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetProductsMarketPrice]
        """
        return self._market_price

    @market_price.setter
    def market_price(self, market_price):
        """Sets the market_price of this GetProductsTypeProductIdResponse.


        :param market_price: The market_price of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetProductsMarketPrice]
        """

        self._market_price = market_price

    @property
    def maximum_shares(self):
        """Gets the maximum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The maximum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._maximum_shares

    @maximum_shares.setter
    def maximum_shares(self, maximum_shares):
        """Sets the maximum_shares of this GetProductsTypeProductIdResponse.


        :param maximum_shares: The maximum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._maximum_shares = maximum_shares

    @property
    def minimum_active_period(self):
        """Gets the minimum_active_period of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The minimum_active_period of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._minimum_active_period

    @minimum_active_period.setter
    def minimum_active_period(self, minimum_active_period):
        """Sets the minimum_active_period of this GetProductsTypeProductIdResponse.


        :param minimum_active_period: The minimum_active_period of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._minimum_active_period = minimum_active_period

    @property
    def minimum_active_period_for_dividends_type_enum(self):
        """Gets the minimum_active_period_for_dividends_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The minimum_active_period_for_dividends_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: GetLockPeriodTypeEnum
        """
        return self._minimum_active_period_for_dividends_type_enum

    @minimum_active_period_for_dividends_type_enum.setter
    def minimum_active_period_for_dividends_type_enum(self, minimum_active_period_for_dividends_type_enum):
        """Sets the minimum_active_period_for_dividends_type_enum of this GetProductsTypeProductIdResponse.


        :param minimum_active_period_for_dividends_type_enum: The minimum_active_period_for_dividends_type_enum of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: GetLockPeriodTypeEnum
        """

        self._minimum_active_period_for_dividends_type_enum = minimum_active_period_for_dividends_type_enum

    @property
    def minimum_active_period_frequency_type_options(self):
        """Gets the minimum_active_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The minimum_active_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: list[GetProductsMinimumActivePeriodFrequencyTypeOptions]
        """
        return self._minimum_active_period_frequency_type_options

    @minimum_active_period_frequency_type_options.setter
    def minimum_active_period_frequency_type_options(self, minimum_active_period_frequency_type_options):
        """Sets the minimum_active_period_frequency_type_options of this GetProductsTypeProductIdResponse.


        :param minimum_active_period_frequency_type_options: The minimum_active_period_frequency_type_options of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: list[GetProductsMinimumActivePeriodFrequencyTypeOptions]
        """

        self._minimum_active_period_frequency_type_options = minimum_active_period_frequency_type_options

    @property
    def minimum_shares(self):
        """Gets the minimum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The minimum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._minimum_shares

    @minimum_shares.setter
    def minimum_shares(self, minimum_shares):
        """Sets the minimum_shares of this GetProductsTypeProductIdResponse.


        :param minimum_shares: The minimum_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._minimum_shares = minimum_shares

    @property
    def name(self):
        """Gets the name of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The name of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductsTypeProductIdResponse.


        :param name: The name of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nominal_shares(self):
        """Gets the nominal_shares of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The nominal_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._nominal_shares

    @nominal_shares.setter
    def nominal_shares(self, nominal_shares):
        """Sets the nominal_shares of this GetProductsTypeProductIdResponse.


        :param nominal_shares: The nominal_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._nominal_shares = nominal_shares

    @property
    def share_capital(self):
        """Gets the share_capital of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The share_capital of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._share_capital

    @share_capital.setter
    def share_capital(self, share_capital):
        """Sets the share_capital of this GetProductsTypeProductIdResponse.


        :param share_capital: The share_capital of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._share_capital = share_capital

    @property
    def short_name(self):
        """Gets the short_name of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The short_name of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetProductsTypeProductIdResponse.


        :param short_name: The short_name of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def total_shares(self):
        """Gets the total_shares of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The total_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_shares

    @total_shares.setter
    def total_shares(self, total_shares):
        """Sets the total_shares of this GetProductsTypeProductIdResponse.


        :param total_shares: The total_shares of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._total_shares = total_shares

    @property
    def total_shares_issued(self):
        """Gets the total_shares_issued of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The total_shares_issued of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_shares_issued

    @total_shares_issued.setter
    def total_shares_issued(self, total_shares_issued):
        """Sets the total_shares_issued of this GetProductsTypeProductIdResponse.


        :param total_shares_issued: The total_shares_issued of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
        """

        self._total_shares_issued = total_shares_issued

    @property
    def unit_price(self):
        """Gets the unit_price of this GetProductsTypeProductIdResponse.  # noqa: E501


        :return: The unit_price of this GetProductsTypeProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this GetProductsTypeProductIdResponse.


        :param unit_price: The unit_price of this GetProductsTypeProductIdResponse.  # noqa: E501
        :type: int
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
        if issubclass(GetProductsTypeProductIdResponse, dict):
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
        if not isinstance(other, GetProductsTypeProductIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
