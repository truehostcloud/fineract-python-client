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

class IdDocument(object):
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
        'id_number': 'str',
        'id_type': 'str',
        'issuer_country': 'str',
        'other_id_description': 'str'
    }

    attribute_map = {
        'id_number': 'idNumber',
        'id_type': 'idType',
        'issuer_country': 'issuerCountry',
        'other_id_description': 'otherIdDescription'
    }

    def __init__(self, id_number=None, id_type=None, issuer_country=None, other_id_description=None):  # noqa: E501
        """IdDocument - a model defined in Swagger"""  # noqa: E501
        self._id_number = None
        self._id_type = None
        self._issuer_country = None
        self._other_id_description = None
        self.discriminator = None
        if id_number is not None:
            self.id_number = id_number
        if id_type is not None:
            self.id_type = id_type
        if issuer_country is not None:
            self.issuer_country = issuer_country
        if other_id_description is not None:
            self.other_id_description = other_id_description

    @property
    def id_number(self):
        """Gets the id_number of this IdDocument.  # noqa: E501


        :return: The id_number of this IdDocument.  # noqa: E501
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this IdDocument.


        :param id_number: The id_number of this IdDocument.  # noqa: E501
        :type: str
        """

        self._id_number = id_number

    @property
    def id_type(self):
        """Gets the id_type of this IdDocument.  # noqa: E501


        :return: The id_type of this IdDocument.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this IdDocument.


        :param id_type: The id_type of this IdDocument.  # noqa: E501
        :type: str
        """

        self._id_type = id_type

    @property
    def issuer_country(self):
        """Gets the issuer_country of this IdDocument.  # noqa: E501


        :return: The issuer_country of this IdDocument.  # noqa: E501
        :rtype: str
        """
        return self._issuer_country

    @issuer_country.setter
    def issuer_country(self, issuer_country):
        """Sets the issuer_country of this IdDocument.


        :param issuer_country: The issuer_country of this IdDocument.  # noqa: E501
        :type: str
        """

        self._issuer_country = issuer_country

    @property
    def other_id_description(self):
        """Gets the other_id_description of this IdDocument.  # noqa: E501


        :return: The other_id_description of this IdDocument.  # noqa: E501
        :rtype: str
        """
        return self._other_id_description

    @other_id_description.setter
    def other_id_description(self, other_id_description):
        """Sets the other_id_description of this IdDocument.


        :param other_id_description: The other_id_description of this IdDocument.  # noqa: E501
        :type: str
        """

        self._other_id_description = other_id_description

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
        if issubclass(IdDocument, dict):
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
        if not isinstance(other, IdDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
