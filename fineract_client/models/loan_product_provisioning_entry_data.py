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

class LoanProductProvisioningEntryData(object):
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
        'amountreserved': 'float',
        'balance': 'float',
        'category_id': 'int',
        'category_name': 'str',
        'criteria_id': 'int',
        'currency_code': 'str',
        'expense_account': 'int',
        'expense_account_code': 'str',
        'expense_account_name': 'str',
        'history_id': 'int',
        'liability_account_code': 'str',
        'liability_account_name': 'str',
        'liablity_account': 'int',
        'office_id': 'int',
        'office_name': 'str',
        'overdue_in_days': 'int',
        'percentage': 'float',
        'product_id': 'int',
        'product_name': 'str'
    }

    attribute_map = {
        'amountreserved': 'amountreserved',
        'balance': 'balance',
        'category_id': 'categoryId',
        'category_name': 'categoryName',
        'criteria_id': 'criteriaId',
        'currency_code': 'currencyCode',
        'expense_account': 'expenseAccount',
        'expense_account_code': 'expenseAccountCode',
        'expense_account_name': 'expenseAccountName',
        'history_id': 'historyId',
        'liability_account_code': 'liabilityAccountCode',
        'liability_account_name': 'liabilityAccountName',
        'liablity_account': 'liablityAccount',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'overdue_in_days': 'overdueInDays',
        'percentage': 'percentage',
        'product_id': 'productId',
        'product_name': 'productName'
    }

    def __init__(self, amountreserved=None, balance=None, category_id=None, category_name=None, criteria_id=None, currency_code=None, expense_account=None, expense_account_code=None, expense_account_name=None, history_id=None, liability_account_code=None, liability_account_name=None, liablity_account=None, office_id=None, office_name=None, overdue_in_days=None, percentage=None, product_id=None, product_name=None):  # noqa: E501
        """LoanProductProvisioningEntryData - a model defined in Swagger"""  # noqa: E501
        self._amountreserved = None
        self._balance = None
        self._category_id = None
        self._category_name = None
        self._criteria_id = None
        self._currency_code = None
        self._expense_account = None
        self._expense_account_code = None
        self._expense_account_name = None
        self._history_id = None
        self._liability_account_code = None
        self._liability_account_name = None
        self._liablity_account = None
        self._office_id = None
        self._office_name = None
        self._overdue_in_days = None
        self._percentage = None
        self._product_id = None
        self._product_name = None
        self.discriminator = None
        if amountreserved is not None:
            self.amountreserved = amountreserved
        if balance is not None:
            self.balance = balance
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if criteria_id is not None:
            self.criteria_id = criteria_id
        if currency_code is not None:
            self.currency_code = currency_code
        if expense_account is not None:
            self.expense_account = expense_account
        if expense_account_code is not None:
            self.expense_account_code = expense_account_code
        if expense_account_name is not None:
            self.expense_account_name = expense_account_name
        if history_id is not None:
            self.history_id = history_id
        if liability_account_code is not None:
            self.liability_account_code = liability_account_code
        if liability_account_name is not None:
            self.liability_account_name = liability_account_name
        if liablity_account is not None:
            self.liablity_account = liablity_account
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if overdue_in_days is not None:
            self.overdue_in_days = overdue_in_days
        if percentage is not None:
            self.percentage = percentage
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name

    @property
    def amountreserved(self):
        """Gets the amountreserved of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The amountreserved of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: float
        """
        return self._amountreserved

    @amountreserved.setter
    def amountreserved(self, amountreserved):
        """Sets the amountreserved of this LoanProductProvisioningEntryData.


        :param amountreserved: The amountreserved of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: float
        """

        self._amountreserved = amountreserved

    @property
    def balance(self):
        """Gets the balance of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The balance of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this LoanProductProvisioningEntryData.


        :param balance: The balance of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def category_id(self):
        """Gets the category_id of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The category_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this LoanProductProvisioningEntryData.


        :param category_id: The category_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The category_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this LoanProductProvisioningEntryData.


        :param category_name: The category_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def criteria_id(self):
        """Gets the criteria_id of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The criteria_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._criteria_id

    @criteria_id.setter
    def criteria_id(self, criteria_id):
        """Sets the criteria_id of this LoanProductProvisioningEntryData.


        :param criteria_id: The criteria_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._criteria_id = criteria_id

    @property
    def currency_code(self):
        """Gets the currency_code of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The currency_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this LoanProductProvisioningEntryData.


        :param currency_code: The currency_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def expense_account(self):
        """Gets the expense_account of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The expense_account of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._expense_account

    @expense_account.setter
    def expense_account(self, expense_account):
        """Sets the expense_account of this LoanProductProvisioningEntryData.


        :param expense_account: The expense_account of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._expense_account = expense_account

    @property
    def expense_account_code(self):
        """Gets the expense_account_code of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The expense_account_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_code

    @expense_account_code.setter
    def expense_account_code(self, expense_account_code):
        """Sets the expense_account_code of this LoanProductProvisioningEntryData.


        :param expense_account_code: The expense_account_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._expense_account_code = expense_account_code

    @property
    def expense_account_name(self):
        """Gets the expense_account_name of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The expense_account_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_name

    @expense_account_name.setter
    def expense_account_name(self, expense_account_name):
        """Sets the expense_account_name of this LoanProductProvisioningEntryData.


        :param expense_account_name: The expense_account_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._expense_account_name = expense_account_name

    @property
    def history_id(self):
        """Gets the history_id of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The history_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._history_id

    @history_id.setter
    def history_id(self, history_id):
        """Sets the history_id of this LoanProductProvisioningEntryData.


        :param history_id: The history_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._history_id = history_id

    @property
    def liability_account_code(self):
        """Gets the liability_account_code of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The liability_account_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_code

    @liability_account_code.setter
    def liability_account_code(self, liability_account_code):
        """Sets the liability_account_code of this LoanProductProvisioningEntryData.


        :param liability_account_code: The liability_account_code of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._liability_account_code = liability_account_code

    @property
    def liability_account_name(self):
        """Gets the liability_account_name of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The liability_account_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_name

    @liability_account_name.setter
    def liability_account_name(self, liability_account_name):
        """Sets the liability_account_name of this LoanProductProvisioningEntryData.


        :param liability_account_name: The liability_account_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._liability_account_name = liability_account_name

    @property
    def liablity_account(self):
        """Gets the liablity_account of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The liablity_account of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._liablity_account

    @liablity_account.setter
    def liablity_account(self, liablity_account):
        """Sets the liablity_account of this LoanProductProvisioningEntryData.


        :param liablity_account: The liablity_account of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._liablity_account = liablity_account

    @property
    def office_id(self):
        """Gets the office_id of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The office_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this LoanProductProvisioningEntryData.


        :param office_id: The office_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The office_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this LoanProductProvisioningEntryData.


        :param office_name: The office_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def overdue_in_days(self):
        """Gets the overdue_in_days of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The overdue_in_days of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._overdue_in_days

    @overdue_in_days.setter
    def overdue_in_days(self, overdue_in_days):
        """Sets the overdue_in_days of this LoanProductProvisioningEntryData.


        :param overdue_in_days: The overdue_in_days of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._overdue_in_days = overdue_in_days

    @property
    def percentage(self):
        """Gets the percentage of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The percentage of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this LoanProductProvisioningEntryData.


        :param percentage: The percentage of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def product_id(self):
        """Gets the product_id of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The product_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this LoanProductProvisioningEntryData.


        :param product_id: The product_id of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this LoanProductProvisioningEntryData.  # noqa: E501


        :return: The product_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this LoanProductProvisioningEntryData.


        :param product_name: The product_name of this LoanProductProvisioningEntryData.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

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
        if issubclass(LoanProductProvisioningEntryData, dict):
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
        if not isinstance(other, LoanProductProvisioningEntryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
