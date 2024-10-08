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

class PostFixedDepositProductsCharts(object):
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
        'chart_slabs': 'list[PostFixedDepositProductsChartSlabs]',
        'date_format': 'str',
        'from_date': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'chart_slabs': 'chartSlabs',
        'date_format': 'dateFormat',
        'from_date': 'fromDate',
        'locale': 'locale'
    }

    def __init__(self, chart_slabs=None, date_format=None, from_date=None, locale=None):  # noqa: E501
        """PostFixedDepositProductsCharts - a model defined in Swagger"""  # noqa: E501
        self._chart_slabs = None
        self._date_format = None
        self._from_date = None
        self._locale = None
        self.discriminator = None
        if chart_slabs is not None:
            self.chart_slabs = chart_slabs
        if date_format is not None:
            self.date_format = date_format
        if from_date is not None:
            self.from_date = from_date
        if locale is not None:
            self.locale = locale

    @property
    def chart_slabs(self):
        """Gets the chart_slabs of this PostFixedDepositProductsCharts.  # noqa: E501


        :return: The chart_slabs of this PostFixedDepositProductsCharts.  # noqa: E501
        :rtype: list[PostFixedDepositProductsChartSlabs]
        """
        return self._chart_slabs

    @chart_slabs.setter
    def chart_slabs(self, chart_slabs):
        """Sets the chart_slabs of this PostFixedDepositProductsCharts.


        :param chart_slabs: The chart_slabs of this PostFixedDepositProductsCharts.  # noqa: E501
        :type: list[PostFixedDepositProductsChartSlabs]
        """

        self._chart_slabs = chart_slabs

    @property
    def date_format(self):
        """Gets the date_format of this PostFixedDepositProductsCharts.  # noqa: E501


        :return: The date_format of this PostFixedDepositProductsCharts.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostFixedDepositProductsCharts.


        :param date_format: The date_format of this PostFixedDepositProductsCharts.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def from_date(self):
        """Gets the from_date of this PostFixedDepositProductsCharts.  # noqa: E501


        :return: The from_date of this PostFixedDepositProductsCharts.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this PostFixedDepositProductsCharts.


        :param from_date: The from_date of this PostFixedDepositProductsCharts.  # noqa: E501
        :type: str
        """

        self._from_date = from_date

    @property
    def locale(self):
        """Gets the locale of this PostFixedDepositProductsCharts.  # noqa: E501


        :return: The locale of this PostFixedDepositProductsCharts.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostFixedDepositProductsCharts.


        :param locale: The locale of this PostFixedDepositProductsCharts.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(PostFixedDepositProductsCharts, dict):
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
        if not isinstance(other, PostFixedDepositProductsCharts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
