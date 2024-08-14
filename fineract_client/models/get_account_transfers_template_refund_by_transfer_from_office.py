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

class GetAccountTransfersTemplateRefundByTransferFromOffice(object):
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
        'external_id': 'str',
        'hierarchy': 'str',
        'id': 'int',
        'name': 'str',
        'name_decorated': 'str',
        'opening_date': 'date'
    }

    attribute_map = {
        'external_id': 'externalId',
        'hierarchy': 'hierarchy',
        'id': 'id',
        'name': 'name',
        'name_decorated': 'nameDecorated',
        'opening_date': 'openingDate'
    }

    def __init__(self, external_id=None, hierarchy=None, id=None, name=None, name_decorated=None, opening_date=None):  # noqa: E501
        """GetAccountTransfersTemplateRefundByTransferFromOffice - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._hierarchy = None
        self._id = None
        self._name = None
        self._name_decorated = None
        self._opening_date = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if hierarchy is not None:
            self.hierarchy = hierarchy
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_decorated is not None:
            self.name_decorated = name_decorated
        if opening_date is not None:
            self.opening_date = opening_date

    @property
    def external_id(self):
        """Gets the external_id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The external_id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param external_id: The external_id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def hierarchy(self):
        """Gets the hierarchy of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The hierarchy of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: str
        """
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        """Sets the hierarchy of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param hierarchy: The hierarchy of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: str
        """

        self._hierarchy = hierarchy

    @property
    def id(self):
        """Gets the id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param id: The id of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The name of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param name: The name of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_decorated(self):
        """Gets the name_decorated of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The name_decorated of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: str
        """
        return self._name_decorated

    @name_decorated.setter
    def name_decorated(self, name_decorated):
        """Sets the name_decorated of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param name_decorated: The name_decorated of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: str
        """

        self._name_decorated = name_decorated

    @property
    def opening_date(self):
        """Gets the opening_date of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501


        :return: The opening_date of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :rtype: date
        """
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        """Sets the opening_date of this GetAccountTransfersTemplateRefundByTransferFromOffice.


        :param opening_date: The opening_date of this GetAccountTransfersTemplateRefundByTransferFromOffice.  # noqa: E501
        :type: date
        """

        self._opening_date = opening_date

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
        if issubclass(GetAccountTransfersTemplateRefundByTransferFromOffice, dict):
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
        if not isinstance(other, GetAccountTransfersTemplateRefundByTransferFromOffice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
