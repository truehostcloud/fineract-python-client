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

class GetSelfSavingsAccountsResponse(object):
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
        'currency': 'GetSelfSavingsCurrency',
        'field_officer_id': 'int',
        'id': 'int',
        'interest_calculation_days_in_year_type': 'GetSelfSavingsInterestCalculationDaysInYearType',
        'interest_calculation_type': 'GetSelfSavingsInterestCalculationType',
        'interest_compounding_period_type': 'GetSelfSavingsInterestCompoundingPeriodType',
        'interest_posting_period_type': 'GetSelfSavingsInterestPostingPeriodType',
        'nominal_annual_interest_rate': 'float',
        'savings_product_id': 'int',
        'savings_product_name': 'str',
        'status': 'GetSelfSavingsStatus',
        'summary': 'GetSelfSavingsSummary',
        'timeline': 'GetSelfSavingsTimeline'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'client_id': 'clientId',
        'client_name': 'clientName',
        'currency': 'currency',
        'field_officer_id': 'fieldOfficerId',
        'id': 'id',
        'interest_calculation_days_in_year_type': 'interestCalculationDaysInYearType',
        'interest_calculation_type': 'interestCalculationType',
        'interest_compounding_period_type': 'interestCompoundingPeriodType',
        'interest_posting_period_type': 'interestPostingPeriodType',
        'nominal_annual_interest_rate': 'nominalAnnualInterestRate',
        'savings_product_id': 'savingsProductId',
        'savings_product_name': 'savingsProductName',
        'status': 'status',
        'summary': 'summary',
        'timeline': 'timeline'
    }

    def __init__(self, account_no=None, client_id=None, client_name=None, currency=None, field_officer_id=None, id=None, interest_calculation_days_in_year_type=None, interest_calculation_type=None, interest_compounding_period_type=None, interest_posting_period_type=None, nominal_annual_interest_rate=None, savings_product_id=None, savings_product_name=None, status=None, summary=None, timeline=None):  # noqa: E501
        """GetSelfSavingsAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._client_id = None
        self._client_name = None
        self._currency = None
        self._field_officer_id = None
        self._id = None
        self._interest_calculation_days_in_year_type = None
        self._interest_calculation_type = None
        self._interest_compounding_period_type = None
        self._interest_posting_period_type = None
        self._nominal_annual_interest_rate = None
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
        if nominal_annual_interest_rate is not None:
            self.nominal_annual_interest_rate = nominal_annual_interest_rate
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
        """Gets the account_no of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The account_no of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetSelfSavingsAccountsResponse.


        :param account_no: The account_no of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._account_no = account_no

    @property
    def client_id(self):
        """Gets the client_id of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The client_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetSelfSavingsAccountsResponse.


        :param client_id: The client_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The client_name of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this GetSelfSavingsAccountsResponse.


        :param client_name: The client_name of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def currency(self):
        """Gets the currency of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The currency of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetSelfSavingsAccountsResponse.


        :param currency: The currency of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsCurrency
        """

        self._currency = currency

    @property
    def field_officer_id(self):
        """Gets the field_officer_id of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The field_officer_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._field_officer_id

    @field_officer_id.setter
    def field_officer_id(self, field_officer_id):
        """Sets the field_officer_id of this GetSelfSavingsAccountsResponse.


        :param field_officer_id: The field_officer_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._field_officer_id = field_officer_id

    @property
    def id(self):
        """Gets the id of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSelfSavingsAccountsResponse.


        :param id: The id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_calculation_days_in_year_type(self):
        """Gets the interest_calculation_days_in_year_type of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The interest_calculation_days_in_year_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsInterestCalculationDaysInYearType
        """
        return self._interest_calculation_days_in_year_type

    @interest_calculation_days_in_year_type.setter
    def interest_calculation_days_in_year_type(self, interest_calculation_days_in_year_type):
        """Sets the interest_calculation_days_in_year_type of this GetSelfSavingsAccountsResponse.


        :param interest_calculation_days_in_year_type: The interest_calculation_days_in_year_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsInterestCalculationDaysInYearType
        """

        self._interest_calculation_days_in_year_type = interest_calculation_days_in_year_type

    @property
    def interest_calculation_type(self):
        """Gets the interest_calculation_type of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The interest_calculation_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsInterestCalculationType
        """
        return self._interest_calculation_type

    @interest_calculation_type.setter
    def interest_calculation_type(self, interest_calculation_type):
        """Sets the interest_calculation_type of this GetSelfSavingsAccountsResponse.


        :param interest_calculation_type: The interest_calculation_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsInterestCalculationType
        """

        self._interest_calculation_type = interest_calculation_type

    @property
    def interest_compounding_period_type(self):
        """Gets the interest_compounding_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The interest_compounding_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsInterestCompoundingPeriodType
        """
        return self._interest_compounding_period_type

    @interest_compounding_period_type.setter
    def interest_compounding_period_type(self, interest_compounding_period_type):
        """Sets the interest_compounding_period_type of this GetSelfSavingsAccountsResponse.


        :param interest_compounding_period_type: The interest_compounding_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsInterestCompoundingPeriodType
        """

        self._interest_compounding_period_type = interest_compounding_period_type

    @property
    def interest_posting_period_type(self):
        """Gets the interest_posting_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The interest_posting_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsInterestPostingPeriodType
        """
        return self._interest_posting_period_type

    @interest_posting_period_type.setter
    def interest_posting_period_type(self, interest_posting_period_type):
        """Sets the interest_posting_period_type of this GetSelfSavingsAccountsResponse.


        :param interest_posting_period_type: The interest_posting_period_type of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsInterestPostingPeriodType
        """

        self._interest_posting_period_type = interest_posting_period_type

    @property
    def nominal_annual_interest_rate(self):
        """Gets the nominal_annual_interest_rate of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The nominal_annual_interest_rate of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: float
        """
        return self._nominal_annual_interest_rate

    @nominal_annual_interest_rate.setter
    def nominal_annual_interest_rate(self, nominal_annual_interest_rate):
        """Sets the nominal_annual_interest_rate of this GetSelfSavingsAccountsResponse.


        :param nominal_annual_interest_rate: The nominal_annual_interest_rate of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: float
        """

        self._nominal_annual_interest_rate = nominal_annual_interest_rate

    @property
    def savings_product_id(self):
        """Gets the savings_product_id of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The savings_product_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._savings_product_id

    @savings_product_id.setter
    def savings_product_id(self, savings_product_id):
        """Sets the savings_product_id of this GetSelfSavingsAccountsResponse.


        :param savings_product_id: The savings_product_id of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._savings_product_id = savings_product_id

    @property
    def savings_product_name(self):
        """Gets the savings_product_name of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The savings_product_name of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._savings_product_name

    @savings_product_name.setter
    def savings_product_name(self, savings_product_name):
        """Sets the savings_product_name of this GetSelfSavingsAccountsResponse.


        :param savings_product_name: The savings_product_name of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: str
        """

        self._savings_product_name = savings_product_name

    @property
    def status(self):
        """Gets the status of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The status of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetSelfSavingsAccountsResponse.


        :param status: The status of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsStatus
        """

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The summary of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this GetSelfSavingsAccountsResponse.


        :param summary: The summary of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsSummary
        """

        self._summary = summary

    @property
    def timeline(self):
        """Gets the timeline of this GetSelfSavingsAccountsResponse.  # noqa: E501


        :return: The timeline of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :rtype: GetSelfSavingsTimeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this GetSelfSavingsAccountsResponse.


        :param timeline: The timeline of this GetSelfSavingsAccountsResponse.  # noqa: E501
        :type: GetSelfSavingsTimeline
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
        if issubclass(GetSelfSavingsAccountsResponse, dict):
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
        if not isinstance(other, GetSelfSavingsAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
