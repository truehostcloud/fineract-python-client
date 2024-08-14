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

class GlobalConfigurationPropertyData(object):
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
        'date_value': 'date',
        'description': 'str',
        'enabled': 'bool',
        'id': 'int',
        'name': 'str',
        'string_value': 'str',
        'trap_door': 'bool',
        'value': 'int'
    }

    attribute_map = {
        'date_value': 'dateValue',
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'string_value': 'stringValue',
        'trap_door': 'trapDoor',
        'value': 'value'
    }

    def __init__(self, date_value=None, description=None, enabled=None, id=None, name=None, string_value=None, trap_door=None, value=None):  # noqa: E501
        """GlobalConfigurationPropertyData - a model defined in Swagger"""  # noqa: E501
        self._date_value = None
        self._description = None
        self._enabled = None
        self._id = None
        self._name = None
        self._string_value = None
        self._trap_door = None
        self._value = None
        self.discriminator = None
        if date_value is not None:
            self.date_value = date_value
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if string_value is not None:
            self.string_value = string_value
        if trap_door is not None:
            self.trap_door = trap_door
        if value is not None:
            self.value = value

    @property
    def date_value(self):
        """Gets the date_value of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The date_value of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: date
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this GlobalConfigurationPropertyData.


        :param date_value: The date_value of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: date
        """

        self._date_value = date_value

    @property
    def description(self):
        """Gets the description of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The description of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GlobalConfigurationPropertyData.


        :param description: The description of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The enabled of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GlobalConfigurationPropertyData.


        :param enabled: The enabled of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The id of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalConfigurationPropertyData.


        :param id: The id of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The name of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalConfigurationPropertyData.


        :param name: The name of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def string_value(self):
        """Gets the string_value of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The string_value of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this GlobalConfigurationPropertyData.


        :param string_value: The string_value of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def trap_door(self):
        """Gets the trap_door of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The trap_door of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: bool
        """
        return self._trap_door

    @trap_door.setter
    def trap_door(self, trap_door):
        """Sets the trap_door of this GlobalConfigurationPropertyData.


        :param trap_door: The trap_door of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: bool
        """

        self._trap_door = trap_door

    @property
    def value(self):
        """Gets the value of this GlobalConfigurationPropertyData.  # noqa: E501


        :return: The value of this GlobalConfigurationPropertyData.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GlobalConfigurationPropertyData.


        :param value: The value of this GlobalConfigurationPropertyData.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if issubclass(GlobalConfigurationPropertyData, dict):
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
        if not isinstance(other, GlobalConfigurationPropertyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
