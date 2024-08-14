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

class GetRecurringDepositProductsProductIdActiveChart(object):
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
        'chart_slabs': 'list[GetRecurringDepositProductsProductIdChartSlabs]',
        'from_date': 'date',
        'id': 'int',
        'period_types': 'list[GetRecurringDepositProductsProductIdPeriodType]',
        'savings_product_id': 'int',
        'savings_product_name': 'str'
    }

    attribute_map = {
        'chart_slabs': 'chartSlabs',
        'from_date': 'fromDate',
        'id': 'id',
        'period_types': 'periodTypes',
        'savings_product_id': 'savingsProductId',
        'savings_product_name': 'savingsProductName'
    }

    def __init__(self, chart_slabs=None, from_date=None, id=None, period_types=None, savings_product_id=None, savings_product_name=None):  # noqa: E501
        """GetRecurringDepositProductsProductIdActiveChart - a model defined in Swagger"""  # noqa: E501
        self._chart_slabs = None
        self._from_date = None
        self._id = None
        self._period_types = None
        self._savings_product_id = None
        self._savings_product_name = None
        self.discriminator = None
        if chart_slabs is not None:
            self.chart_slabs = chart_slabs
        if from_date is not None:
            self.from_date = from_date
        if id is not None:
            self.id = id
        if period_types is not None:
            self.period_types = period_types
        if savings_product_id is not None:
            self.savings_product_id = savings_product_id
        if savings_product_name is not None:
            self.savings_product_name = savings_product_name

    @property
    def chart_slabs(self):
        """Gets the chart_slabs of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The chart_slabs of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: list[GetRecurringDepositProductsProductIdChartSlabs]
        """
        return self._chart_slabs

    @chart_slabs.setter
    def chart_slabs(self, chart_slabs):
        """Sets the chart_slabs of this GetRecurringDepositProductsProductIdActiveChart.


        :param chart_slabs: The chart_slabs of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: list[GetRecurringDepositProductsProductIdChartSlabs]
        """

        self._chart_slabs = chart_slabs

    @property
    def from_date(self):
        """Gets the from_date of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The from_date of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this GetRecurringDepositProductsProductIdActiveChart.


        :param from_date: The from_date of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: date
        """

        self._from_date = from_date

    @property
    def id(self):
        """Gets the id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetRecurringDepositProductsProductIdActiveChart.


        :param id: The id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def period_types(self):
        """Gets the period_types of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The period_types of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: list[GetRecurringDepositProductsProductIdPeriodType]
        """
        return self._period_types

    @period_types.setter
    def period_types(self, period_types):
        """Sets the period_types of this GetRecurringDepositProductsProductIdActiveChart.


        :param period_types: The period_types of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: list[GetRecurringDepositProductsProductIdPeriodType]
        """

        self._period_types = period_types

    @property
    def savings_product_id(self):
        """Gets the savings_product_id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The savings_product_id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: int
        """
        return self._savings_product_id

    @savings_product_id.setter
    def savings_product_id(self, savings_product_id):
        """Sets the savings_product_id of this GetRecurringDepositProductsProductIdActiveChart.


        :param savings_product_id: The savings_product_id of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: int
        """

        self._savings_product_id = savings_product_id

    @property
    def savings_product_name(self):
        """Gets the savings_product_name of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501


        :return: The savings_product_name of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :rtype: str
        """
        return self._savings_product_name

    @savings_product_name.setter
    def savings_product_name(self, savings_product_name):
        """Sets the savings_product_name of this GetRecurringDepositProductsProductIdActiveChart.


        :param savings_product_name: The savings_product_name of this GetRecurringDepositProductsProductIdActiveChart.  # noqa: E501
        :type: str
        """

        self._savings_product_name = savings_product_name

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
        if issubclass(GetRecurringDepositProductsProductIdActiveChart, dict):
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
        if not isinstance(other, GetRecurringDepositProductsProductIdActiveChart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
