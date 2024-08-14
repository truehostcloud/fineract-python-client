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

class ComponentData(object):
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
        'description': 'str',
        'id': 'int',
        'key': 'str',
        'sequence_no': 'int',
        'text': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'key': 'key',
        'sequence_no': 'sequenceNo',
        'text': 'text'
    }

    def __init__(self, description=None, id=None, key=None, sequence_no=None, text=None):  # noqa: E501
        """ComponentData - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._id = None
        self._key = None
        self._sequence_no = None
        self._text = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if sequence_no is not None:
            self.sequence_no = sequence_no
        if text is not None:
            self.text = text

    @property
    def description(self):
        """Gets the description of this ComponentData.  # noqa: E501


        :return: The description of this ComponentData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentData.


        :param description: The description of this ComponentData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ComponentData.  # noqa: E501


        :return: The id of this ComponentData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentData.


        :param id: The id of this ComponentData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this ComponentData.  # noqa: E501


        :return: The key of this ComponentData.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ComponentData.


        :param key: The key of this ComponentData.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def sequence_no(self):
        """Gets the sequence_no of this ComponentData.  # noqa: E501


        :return: The sequence_no of this ComponentData.  # noqa: E501
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        """Sets the sequence_no of this ComponentData.


        :param sequence_no: The sequence_no of this ComponentData.  # noqa: E501
        :type: int
        """

        self._sequence_no = sequence_no

    @property
    def text(self):
        """Gets the text of this ComponentData.  # noqa: E501


        :return: The text of this ComponentData.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ComponentData.


        :param text: The text of this ComponentData.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(ComponentData, dict):
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
        if not isinstance(other, ComponentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
