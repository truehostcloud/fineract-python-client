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

class ProvisioningCriteriaDefinitionData(object):
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
        'category_id': 'int',
        'category_name': 'str',
        'expense_account': 'int',
        'expense_code': 'str',
        'expense_name': 'str',
        'id': 'int',
        'liability_account': 'int',
        'liability_code': 'str',
        'liability_name': 'str',
        'max_age': 'int',
        'min_age': 'int',
        'provisioning_percentage': 'float'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'category_name': 'categoryName',
        'expense_account': 'expenseAccount',
        'expense_code': 'expenseCode',
        'expense_name': 'expenseName',
        'id': 'id',
        'liability_account': 'liabilityAccount',
        'liability_code': 'liabilityCode',
        'liability_name': 'liabilityName',
        'max_age': 'maxAge',
        'min_age': 'minAge',
        'provisioning_percentage': 'provisioningPercentage'
    }

    def __init__(self, category_id=None, category_name=None, expense_account=None, expense_code=None, expense_name=None, id=None, liability_account=None, liability_code=None, liability_name=None, max_age=None, min_age=None, provisioning_percentage=None):  # noqa: E501
        """ProvisioningCriteriaDefinitionData - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._category_name = None
        self._expense_account = None
        self._expense_code = None
        self._expense_name = None
        self._id = None
        self._liability_account = None
        self._liability_code = None
        self._liability_name = None
        self._max_age = None
        self._min_age = None
        self._provisioning_percentage = None
        self.discriminator = None
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if expense_account is not None:
            self.expense_account = expense_account
        if expense_code is not None:
            self.expense_code = expense_code
        if expense_name is not None:
            self.expense_name = expense_name
        if id is not None:
            self.id = id
        if liability_account is not None:
            self.liability_account = liability_account
        if liability_code is not None:
            self.liability_code = liability_code
        if liability_name is not None:
            self.liability_name = liability_name
        if max_age is not None:
            self.max_age = max_age
        if min_age is not None:
            self.min_age = min_age
        if provisioning_percentage is not None:
            self.provisioning_percentage = provisioning_percentage

    @property
    def category_id(self):
        """Gets the category_id of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The category_id of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ProvisioningCriteriaDefinitionData.


        :param category_id: The category_id of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The category_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this ProvisioningCriteriaDefinitionData.


        :param category_name: The category_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def expense_account(self):
        """Gets the expense_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The expense_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._expense_account

    @expense_account.setter
    def expense_account(self, expense_account):
        """Sets the expense_account of this ProvisioningCriteriaDefinitionData.


        :param expense_account: The expense_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._expense_account = expense_account

    @property
    def expense_code(self):
        """Gets the expense_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The expense_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: str
        """
        return self._expense_code

    @expense_code.setter
    def expense_code(self, expense_code):
        """Sets the expense_code of this ProvisioningCriteriaDefinitionData.


        :param expense_code: The expense_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: str
        """

        self._expense_code = expense_code

    @property
    def expense_name(self):
        """Gets the expense_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The expense_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: str
        """
        return self._expense_name

    @expense_name.setter
    def expense_name(self, expense_name):
        """Sets the expense_name of this ProvisioningCriteriaDefinitionData.


        :param expense_name: The expense_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: str
        """

        self._expense_name = expense_name

    @property
    def id(self):
        """Gets the id of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The id of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvisioningCriteriaDefinitionData.


        :param id: The id of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def liability_account(self):
        """Gets the liability_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The liability_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._liability_account

    @liability_account.setter
    def liability_account(self, liability_account):
        """Sets the liability_account of this ProvisioningCriteriaDefinitionData.


        :param liability_account: The liability_account of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._liability_account = liability_account

    @property
    def liability_code(self):
        """Gets the liability_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The liability_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: str
        """
        return self._liability_code

    @liability_code.setter
    def liability_code(self, liability_code):
        """Sets the liability_code of this ProvisioningCriteriaDefinitionData.


        :param liability_code: The liability_code of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: str
        """

        self._liability_code = liability_code

    @property
    def liability_name(self):
        """Gets the liability_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The liability_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: str
        """
        return self._liability_name

    @liability_name.setter
    def liability_name(self, liability_name):
        """Sets the liability_name of this ProvisioningCriteriaDefinitionData.


        :param liability_name: The liability_name of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: str
        """

        self._liability_name = liability_name

    @property
    def max_age(self):
        """Gets the max_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The max_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this ProvisioningCriteriaDefinitionData.


        :param max_age: The max_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._max_age = max_age

    @property
    def min_age(self):
        """Gets the min_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The min_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: int
        """
        return self._min_age

    @min_age.setter
    def min_age(self, min_age):
        """Sets the min_age of this ProvisioningCriteriaDefinitionData.


        :param min_age: The min_age of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: int
        """

        self._min_age = min_age

    @property
    def provisioning_percentage(self):
        """Gets the provisioning_percentage of this ProvisioningCriteriaDefinitionData.  # noqa: E501


        :return: The provisioning_percentage of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :rtype: float
        """
        return self._provisioning_percentage

    @provisioning_percentage.setter
    def provisioning_percentage(self, provisioning_percentage):
        """Sets the provisioning_percentage of this ProvisioningCriteriaDefinitionData.


        :param provisioning_percentage: The provisioning_percentage of this ProvisioningCriteriaDefinitionData.  # noqa: E501
        :type: float
        """

        self._provisioning_percentage = provisioning_percentage

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
        if issubclass(ProvisioningCriteriaDefinitionData, dict):
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
        if not isinstance(other, ProvisioningCriteriaDefinitionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
