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

class RescheduleReasonsCodeValue(object):
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
        'active': 'bool',
        'id': 'int',
        'mandatory': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'active': 'active',
        'id': 'id',
        'mandatory': 'mandatory',
        'name': 'name'
    }

    def __init__(self, active=None, id=None, mandatory=None, name=None):  # noqa: E501
        """RescheduleReasonsCodeValue - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._id = None
        self._mandatory = None
        self._name = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if id is not None:
            self.id = id
        if mandatory is not None:
            self.mandatory = mandatory
        if name is not None:
            self.name = name

    @property
    def active(self):
        """Gets the active of this RescheduleReasonsCodeValue.  # noqa: E501


        :return: The active of this RescheduleReasonsCodeValue.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RescheduleReasonsCodeValue.


        :param active: The active of this RescheduleReasonsCodeValue.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def id(self):
        """Gets the id of this RescheduleReasonsCodeValue.  # noqa: E501


        :return: The id of this RescheduleReasonsCodeValue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RescheduleReasonsCodeValue.


        :param id: The id of this RescheduleReasonsCodeValue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mandatory(self):
        """Gets the mandatory of this RescheduleReasonsCodeValue.  # noqa: E501


        :return: The mandatory of this RescheduleReasonsCodeValue.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this RescheduleReasonsCodeValue.


        :param mandatory: The mandatory of this RescheduleReasonsCodeValue.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def name(self):
        """Gets the name of this RescheduleReasonsCodeValue.  # noqa: E501


        :return: The name of this RescheduleReasonsCodeValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RescheduleReasonsCodeValue.


        :param name: The name of this RescheduleReasonsCodeValue.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(RescheduleReasonsCodeValue, dict):
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
        if not isinstance(other, RescheduleReasonsCodeValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
