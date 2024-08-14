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

class GetDelinquencyTagHistoryResponse(object):
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
        'added_on_date': 'date',
        'delinquency_range': 'GetDelinquencyRangesResponse',
        'id': 'int',
        'lifted_on_date': 'date',
        'loan_id': 'int'
    }

    attribute_map = {
        'added_on_date': 'addedOnDate',
        'delinquency_range': 'delinquencyRange',
        'id': 'id',
        'lifted_on_date': 'liftedOnDate',
        'loan_id': 'loanId'
    }

    def __init__(self, added_on_date=None, delinquency_range=None, id=None, lifted_on_date=None, loan_id=None):  # noqa: E501
        """GetDelinquencyTagHistoryResponse - a model defined in Swagger"""  # noqa: E501
        self._added_on_date = None
        self._delinquency_range = None
        self._id = None
        self._lifted_on_date = None
        self._loan_id = None
        self.discriminator = None
        if added_on_date is not None:
            self.added_on_date = added_on_date
        if delinquency_range is not None:
            self.delinquency_range = delinquency_range
        if id is not None:
            self.id = id
        if lifted_on_date is not None:
            self.lifted_on_date = lifted_on_date
        if loan_id is not None:
            self.loan_id = loan_id

    @property
    def added_on_date(self):
        """Gets the added_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501


        :return: The added_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :rtype: date
        """
        return self._added_on_date

    @added_on_date.setter
    def added_on_date(self, added_on_date):
        """Sets the added_on_date of this GetDelinquencyTagHistoryResponse.


        :param added_on_date: The added_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :type: date
        """

        self._added_on_date = added_on_date

    @property
    def delinquency_range(self):
        """Gets the delinquency_range of this GetDelinquencyTagHistoryResponse.  # noqa: E501


        :return: The delinquency_range of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :rtype: GetDelinquencyRangesResponse
        """
        return self._delinquency_range

    @delinquency_range.setter
    def delinquency_range(self, delinquency_range):
        """Sets the delinquency_range of this GetDelinquencyTagHistoryResponse.


        :param delinquency_range: The delinquency_range of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :type: GetDelinquencyRangesResponse
        """

        self._delinquency_range = delinquency_range

    @property
    def id(self):
        """Gets the id of this GetDelinquencyTagHistoryResponse.  # noqa: E501


        :return: The id of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetDelinquencyTagHistoryResponse.


        :param id: The id of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lifted_on_date(self):
        """Gets the lifted_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501


        :return: The lifted_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :rtype: date
        """
        return self._lifted_on_date

    @lifted_on_date.setter
    def lifted_on_date(self, lifted_on_date):
        """Sets the lifted_on_date of this GetDelinquencyTagHistoryResponse.


        :param lifted_on_date: The lifted_on_date of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :type: date
        """

        self._lifted_on_date = lifted_on_date

    @property
    def loan_id(self):
        """Gets the loan_id of this GetDelinquencyTagHistoryResponse.  # noqa: E501


        :return: The loan_id of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this GetDelinquencyTagHistoryResponse.


        :param loan_id: The loan_id of this GetDelinquencyTagHistoryResponse.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

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
        if issubclass(GetDelinquencyTagHistoryResponse, dict):
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
        if not isinstance(other, GetDelinquencyTagHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
