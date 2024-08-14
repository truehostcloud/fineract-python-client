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

class GetSavingsAccountsResponse(object):
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
        'page_items': 'list[GetSavingsPageItems]',
        'total_filtered_records': 'int'
    }

    attribute_map = {
        'page_items': 'pageItems',
        'total_filtered_records': 'totalFilteredRecords'
    }

    def __init__(self, page_items=None, total_filtered_records=None):  # noqa: E501
        """GetSavingsAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._page_items = None
        self._total_filtered_records = None
        self.discriminator = None
        if page_items is not None:
            self.page_items = page_items
        if total_filtered_records is not None:
            self.total_filtered_records = total_filtered_records

    @property
    def page_items(self):
        """Gets the page_items of this GetSavingsAccountsResponse.  # noqa: E501


        :return: The page_items of this GetSavingsAccountsResponse.  # noqa: E501
        :rtype: list[GetSavingsPageItems]
        """
        return self._page_items

    @page_items.setter
    def page_items(self, page_items):
        """Sets the page_items of this GetSavingsAccountsResponse.


        :param page_items: The page_items of this GetSavingsAccountsResponse.  # noqa: E501
        :type: list[GetSavingsPageItems]
        """

        self._page_items = page_items

    @property
    def total_filtered_records(self):
        """Gets the total_filtered_records of this GetSavingsAccountsResponse.  # noqa: E501


        :return: The total_filtered_records of this GetSavingsAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_filtered_records

    @total_filtered_records.setter
    def total_filtered_records(self, total_filtered_records):
        """Sets the total_filtered_records of this GetSavingsAccountsResponse.


        :param total_filtered_records: The total_filtered_records of this GetSavingsAccountsResponse.  # noqa: E501
        :type: int
        """

        self._total_filtered_records = total_filtered_records

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
        if issubclass(GetSavingsAccountsResponse, dict):
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
        if not isinstance(other, GetSavingsAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
