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

class TaxComponentData(object):
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
        'credit_account': 'GLAccountData',
        'credit_account_type': 'EnumOptionData',
        'debit_account': 'GLAccountData',
        'debit_account_type': 'EnumOptionData',
        'gl_account_options': 'dict(str, list[GLAccountData])',
        'gl_account_type_options': 'list[EnumOptionData]',
        'id': 'int',
        'name': 'str',
        'percentage': 'float',
        'start_date': 'date',
        'tax_component_histories': 'list[TaxComponentHistoryData]'
    }

    attribute_map = {
        'credit_account': 'creditAccount',
        'credit_account_type': 'creditAccountType',
        'debit_account': 'debitAccount',
        'debit_account_type': 'debitAccountType',
        'gl_account_options': 'glAccountOptions',
        'gl_account_type_options': 'glAccountTypeOptions',
        'id': 'id',
        'name': 'name',
        'percentage': 'percentage',
        'start_date': 'startDate',
        'tax_component_histories': 'taxComponentHistories'
    }

    def __init__(self, credit_account=None, credit_account_type=None, debit_account=None, debit_account_type=None, gl_account_options=None, gl_account_type_options=None, id=None, name=None, percentage=None, start_date=None, tax_component_histories=None):  # noqa: E501
        """TaxComponentData - a model defined in Swagger"""  # noqa: E501
        self._credit_account = None
        self._credit_account_type = None
        self._debit_account = None
        self._debit_account_type = None
        self._gl_account_options = None
        self._gl_account_type_options = None
        self._id = None
        self._name = None
        self._percentage = None
        self._start_date = None
        self._tax_component_histories = None
        self.discriminator = None
        if credit_account is not None:
            self.credit_account = credit_account
        if credit_account_type is not None:
            self.credit_account_type = credit_account_type
        if debit_account is not None:
            self.debit_account = debit_account
        if debit_account_type is not None:
            self.debit_account_type = debit_account_type
        if gl_account_options is not None:
            self.gl_account_options = gl_account_options
        if gl_account_type_options is not None:
            self.gl_account_type_options = gl_account_type_options
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if percentage is not None:
            self.percentage = percentage
        if start_date is not None:
            self.start_date = start_date
        if tax_component_histories is not None:
            self.tax_component_histories = tax_component_histories

    @property
    def credit_account(self):
        """Gets the credit_account of this TaxComponentData.  # noqa: E501


        :return: The credit_account of this TaxComponentData.  # noqa: E501
        :rtype: GLAccountData
        """
        return self._credit_account

    @credit_account.setter
    def credit_account(self, credit_account):
        """Sets the credit_account of this TaxComponentData.


        :param credit_account: The credit_account of this TaxComponentData.  # noqa: E501
        :type: GLAccountData
        """

        self._credit_account = credit_account

    @property
    def credit_account_type(self):
        """Gets the credit_account_type of this TaxComponentData.  # noqa: E501


        :return: The credit_account_type of this TaxComponentData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._credit_account_type

    @credit_account_type.setter
    def credit_account_type(self, credit_account_type):
        """Sets the credit_account_type of this TaxComponentData.


        :param credit_account_type: The credit_account_type of this TaxComponentData.  # noqa: E501
        :type: EnumOptionData
        """

        self._credit_account_type = credit_account_type

    @property
    def debit_account(self):
        """Gets the debit_account of this TaxComponentData.  # noqa: E501


        :return: The debit_account of this TaxComponentData.  # noqa: E501
        :rtype: GLAccountData
        """
        return self._debit_account

    @debit_account.setter
    def debit_account(self, debit_account):
        """Sets the debit_account of this TaxComponentData.


        :param debit_account: The debit_account of this TaxComponentData.  # noqa: E501
        :type: GLAccountData
        """

        self._debit_account = debit_account

    @property
    def debit_account_type(self):
        """Gets the debit_account_type of this TaxComponentData.  # noqa: E501


        :return: The debit_account_type of this TaxComponentData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._debit_account_type

    @debit_account_type.setter
    def debit_account_type(self, debit_account_type):
        """Sets the debit_account_type of this TaxComponentData.


        :param debit_account_type: The debit_account_type of this TaxComponentData.  # noqa: E501
        :type: EnumOptionData
        """

        self._debit_account_type = debit_account_type

    @property
    def gl_account_options(self):
        """Gets the gl_account_options of this TaxComponentData.  # noqa: E501


        :return: The gl_account_options of this TaxComponentData.  # noqa: E501
        :rtype: dict(str, list[GLAccountData])
        """
        return self._gl_account_options

    @gl_account_options.setter
    def gl_account_options(self, gl_account_options):
        """Sets the gl_account_options of this TaxComponentData.


        :param gl_account_options: The gl_account_options of this TaxComponentData.  # noqa: E501
        :type: dict(str, list[GLAccountData])
        """

        self._gl_account_options = gl_account_options

    @property
    def gl_account_type_options(self):
        """Gets the gl_account_type_options of this TaxComponentData.  # noqa: E501


        :return: The gl_account_type_options of this TaxComponentData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._gl_account_type_options

    @gl_account_type_options.setter
    def gl_account_type_options(self, gl_account_type_options):
        """Sets the gl_account_type_options of this TaxComponentData.


        :param gl_account_type_options: The gl_account_type_options of this TaxComponentData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._gl_account_type_options = gl_account_type_options

    @property
    def id(self):
        """Gets the id of this TaxComponentData.  # noqa: E501


        :return: The id of this TaxComponentData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxComponentData.


        :param id: The id of this TaxComponentData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaxComponentData.  # noqa: E501


        :return: The name of this TaxComponentData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxComponentData.


        :param name: The name of this TaxComponentData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this TaxComponentData.  # noqa: E501


        :return: The percentage of this TaxComponentData.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this TaxComponentData.


        :param percentage: The percentage of this TaxComponentData.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def start_date(self):
        """Gets the start_date of this TaxComponentData.  # noqa: E501


        :return: The start_date of this TaxComponentData.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TaxComponentData.


        :param start_date: The start_date of this TaxComponentData.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def tax_component_histories(self):
        """Gets the tax_component_histories of this TaxComponentData.  # noqa: E501


        :return: The tax_component_histories of this TaxComponentData.  # noqa: E501
        :rtype: list[TaxComponentHistoryData]
        """
        return self._tax_component_histories

    @tax_component_histories.setter
    def tax_component_histories(self, tax_component_histories):
        """Sets the tax_component_histories of this TaxComponentData.


        :param tax_component_histories: The tax_component_histories of this TaxComponentData.  # noqa: E501
        :type: list[TaxComponentHistoryData]
        """

        self._tax_component_histories = tax_component_histories

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
        if issubclass(TaxComponentData, dict):
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
        if not isinstance(other, TaxComponentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
