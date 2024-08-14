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

class GetRecurringDepositProductsProductIdResponse(object):
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
        'accounting_mappings': 'GetRecurringDepositProductsProductIdAccountingMappings',
        'active_chart': 'GetRecurringDepositProductsProductIdActiveChart',
        'currency': 'GetRecurringDepositProductsProductIdCurrency',
        'description': 'str',
        'fee_to_income_account_mappings': 'list[GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings]',
        'id': 'int',
        'interest_calculation_days_in_year_type': 'GetRecurringDepositProductsInterestCalculationDaysInYearType',
        'interest_calculation_type': 'GetRecurringDepositProductsInterestCalculationType',
        'interest_compounding_period_type': 'GetRecurringDepositProductsProductIdInterestCompoundingPeriodType',
        'interest_posting_period_type': 'GetRecurringDepositProductsInterestPostingPeriodType',
        'max_deposit_term': 'int',
        'max_deposit_term_type': 'GetRecurringDepositProductsProductIdMaxDepositTermType',
        'min_deposit_term': 'int',
        'min_deposit_term_type': 'GetRecurringDepositProductsProductIdMinDepositTermType',
        'name': 'str',
        'penalty_to_income_account_mappings': 'list[GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings]',
        'pre_closure_penal_applicable': 'bool',
        'pre_closure_penal_interest': 'float',
        'pre_closure_penal_interest_on_type': 'GetRecurringDepositProductsProductIdPreClosurePenalInterestOnType',
        'recurring_deposit_frequency': 'int',
        'recurring_deposit_frequency_type': 'GetRecurringDepositProductsRecurringDepositFrequencyType',
        'short_name': 'str'
    }

    attribute_map = {
        'accounting_mappings': 'accountingMappings',
        'active_chart': 'activeChart',
        'currency': 'currency',
        'description': 'description',
        'fee_to_income_account_mappings': 'feeToIncomeAccountMappings',
        'id': 'id',
        'interest_calculation_days_in_year_type': 'interestCalculationDaysInYearType',
        'interest_calculation_type': 'interestCalculationType',
        'interest_compounding_period_type': 'interestCompoundingPeriodType',
        'interest_posting_period_type': 'interestPostingPeriodType',
        'max_deposit_term': 'maxDepositTerm',
        'max_deposit_term_type': 'maxDepositTermType',
        'min_deposit_term': 'minDepositTerm',
        'min_deposit_term_type': 'minDepositTermType',
        'name': 'name',
        'penalty_to_income_account_mappings': 'penaltyToIncomeAccountMappings',
        'pre_closure_penal_applicable': 'preClosurePenalApplicable',
        'pre_closure_penal_interest': 'preClosurePenalInterest',
        'pre_closure_penal_interest_on_type': 'preClosurePenalInterestOnType',
        'recurring_deposit_frequency': 'recurringDepositFrequency',
        'recurring_deposit_frequency_type': 'recurringDepositFrequencyType',
        'short_name': 'shortName'
    }

    def __init__(self, accounting_mappings=None, active_chart=None, currency=None, description=None, fee_to_income_account_mappings=None, id=None, interest_calculation_days_in_year_type=None, interest_calculation_type=None, interest_compounding_period_type=None, interest_posting_period_type=None, max_deposit_term=None, max_deposit_term_type=None, min_deposit_term=None, min_deposit_term_type=None, name=None, penalty_to_income_account_mappings=None, pre_closure_penal_applicable=None, pre_closure_penal_interest=None, pre_closure_penal_interest_on_type=None, recurring_deposit_frequency=None, recurring_deposit_frequency_type=None, short_name=None):  # noqa: E501
        """GetRecurringDepositProductsProductIdResponse - a model defined in Swagger"""  # noqa: E501
        self._accounting_mappings = None
        self._active_chart = None
        self._currency = None
        self._description = None
        self._fee_to_income_account_mappings = None
        self._id = None
        self._interest_calculation_days_in_year_type = None
        self._interest_calculation_type = None
        self._interest_compounding_period_type = None
        self._interest_posting_period_type = None
        self._max_deposit_term = None
        self._max_deposit_term_type = None
        self._min_deposit_term = None
        self._min_deposit_term_type = None
        self._name = None
        self._penalty_to_income_account_mappings = None
        self._pre_closure_penal_applicable = None
        self._pre_closure_penal_interest = None
        self._pre_closure_penal_interest_on_type = None
        self._recurring_deposit_frequency = None
        self._recurring_deposit_frequency_type = None
        self._short_name = None
        self.discriminator = None
        if accounting_mappings is not None:
            self.accounting_mappings = accounting_mappings
        if active_chart is not None:
            self.active_chart = active_chart
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if fee_to_income_account_mappings is not None:
            self.fee_to_income_account_mappings = fee_to_income_account_mappings
        if id is not None:
            self.id = id
        if interest_calculation_days_in_year_type is not None:
            self.interest_calculation_days_in_year_type = interest_calculation_days_in_year_type
        if interest_calculation_type is not None:
            self.interest_calculation_type = interest_calculation_type
        if interest_compounding_period_type is not None:
            self.interest_compounding_period_type = interest_compounding_period_type
        if interest_posting_period_type is not None:
            self.interest_posting_period_type = interest_posting_period_type
        if max_deposit_term is not None:
            self.max_deposit_term = max_deposit_term
        if max_deposit_term_type is not None:
            self.max_deposit_term_type = max_deposit_term_type
        if min_deposit_term is not None:
            self.min_deposit_term = min_deposit_term
        if min_deposit_term_type is not None:
            self.min_deposit_term_type = min_deposit_term_type
        if name is not None:
            self.name = name
        if penalty_to_income_account_mappings is not None:
            self.penalty_to_income_account_mappings = penalty_to_income_account_mappings
        if pre_closure_penal_applicable is not None:
            self.pre_closure_penal_applicable = pre_closure_penal_applicable
        if pre_closure_penal_interest is not None:
            self.pre_closure_penal_interest = pre_closure_penal_interest
        if pre_closure_penal_interest_on_type is not None:
            self.pre_closure_penal_interest_on_type = pre_closure_penal_interest_on_type
        if recurring_deposit_frequency is not None:
            self.recurring_deposit_frequency = recurring_deposit_frequency
        if recurring_deposit_frequency_type is not None:
            self.recurring_deposit_frequency_type = recurring_deposit_frequency_type
        if short_name is not None:
            self.short_name = short_name

    @property
    def accounting_mappings(self):
        """Gets the accounting_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The accounting_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdAccountingMappings
        """
        return self._accounting_mappings

    @accounting_mappings.setter
    def accounting_mappings(self, accounting_mappings):
        """Sets the accounting_mappings of this GetRecurringDepositProductsProductIdResponse.


        :param accounting_mappings: The accounting_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdAccountingMappings
        """

        self._accounting_mappings = accounting_mappings

    @property
    def active_chart(self):
        """Gets the active_chart of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The active_chart of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdActiveChart
        """
        return self._active_chart

    @active_chart.setter
    def active_chart(self, active_chart):
        """Sets the active_chart of this GetRecurringDepositProductsProductIdResponse.


        :param active_chart: The active_chart of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdActiveChart
        """

        self._active_chart = active_chart

    @property
    def currency(self):
        """Gets the currency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The currency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetRecurringDepositProductsProductIdResponse.


        :param currency: The currency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdCurrency
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The description of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetRecurringDepositProductsProductIdResponse.


        :param description: The description of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fee_to_income_account_mappings(self):
        """Gets the fee_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The fee_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: list[GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings]
        """
        return self._fee_to_income_account_mappings

    @fee_to_income_account_mappings.setter
    def fee_to_income_account_mappings(self, fee_to_income_account_mappings):
        """Sets the fee_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.


        :param fee_to_income_account_mappings: The fee_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: list[GetRecurringDepositProductsProductIdFeeToIncomeAccountMappings]
        """

        self._fee_to_income_account_mappings = fee_to_income_account_mappings

    @property
    def id(self):
        """Gets the id of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The id of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetRecurringDepositProductsProductIdResponse.


        :param id: The id of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_calculation_days_in_year_type(self):
        """Gets the interest_calculation_days_in_year_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The interest_calculation_days_in_year_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsInterestCalculationDaysInYearType
        """
        return self._interest_calculation_days_in_year_type

    @interest_calculation_days_in_year_type.setter
    def interest_calculation_days_in_year_type(self, interest_calculation_days_in_year_type):
        """Sets the interest_calculation_days_in_year_type of this GetRecurringDepositProductsProductIdResponse.


        :param interest_calculation_days_in_year_type: The interest_calculation_days_in_year_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsInterestCalculationDaysInYearType
        """

        self._interest_calculation_days_in_year_type = interest_calculation_days_in_year_type

    @property
    def interest_calculation_type(self):
        """Gets the interest_calculation_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The interest_calculation_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsInterestCalculationType
        """
        return self._interest_calculation_type

    @interest_calculation_type.setter
    def interest_calculation_type(self, interest_calculation_type):
        """Sets the interest_calculation_type of this GetRecurringDepositProductsProductIdResponse.


        :param interest_calculation_type: The interest_calculation_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsInterestCalculationType
        """

        self._interest_calculation_type = interest_calculation_type

    @property
    def interest_compounding_period_type(self):
        """Gets the interest_compounding_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The interest_compounding_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdInterestCompoundingPeriodType
        """
        return self._interest_compounding_period_type

    @interest_compounding_period_type.setter
    def interest_compounding_period_type(self, interest_compounding_period_type):
        """Sets the interest_compounding_period_type of this GetRecurringDepositProductsProductIdResponse.


        :param interest_compounding_period_type: The interest_compounding_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdInterestCompoundingPeriodType
        """

        self._interest_compounding_period_type = interest_compounding_period_type

    @property
    def interest_posting_period_type(self):
        """Gets the interest_posting_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The interest_posting_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsInterestPostingPeriodType
        """
        return self._interest_posting_period_type

    @interest_posting_period_type.setter
    def interest_posting_period_type(self, interest_posting_period_type):
        """Sets the interest_posting_period_type of this GetRecurringDepositProductsProductIdResponse.


        :param interest_posting_period_type: The interest_posting_period_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsInterestPostingPeriodType
        """

        self._interest_posting_period_type = interest_posting_period_type

    @property
    def max_deposit_term(self):
        """Gets the max_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The max_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._max_deposit_term

    @max_deposit_term.setter
    def max_deposit_term(self, max_deposit_term):
        """Sets the max_deposit_term of this GetRecurringDepositProductsProductIdResponse.


        :param max_deposit_term: The max_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: int
        """

        self._max_deposit_term = max_deposit_term

    @property
    def max_deposit_term_type(self):
        """Gets the max_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The max_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdMaxDepositTermType
        """
        return self._max_deposit_term_type

    @max_deposit_term_type.setter
    def max_deposit_term_type(self, max_deposit_term_type):
        """Sets the max_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.


        :param max_deposit_term_type: The max_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdMaxDepositTermType
        """

        self._max_deposit_term_type = max_deposit_term_type

    @property
    def min_deposit_term(self):
        """Gets the min_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The min_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._min_deposit_term

    @min_deposit_term.setter
    def min_deposit_term(self, min_deposit_term):
        """Sets the min_deposit_term of this GetRecurringDepositProductsProductIdResponse.


        :param min_deposit_term: The min_deposit_term of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: int
        """

        self._min_deposit_term = min_deposit_term

    @property
    def min_deposit_term_type(self):
        """Gets the min_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The min_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdMinDepositTermType
        """
        return self._min_deposit_term_type

    @min_deposit_term_type.setter
    def min_deposit_term_type(self, min_deposit_term_type):
        """Sets the min_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.


        :param min_deposit_term_type: The min_deposit_term_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdMinDepositTermType
        """

        self._min_deposit_term_type = min_deposit_term_type

    @property
    def name(self):
        """Gets the name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetRecurringDepositProductsProductIdResponse.


        :param name: The name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def penalty_to_income_account_mappings(self):
        """Gets the penalty_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The penalty_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: list[GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings]
        """
        return self._penalty_to_income_account_mappings

    @penalty_to_income_account_mappings.setter
    def penalty_to_income_account_mappings(self, penalty_to_income_account_mappings):
        """Sets the penalty_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.


        :param penalty_to_income_account_mappings: The penalty_to_income_account_mappings of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: list[GetRecurringDepositProductsProductIdPenaltyToIncomeAccountMappings]
        """

        self._penalty_to_income_account_mappings = penalty_to_income_account_mappings

    @property
    def pre_closure_penal_applicable(self):
        """Gets the pre_closure_penal_applicable of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The pre_closure_penal_applicable of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._pre_closure_penal_applicable

    @pre_closure_penal_applicable.setter
    def pre_closure_penal_applicable(self, pre_closure_penal_applicable):
        """Sets the pre_closure_penal_applicable of this GetRecurringDepositProductsProductIdResponse.


        :param pre_closure_penal_applicable: The pre_closure_penal_applicable of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: bool
        """

        self._pre_closure_penal_applicable = pre_closure_penal_applicable

    @property
    def pre_closure_penal_interest(self):
        """Gets the pre_closure_penal_interest of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The pre_closure_penal_interest of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: float
        """
        return self._pre_closure_penal_interest

    @pre_closure_penal_interest.setter
    def pre_closure_penal_interest(self, pre_closure_penal_interest):
        """Sets the pre_closure_penal_interest of this GetRecurringDepositProductsProductIdResponse.


        :param pre_closure_penal_interest: The pre_closure_penal_interest of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: float
        """

        self._pre_closure_penal_interest = pre_closure_penal_interest

    @property
    def pre_closure_penal_interest_on_type(self):
        """Gets the pre_closure_penal_interest_on_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The pre_closure_penal_interest_on_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsProductIdPreClosurePenalInterestOnType
        """
        return self._pre_closure_penal_interest_on_type

    @pre_closure_penal_interest_on_type.setter
    def pre_closure_penal_interest_on_type(self, pre_closure_penal_interest_on_type):
        """Sets the pre_closure_penal_interest_on_type of this GetRecurringDepositProductsProductIdResponse.


        :param pre_closure_penal_interest_on_type: The pre_closure_penal_interest_on_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsProductIdPreClosurePenalInterestOnType
        """

        self._pre_closure_penal_interest_on_type = pre_closure_penal_interest_on_type

    @property
    def recurring_deposit_frequency(self):
        """Gets the recurring_deposit_frequency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The recurring_deposit_frequency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._recurring_deposit_frequency

    @recurring_deposit_frequency.setter
    def recurring_deposit_frequency(self, recurring_deposit_frequency):
        """Sets the recurring_deposit_frequency of this GetRecurringDepositProductsProductIdResponse.


        :param recurring_deposit_frequency: The recurring_deposit_frequency of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: int
        """

        self._recurring_deposit_frequency = recurring_deposit_frequency

    @property
    def recurring_deposit_frequency_type(self):
        """Gets the recurring_deposit_frequency_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The recurring_deposit_frequency_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: GetRecurringDepositProductsRecurringDepositFrequencyType
        """
        return self._recurring_deposit_frequency_type

    @recurring_deposit_frequency_type.setter
    def recurring_deposit_frequency_type(self, recurring_deposit_frequency_type):
        """Sets the recurring_deposit_frequency_type of this GetRecurringDepositProductsProductIdResponse.


        :param recurring_deposit_frequency_type: The recurring_deposit_frequency_type of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: GetRecurringDepositProductsRecurringDepositFrequencyType
        """

        self._recurring_deposit_frequency_type = recurring_deposit_frequency_type

    @property
    def short_name(self):
        """Gets the short_name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501


        :return: The short_name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this GetRecurringDepositProductsProductIdResponse.


        :param short_name: The short_name of this GetRecurringDepositProductsProductIdResponse.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

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
        if issubclass(GetRecurringDepositProductsProductIdResponse, dict):
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
        if not isinstance(other, GetRecurringDepositProductsProductIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
