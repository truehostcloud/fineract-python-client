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

class GetStandingInstructionHistoryPageItemsFromClient(object):
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
        'display_name': 'str',
        'id': 'int',
        'office_id': 'int',
        'office_name': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'office_id': 'officeId',
        'office_name': 'officeName'
    }

    def __init__(self, display_name=None, id=None, office_id=None, office_name=None):  # noqa: E501
        """GetStandingInstructionHistoryPageItemsFromClient - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._id = None
        self._office_id = None
        self._office_name = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name

    @property
    def display_name(self):
        """Gets the display_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501


        :return: The display_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetStandingInstructionHistoryPageItemsFromClient.


        :param display_name: The display_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501


        :return: The id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetStandingInstructionHistoryPageItemsFromClient.


        :param id: The id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def office_id(self):
        """Gets the office_id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501


        :return: The office_id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetStandingInstructionHistoryPageItemsFromClient.


        :param office_id: The office_id of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501


        :return: The office_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetStandingInstructionHistoryPageItemsFromClient.


        :param office_name: The office_name of this GetStandingInstructionHistoryPageItemsFromClient.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

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
        if issubclass(GetStandingInstructionHistoryPageItemsFromClient, dict):
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
        if not isinstance(other, GetStandingInstructionHistoryPageItemsFromClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
