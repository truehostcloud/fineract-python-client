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

class GetRecurringDepositAccountsResponse(object):
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
        'account_no': 'int',
        'client_id': 'int',
        'client_name': 'str',
        'currency': 'GetRecurringDepositAccountsCurrency',
        'deposit_amount': 'float',
        'deposit_period': 'int',
        'deposit_period_frequency': 'GetRecurringDepositAccountsDepositPeriodFrequency',
        'field_officer_id': 'int',
        'id': 'int',
        'interest_calculation_days_in_year_type': 'GetRecurringDepositAccountsInterestCalculationDaysInYearType',
        'interest_calculation_type': 'GetRecurringDepositAccountsInterestCalculationType',
        'interest_compounding_period_type': 'GetRecurringDepositAccountsInterestCompoundingPeriodType',
        'interest_posting_period_type': 'GetRecurringDepositAccountsInterestPostingPeriodType',
        'maturity_amount': 'float',
        'maturity_date': 'date',
        'max_deposit_term': 'int',
        'max_deposit_term_type': 'GetRecurringDepositAccountsMaxDepositTermType',
        'min_deposit_term': 'int',
        'min_deposit_term_type': 'GetRecurringDepositAccountsMinDepositTermType',
        'pre_closure_penal_applicable': 'bool',
        'recurring_deposit_amount': 'int',
        'recurring_deposit_frequency': 'int',
        'recurring_deposit_frequency_type': 'GetRecurringDepositAccountsRecurringDepositFrequencyType',
        'savings_product_id': 'int',
        'savings_product_name': 'str',
        'status': 'GetRecurringDepositAccountsStatus',
        'summary': 'GetRecurringDepositAccountsSummary',
        'timeline': 'GetRecurringDepositAccountsTimeline'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'client_id': 'clientId',
        'client_name': 'clientName',
        'currency': 'currency',
        'deposit_amount': 'depositAmount',
        'deposit_period': 'depositPeriod',
        'deposit_period_frequency': 'depositPeriodFrequency',
        'field_officer_id': 'fieldOfficerId',
        'id': 'id',
        'interest_calculation_days_in_year_type': 'interestCalculationDaysInYearType',
        'interest_calculation_type': 'interestCalculationType',
        'interest_compounding_period_type': 'interestCompoundingPeriodType',
        'interest_posting_period_type': 'interestPostingPeriodType',
        'maturity_amount': 'maturityAmount',
        'maturity_date': 'maturityDate',
        'max_deposit_term': 'maxDepositTerm',
        'max_deposit_term_type': 'maxDepositTermType',
        'min_deposit_term': 'minDepositTerm',
        'min_deposit_term_type': 'minDepositTermType',
        'pre_closure_penal_applicable': 'preClosurePenalApplicable',
        'recurring_deposit_amount': 'recurringDepositAmount',
        'recurring_deposit_frequency': 'recurringDepositFrequency',
        'recurring_deposit_frequency_type': 'recurringDepositFrequencyType',
        'savings_product_id': 'savingsProductId',
        'savings_product_name': 'savingsProductName',
        'status': 'status',
        'summary': 'summary',
        'timeline': 'timeline'
    }

    def __init__(self, account_no=None, client_id=None, client_name=None, currency=None, deposit_amount=None, deposit_period=None, deposit_period_frequency=None, field_officer_id=None, id=None, interest_calculation_days_in_year_type=None, interest_calculation_type=None, interest_compounding_period_type=None, interest_posting_period_type=None, maturity_amount=None, maturity_date=None, max_deposit_term=None, max_deposit_term_type=None, min_deposit_term=None, min_deposit_term_type=None, pre_closure_penal_applicable=None, recurring_deposit_amount=None, recurring_deposit_frequency=None, recurring_deposit_frequency_type=None, savings_product_id=None, savings_product_name=None, status=None, summary=None, timeline=None):  # noqa: E501
        """GetRecurringDepositAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._client_id = None
        self._client_name = None
        self._currency = None
        self._deposit_amount = None
        self._deposit_period = None
        self._deposit_period_frequency = None
        self._field_officer_id = None
        self._id = None
        self._interest_calculation_days_in_year_type = None
        self._interest_calculation_type = None
        self._interest_compounding_period_type = None
        self._interest_posting_period_type = None
        self._maturity_amount = None
        self._maturity_date = None
        self._max_deposit_term = None
        self._max_deposit_term_type = None
        self._min_deposit_term = None
        self._min_deposit_term_type = None
        self._pre_closure_penal_applicable = None
        self._recurring_deposit_amount = None
        self._recurring_deposit_frequency = None
        self._recurring_deposit_frequency_type = None
        self._savings_product_id = None
        self._savings_product_name = None
        self._status = None
        self._summary = None
        self._timeline = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if currency is not None:
            self.currency = currency
        if deposit_amount is not None:
            self.deposit_amount = deposit_amount
        if deposit_period is not None:
            self.deposit_period = deposit_period
        if deposit_period_frequency is not None:
            self.deposit_period_frequency = deposit_period_frequency
        if field_officer_id is not None:
            self.field_officer_id = field_officer_id
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
        if maturity_amount is not None:
            self.maturity_amount = maturity_amount
        if maturity_date is not None:
            self.maturity_date = maturity_date
        if max_deposit_term is not None:
            self.max_deposit_term = max_deposit_term
        if max_deposit_term_type is not None:
            self.max_deposit_term_type = max_deposit_term_type
        if min_deposit_term is not None:
            self.min_deposit_term = min_deposit_term
        if min_deposit_term_type is not None:
            self.min_deposit_term_type = min_deposit_term_type
        if pre_closure_penal_applicable is not None:
            self.pre_closure_penal_applicable = pre_closure_penal_applicable
        if recurring_deposit_amount is not None:
            self.recurring_deposit_amount = recurring_deposit_amount
        if recurring_deposit_frequency is not None:
            self.recurring_deposit_frequency = recurring_deposit_frequency
        if recurring_deposit_frequency_type is not None:
            self.recurring_deposit_frequency_type = recurring_deposit_frequency_type
        if savings_product_id is not None:
            self.savings_product_id = savings_product_id
        if savings_product_name is not None:
            self.savings_product_name = savings_product_name
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if timeline is not None:
            self.timeline = timeline

    @property
    def account_no(self):
        """Gets the account_no of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The account_no of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetRecurringDepositAccountsResponse.


        :param account_no: The account_no of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._account_no = account_no

    @property
    def client_id(self):
        """Gets the client_id of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The client_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetRecurringDepositAccountsResponse.


        :param client_id: The client_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The client_name of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this GetRecurringDepositAccountsResponse.


        :param client_name: The client_name of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def currency(self):
        """Gets the currency of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The currency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetRecurringDepositAccountsResponse.


        :param currency: The currency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsCurrency
        """

        self._currency = currency

    @property
    def deposit_amount(self):
        """Gets the deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: float
        """
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, deposit_amount):
        """Sets the deposit_amount of this GetRecurringDepositAccountsResponse.


        :param deposit_amount: The deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: float
        """

        self._deposit_amount = deposit_amount

    @property
    def deposit_period(self):
        """Gets the deposit_period of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The deposit_period of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._deposit_period

    @deposit_period.setter
    def deposit_period(self, deposit_period):
        """Sets the deposit_period of this GetRecurringDepositAccountsResponse.


        :param deposit_period: The deposit_period of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._deposit_period = deposit_period

    @property
    def deposit_period_frequency(self):
        """Gets the deposit_period_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The deposit_period_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsDepositPeriodFrequency
        """
        return self._deposit_period_frequency

    @deposit_period_frequency.setter
    def deposit_period_frequency(self, deposit_period_frequency):
        """Sets the deposit_period_frequency of this GetRecurringDepositAccountsResponse.


        :param deposit_period_frequency: The deposit_period_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsDepositPeriodFrequency
        """

        self._deposit_period_frequency = deposit_period_frequency

    @property
    def field_officer_id(self):
        """Gets the field_officer_id of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The field_officer_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._field_officer_id

    @field_officer_id.setter
    def field_officer_id(self, field_officer_id):
        """Sets the field_officer_id of this GetRecurringDepositAccountsResponse.


        :param field_officer_id: The field_officer_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._field_officer_id = field_officer_id

    @property
    def id(self):
        """Gets the id of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetRecurringDepositAccountsResponse.


        :param id: The id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_calculation_days_in_year_type(self):
        """Gets the interest_calculation_days_in_year_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The interest_calculation_days_in_year_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsInterestCalculationDaysInYearType
        """
        return self._interest_calculation_days_in_year_type

    @interest_calculation_days_in_year_type.setter
    def interest_calculation_days_in_year_type(self, interest_calculation_days_in_year_type):
        """Sets the interest_calculation_days_in_year_type of this GetRecurringDepositAccountsResponse.


        :param interest_calculation_days_in_year_type: The interest_calculation_days_in_year_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsInterestCalculationDaysInYearType
        """

        self._interest_calculation_days_in_year_type = interest_calculation_days_in_year_type

    @property
    def interest_calculation_type(self):
        """Gets the interest_calculation_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The interest_calculation_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsInterestCalculationType
        """
        return self._interest_calculation_type

    @interest_calculation_type.setter
    def interest_calculation_type(self, interest_calculation_type):
        """Sets the interest_calculation_type of this GetRecurringDepositAccountsResponse.


        :param interest_calculation_type: The interest_calculation_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsInterestCalculationType
        """

        self._interest_calculation_type = interest_calculation_type

    @property
    def interest_compounding_period_type(self):
        """Gets the interest_compounding_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The interest_compounding_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsInterestCompoundingPeriodType
        """
        return self._interest_compounding_period_type

    @interest_compounding_period_type.setter
    def interest_compounding_period_type(self, interest_compounding_period_type):
        """Sets the interest_compounding_period_type of this GetRecurringDepositAccountsResponse.


        :param interest_compounding_period_type: The interest_compounding_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsInterestCompoundingPeriodType
        """

        self._interest_compounding_period_type = interest_compounding_period_type

    @property
    def interest_posting_period_type(self):
        """Gets the interest_posting_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The interest_posting_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsInterestPostingPeriodType
        """
        return self._interest_posting_period_type

    @interest_posting_period_type.setter
    def interest_posting_period_type(self, interest_posting_period_type):
        """Sets the interest_posting_period_type of this GetRecurringDepositAccountsResponse.


        :param interest_posting_period_type: The interest_posting_period_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsInterestPostingPeriodType
        """

        self._interest_posting_period_type = interest_posting_period_type

    @property
    def maturity_amount(self):
        """Gets the maturity_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The maturity_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: float
        """
        return self._maturity_amount

    @maturity_amount.setter
    def maturity_amount(self, maturity_amount):
        """Sets the maturity_amount of this GetRecurringDepositAccountsResponse.


        :param maturity_amount: The maturity_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: float
        """

        self._maturity_amount = maturity_amount

    @property
    def maturity_date(self):
        """Gets the maturity_date of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The maturity_date of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: date
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this GetRecurringDepositAccountsResponse.


        :param maturity_date: The maturity_date of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: date
        """

        self._maturity_date = maturity_date

    @property
    def max_deposit_term(self):
        """Gets the max_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The max_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._max_deposit_term

    @max_deposit_term.setter
    def max_deposit_term(self, max_deposit_term):
        """Sets the max_deposit_term of this GetRecurringDepositAccountsResponse.


        :param max_deposit_term: The max_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._max_deposit_term = max_deposit_term

    @property
    def max_deposit_term_type(self):
        """Gets the max_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The max_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsMaxDepositTermType
        """
        return self._max_deposit_term_type

    @max_deposit_term_type.setter
    def max_deposit_term_type(self, max_deposit_term_type):
        """Sets the max_deposit_term_type of this GetRecurringDepositAccountsResponse.


        :param max_deposit_term_type: The max_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsMaxDepositTermType
        """

        self._max_deposit_term_type = max_deposit_term_type

    @property
    def min_deposit_term(self):
        """Gets the min_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The min_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._min_deposit_term

    @min_deposit_term.setter
    def min_deposit_term(self, min_deposit_term):
        """Sets the min_deposit_term of this GetRecurringDepositAccountsResponse.


        :param min_deposit_term: The min_deposit_term of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._min_deposit_term = min_deposit_term

    @property
    def min_deposit_term_type(self):
        """Gets the min_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The min_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsMinDepositTermType
        """
        return self._min_deposit_term_type

    @min_deposit_term_type.setter
    def min_deposit_term_type(self, min_deposit_term_type):
        """Sets the min_deposit_term_type of this GetRecurringDepositAccountsResponse.


        :param min_deposit_term_type: The min_deposit_term_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsMinDepositTermType
        """

        self._min_deposit_term_type = min_deposit_term_type

    @property
    def pre_closure_penal_applicable(self):
        """Gets the pre_closure_penal_applicable of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The pre_closure_penal_applicable of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._pre_closure_penal_applicable

    @pre_closure_penal_applicable.setter
    def pre_closure_penal_applicable(self, pre_closure_penal_applicable):
        """Sets the pre_closure_penal_applicable of this GetRecurringDepositAccountsResponse.


        :param pre_closure_penal_applicable: The pre_closure_penal_applicable of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: bool
        """

        self._pre_closure_penal_applicable = pre_closure_penal_applicable

    @property
    def recurring_deposit_amount(self):
        """Gets the recurring_deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The recurring_deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._recurring_deposit_amount

    @recurring_deposit_amount.setter
    def recurring_deposit_amount(self, recurring_deposit_amount):
        """Sets the recurring_deposit_amount of this GetRecurringDepositAccountsResponse.


        :param recurring_deposit_amount: The recurring_deposit_amount of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._recurring_deposit_amount = recurring_deposit_amount

    @property
    def recurring_deposit_frequency(self):
        """Gets the recurring_deposit_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The recurring_deposit_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._recurring_deposit_frequency

    @recurring_deposit_frequency.setter
    def recurring_deposit_frequency(self, recurring_deposit_frequency):
        """Sets the recurring_deposit_frequency of this GetRecurringDepositAccountsResponse.


        :param recurring_deposit_frequency: The recurring_deposit_frequency of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._recurring_deposit_frequency = recurring_deposit_frequency

    @property
    def recurring_deposit_frequency_type(self):
        """Gets the recurring_deposit_frequency_type of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The recurring_deposit_frequency_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsRecurringDepositFrequencyType
        """
        return self._recurring_deposit_frequency_type

    @recurring_deposit_frequency_type.setter
    def recurring_deposit_frequency_type(self, recurring_deposit_frequency_type):
        """Sets the recurring_deposit_frequency_type of this GetRecurringDepositAccountsResponse.


        :param recurring_deposit_frequency_type: The recurring_deposit_frequency_type of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsRecurringDepositFrequencyType
        """

        self._recurring_deposit_frequency_type = recurring_deposit_frequency_type

    @property
    def savings_product_id(self):
        """Gets the savings_product_id of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The savings_product_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._savings_product_id

    @savings_product_id.setter
    def savings_product_id(self, savings_product_id):
        """Sets the savings_product_id of this GetRecurringDepositAccountsResponse.


        :param savings_product_id: The savings_product_id of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: int
        """

        self._savings_product_id = savings_product_id

    @property
    def savings_product_name(self):
        """Gets the savings_product_name of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The savings_product_name of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._savings_product_name

    @savings_product_name.setter
    def savings_product_name(self, savings_product_name):
        """Sets the savings_product_name of this GetRecurringDepositAccountsResponse.


        :param savings_product_name: The savings_product_name of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: str
        """

        self._savings_product_name = savings_product_name

    @property
    def status(self):
        """Gets the status of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The status of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetRecurringDepositAccountsResponse.


        :param status: The status of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsStatus
        """

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The summary of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GetRecurringDepositAccountsResponse.


        :param summary: The summary of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsSummary
        """

        self._summary = summary

    @property
    def timeline(self):
        """Gets the timeline of this GetRecurringDepositAccountsResponse.  # noqa: E501


        :return: The timeline of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :rtype: GetRecurringDepositAccountsTimeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this GetRecurringDepositAccountsResponse.


        :param timeline: The timeline of this GetRecurringDepositAccountsResponse.  # noqa: E501
        :type: GetRecurringDepositAccountsTimeline
        """

        self._timeline = timeline

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
        if issubclass(GetRecurringDepositAccountsResponse, dict):
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
        if not isinstance(other, GetRecurringDepositAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
