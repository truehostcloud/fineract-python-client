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

class PostGLAccountsRequest(object):
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
        'gl_code': 'str',
        'manual_entries_allowed': 'bool',
        'name': 'str',
        'parent_id': 'int',
        'tag_id': 'int',
        'type': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'description': 'description',
        'gl_code': 'glCode',
        'manual_entries_allowed': 'manualEntriesAllowed',
        'name': 'name',
        'parent_id': 'parentId',
        'tag_id': 'tagId',
        'type': 'type',
        'usage': 'usage'
    }

    def __init__(self, description=None, gl_code=None, manual_entries_allowed=None, name=None, parent_id=None, tag_id=None, type=None, usage=None):  # noqa: E501
        """PostGLAccountsRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._gl_code = None
        self._manual_entries_allowed = None
        self._name = None
        self._parent_id = None
        self._tag_id = None
        self._type = None
        self._usage = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if gl_code is not None:
            self.gl_code = gl_code
        if manual_entries_allowed is not None:
            self.manual_entries_allowed = manual_entries_allowed
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if tag_id is not None:
            self.tag_id = tag_id
        if type is not None:
            self.type = type
        if usage is not None:
            self.usage = usage

    @property
    def description(self):
        """Gets the description of this PostGLAccountsRequest.  # noqa: E501


        :return: The description of this PostGLAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostGLAccountsRequest.


        :param description: The description of this PostGLAccountsRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gl_code(self):
        """Gets the gl_code of this PostGLAccountsRequest.  # noqa: E501


        :return: The gl_code of this PostGLAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._gl_code

    @gl_code.setter
    def gl_code(self, gl_code):
        """Sets the gl_code of this PostGLAccountsRequest.


        :param gl_code: The gl_code of this PostGLAccountsRequest.  # noqa: E501
        :type: str
        """

        self._gl_code = gl_code

    @property
    def manual_entries_allowed(self):
        """Gets the manual_entries_allowed of this PostGLAccountsRequest.  # noqa: E501


        :return: The manual_entries_allowed of this PostGLAccountsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._manual_entries_allowed

    @manual_entries_allowed.setter
    def manual_entries_allowed(self, manual_entries_allowed):
        """Sets the manual_entries_allowed of this PostGLAccountsRequest.


        :param manual_entries_allowed: The manual_entries_allowed of this PostGLAccountsRequest.  # noqa: E501
        :type: bool
        """

        self._manual_entries_allowed = manual_entries_allowed

    @property
    def name(self):
        """Gets the name of this PostGLAccountsRequest.  # noqa: E501


        :return: The name of this PostGLAccountsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostGLAccountsRequest.


        :param name: The name of this PostGLAccountsRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this PostGLAccountsRequest.  # noqa: E501


        :return: The parent_id of this PostGLAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this PostGLAccountsRequest.


        :param parent_id: The parent_id of this PostGLAccountsRequest.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def tag_id(self):
        """Gets the tag_id of this PostGLAccountsRequest.  # noqa: E501


        :return: The tag_id of this PostGLAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this PostGLAccountsRequest.


        :param tag_id: The tag_id of this PostGLAccountsRequest.  # noqa: E501
        :type: int
        """

        self._tag_id = tag_id

    @property
    def type(self):
        """Gets the type of this PostGLAccountsRequest.  # noqa: E501


        :return: The type of this PostGLAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostGLAccountsRequest.


        :param type: The type of this PostGLAccountsRequest.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def usage(self):
        """Gets the usage of this PostGLAccountsRequest.  # noqa: E501


        :return: The usage of this PostGLAccountsRequest.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this PostGLAccountsRequest.


        :param usage: The usage of this PostGLAccountsRequest.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if issubclass(PostGLAccountsRequest, dict):
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
        if not isinstance(other, PostGLAccountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
