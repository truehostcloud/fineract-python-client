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

class GetAccountRulesResponse(object):
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
        'allow_multiple_credit_entries': 'bool',
        'allow_multiple_debit_entries': 'bool',
        'credit_tags': 'list[AccountingTagRuleData]',
        'debit_tags': 'list[AccountingTagRuleData]',
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'office_id': 'int',
        'office_name': 'str',
        'system_defined': 'bool'
    }

    attribute_map = {
        'allow_multiple_credit_entries': 'allowMultipleCreditEntries',
        'allow_multiple_debit_entries': 'allowMultipleDebitEntries',
        'credit_tags': 'creditTags',
        'debit_tags': 'debitTags',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'system_defined': 'systemDefined'
    }

    def __init__(self, allow_multiple_credit_entries=None, allow_multiple_debit_entries=None, credit_tags=None, debit_tags=None, description=None, id=None, name=None, office_id=None, office_name=None, system_defined=None):  # noqa: E501
        """GetAccountRulesResponse - a model defined in Swagger"""  # noqa: E501
        self._allow_multiple_credit_entries = None
        self._allow_multiple_debit_entries = None
        self._credit_tags = None
        self._debit_tags = None
        self._description = None
        self._id = None
        self._name = None
        self._office_id = None
        self._office_name = None
        self._system_defined = None
        self.discriminator = None
        if allow_multiple_credit_entries is not None:
            self.allow_multiple_credit_entries = allow_multiple_credit_entries
        if allow_multiple_debit_entries is not None:
            self.allow_multiple_debit_entries = allow_multiple_debit_entries
        if credit_tags is not None:
            self.credit_tags = credit_tags
        if debit_tags is not None:
            self.debit_tags = debit_tags
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if system_defined is not None:
            self.system_defined = system_defined

    @property
    def allow_multiple_credit_entries(self):
        """Gets the allow_multiple_credit_entries of this GetAccountRulesResponse.  # noqa: E501


        :return: The allow_multiple_credit_entries of this GetAccountRulesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_credit_entries

    @allow_multiple_credit_entries.setter
    def allow_multiple_credit_entries(self, allow_multiple_credit_entries):
        """Sets the allow_multiple_credit_entries of this GetAccountRulesResponse.


        :param allow_multiple_credit_entries: The allow_multiple_credit_entries of this GetAccountRulesResponse.  # noqa: E501
        :type: bool
        """

        self._allow_multiple_credit_entries = allow_multiple_credit_entries

    @property
    def allow_multiple_debit_entries(self):
        """Gets the allow_multiple_debit_entries of this GetAccountRulesResponse.  # noqa: E501


        :return: The allow_multiple_debit_entries of this GetAccountRulesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_debit_entries

    @allow_multiple_debit_entries.setter
    def allow_multiple_debit_entries(self, allow_multiple_debit_entries):
        """Sets the allow_multiple_debit_entries of this GetAccountRulesResponse.


        :param allow_multiple_debit_entries: The allow_multiple_debit_entries of this GetAccountRulesResponse.  # noqa: E501
        :type: bool
        """

        self._allow_multiple_debit_entries = allow_multiple_debit_entries

    @property
    def credit_tags(self):
        """Gets the credit_tags of this GetAccountRulesResponse.  # noqa: E501


        :return: The credit_tags of this GetAccountRulesResponse.  # noqa: E501
        :rtype: list[AccountingTagRuleData]
        """
        return self._credit_tags

    @credit_tags.setter
    def credit_tags(self, credit_tags):
        """Sets the credit_tags of this GetAccountRulesResponse.


        :param credit_tags: The credit_tags of this GetAccountRulesResponse.  # noqa: E501
        :type: list[AccountingTagRuleData]
        """

        self._credit_tags = credit_tags

    @property
    def debit_tags(self):
        """Gets the debit_tags of this GetAccountRulesResponse.  # noqa: E501


        :return: The debit_tags of this GetAccountRulesResponse.  # noqa: E501
        :rtype: list[AccountingTagRuleData]
        """
        return self._debit_tags

    @debit_tags.setter
    def debit_tags(self, debit_tags):
        """Sets the debit_tags of this GetAccountRulesResponse.


        :param debit_tags: The debit_tags of this GetAccountRulesResponse.  # noqa: E501
        :type: list[AccountingTagRuleData]
        """

        self._debit_tags = debit_tags

    @property
    def description(self):
        """Gets the description of this GetAccountRulesResponse.  # noqa: E501


        :return: The description of this GetAccountRulesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetAccountRulesResponse.


        :param description: The description of this GetAccountRulesResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GetAccountRulesResponse.  # noqa: E501


        :return: The id of this GetAccountRulesResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAccountRulesResponse.


        :param id: The id of this GetAccountRulesResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetAccountRulesResponse.  # noqa: E501


        :return: The name of this GetAccountRulesResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAccountRulesResponse.


        :param name: The name of this GetAccountRulesResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def office_id(self):
        """Gets the office_id of this GetAccountRulesResponse.  # noqa: E501


        :return: The office_id of this GetAccountRulesResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetAccountRulesResponse.


        :param office_id: The office_id of this GetAccountRulesResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetAccountRulesResponse.  # noqa: E501


        :return: The office_name of this GetAccountRulesResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetAccountRulesResponse.


        :param office_name: The office_name of this GetAccountRulesResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def system_defined(self):
        """Gets the system_defined of this GetAccountRulesResponse.  # noqa: E501


        :return: The system_defined of this GetAccountRulesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._system_defined

    @system_defined.setter
    def system_defined(self, system_defined):
        """Sets the system_defined of this GetAccountRulesResponse.


        :param system_defined: The system_defined of this GetAccountRulesResponse.  # noqa: E501
        :type: bool
        """

        self._system_defined = system_defined

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
        if issubclass(GetAccountRulesResponse, dict):
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
        if not isinstance(other, GetAccountRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
