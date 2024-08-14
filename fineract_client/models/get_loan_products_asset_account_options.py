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

class GetLoanProductsAssetAccountOptions(object):
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
        'disabled': 'bool',
        'gl_code': 'str',
        'id': 'int',
        'manual_entries_allowed': 'bool',
        'name': 'str',
        'name_decorated': 'str',
        'organization_running_balance': 'int',
        'tag_id': 'GetLoanProductsLiabilityTagId',
        'type': 'GetLoanProductsLiabilityType',
        'usage': 'GetLoanProductsLiabilityUsage'
    }

    attribute_map = {
        'disabled': 'disabled',
        'gl_code': 'glCode',
        'id': 'id',
        'manual_entries_allowed': 'manualEntriesAllowed',
        'name': 'name',
        'name_decorated': 'nameDecorated',
        'organization_running_balance': 'organizationRunningBalance',
        'tag_id': 'tagId',
        'type': 'type',
        'usage': 'usage'
    }

    def __init__(self, disabled=None, gl_code=None, id=None, manual_entries_allowed=None, name=None, name_decorated=None, organization_running_balance=None, tag_id=None, type=None, usage=None):  # noqa: E501
        """GetLoanProductsAssetAccountOptions - a model defined in Swagger"""  # noqa: E501
        self._disabled = None
        self._gl_code = None
        self._id = None
        self._manual_entries_allowed = None
        self._name = None
        self._name_decorated = None
        self._organization_running_balance = None
        self._tag_id = None
        self._type = None
        self._usage = None
        self.discriminator = None
        if disabled is not None:
            self.disabled = disabled
        if gl_code is not None:
            self.gl_code = gl_code
        if id is not None:
            self.id = id
        if manual_entries_allowed is not None:
            self.manual_entries_allowed = manual_entries_allowed
        if name is not None:
            self.name = name
        if name_decorated is not None:
            self.name_decorated = name_decorated
        if organization_running_balance is not None:
            self.organization_running_balance = organization_running_balance
        if tag_id is not None:
            self.tag_id = tag_id
        if type is not None:
            self.type = type
        if usage is not None:
            self.usage = usage

    @property
    def disabled(self):
        """Gets the disabled of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The disabled of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this GetLoanProductsAssetAccountOptions.


        :param disabled: The disabled of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def gl_code(self):
        """Gets the gl_code of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The gl_code of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: str
        """
        return self._gl_code

    @gl_code.setter
    def gl_code(self, gl_code):
        """Sets the gl_code of this GetLoanProductsAssetAccountOptions.


        :param gl_code: The gl_code of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: str
        """

        self._gl_code = gl_code

    @property
    def id(self):
        """Gets the id of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The id of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetLoanProductsAssetAccountOptions.


        :param id: The id of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def manual_entries_allowed(self):
        """Gets the manual_entries_allowed of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The manual_entries_allowed of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: bool
        """
        return self._manual_entries_allowed

    @manual_entries_allowed.setter
    def manual_entries_allowed(self, manual_entries_allowed):
        """Sets the manual_entries_allowed of this GetLoanProductsAssetAccountOptions.


        :param manual_entries_allowed: The manual_entries_allowed of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: bool
        """

        self._manual_entries_allowed = manual_entries_allowed

    @property
    def name(self):
        """Gets the name of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The name of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetLoanProductsAssetAccountOptions.


        :param name: The name of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_decorated(self):
        """Gets the name_decorated of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The name_decorated of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: str
        """
        return self._name_decorated

    @name_decorated.setter
    def name_decorated(self, name_decorated):
        """Sets the name_decorated of this GetLoanProductsAssetAccountOptions.


        :param name_decorated: The name_decorated of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: str
        """

        self._name_decorated = name_decorated

    @property
    def organization_running_balance(self):
        """Gets the organization_running_balance of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The organization_running_balance of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: int
        """
        return self._organization_running_balance

    @organization_running_balance.setter
    def organization_running_balance(self, organization_running_balance):
        """Sets the organization_running_balance of this GetLoanProductsAssetAccountOptions.


        :param organization_running_balance: The organization_running_balance of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: int
        """

        self._organization_running_balance = organization_running_balance

    @property
    def tag_id(self):
        """Gets the tag_id of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The tag_id of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: GetLoanProductsLiabilityTagId
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this GetLoanProductsAssetAccountOptions.


        :param tag_id: The tag_id of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: GetLoanProductsLiabilityTagId
        """

        self._tag_id = tag_id

    @property
    def type(self):
        """Gets the type of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The type of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: GetLoanProductsLiabilityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetLoanProductsAssetAccountOptions.


        :param type: The type of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: GetLoanProductsLiabilityType
        """

        self._type = type

    @property
    def usage(self):
        """Gets the usage of this GetLoanProductsAssetAccountOptions.  # noqa: E501


        :return: The usage of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :rtype: GetLoanProductsLiabilityUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this GetLoanProductsAssetAccountOptions.


        :param usage: The usage of this GetLoanProductsAssetAccountOptions.  # noqa: E501
        :type: GetLoanProductsLiabilityUsage
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
        if issubclass(GetLoanProductsAssetAccountOptions, dict):
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
        if not isinstance(other, GetLoanProductsAssetAccountOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
