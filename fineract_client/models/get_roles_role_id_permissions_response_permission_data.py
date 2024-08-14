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

class GetRolesRoleIdPermissionsResponsePermissionData(object):
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
        'action_name': 'str',
        'code': 'str',
        'entity_name': 'str',
        'grouping': 'str',
        'selected': 'bool'
    }

    attribute_map = {
        'action_name': 'actionName',
        'code': 'code',
        'entity_name': 'entityName',
        'grouping': 'grouping',
        'selected': 'selected'
    }

    def __init__(self, action_name=None, code=None, entity_name=None, grouping=None, selected=None):  # noqa: E501
        """GetRolesRoleIdPermissionsResponsePermissionData - a model defined in Swagger"""  # noqa: E501
        self._action_name = None
        self._code = None
        self._entity_name = None
        self._grouping = None
        self._selected = None
        self.discriminator = None
        if action_name is not None:
            self.action_name = action_name
        if code is not None:
            self.code = code
        if entity_name is not None:
            self.entity_name = entity_name
        if grouping is not None:
            self.grouping = grouping
        if selected is not None:
            self.selected = selected

    @property
    def action_name(self):
        """Gets the action_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501


        :return: The action_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this GetRolesRoleIdPermissionsResponsePermissionData.


        :param action_name: The action_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def code(self):
        """Gets the code of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501


        :return: The code of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetRolesRoleIdPermissionsResponsePermissionData.


        :param code: The code of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def entity_name(self):
        """Gets the entity_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501


        :return: The entity_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this GetRolesRoleIdPermissionsResponsePermissionData.


        :param entity_name: The entity_name of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def grouping(self):
        """Gets the grouping of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501


        :return: The grouping of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :rtype: str
        """
        return self._grouping

    @grouping.setter
    def grouping(self, grouping):
        """Sets the grouping of this GetRolesRoleIdPermissionsResponsePermissionData.


        :param grouping: The grouping of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :type: str
        """

        self._grouping = grouping

    @property
    def selected(self):
        """Gets the selected of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501


        :return: The selected of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this GetRolesRoleIdPermissionsResponsePermissionData.


        :param selected: The selected of this GetRolesRoleIdPermissionsResponsePermissionData.  # noqa: E501
        :type: bool
        """

        self._selected = selected

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
        if issubclass(GetRolesRoleIdPermissionsResponsePermissionData, dict):
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
        if not isinstance(other, GetRolesRoleIdPermissionsResponsePermissionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
