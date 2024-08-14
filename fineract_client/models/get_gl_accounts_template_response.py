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

class GetGLAccountsTemplateResponse(object):
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
        'account_type_options': 'list[EnumOptionData]',
        'allowed_assets_tag_options': 'list[CodeValueData]',
        'allowed_equity_tag_options': 'list[CodeValueData]',
        'allowed_expenses_tag_options': 'list[CodeValueData]',
        'allowed_income_tag_options': 'list[CodeValueData]',
        'allowed_liabilities_tag_options': 'list[CodeValueData]',
        'asset_header_account_options': 'list[GLAccountData]',
        'disabled': 'bool',
        'equity_header_account_options': 'list[GLAccountData]',
        'expense_header_account_options': 'list[GLAccountData]',
        'liability_header_account_options': 'list[GLAccountData]',
        'manual_entries_allowed': 'bool',
        'type': 'EnumOptionData',
        'usage': 'EnumOptionData',
        'usage_options': 'list[EnumOptionData]'
    }

    attribute_map = {
        'account_type_options': 'accountTypeOptions',
        'allowed_assets_tag_options': 'allowedAssetsTagOptions',
        'allowed_equity_tag_options': 'allowedEquityTagOptions',
        'allowed_expenses_tag_options': 'allowedExpensesTagOptions',
        'allowed_income_tag_options': 'allowedIncomeTagOptions',
        'allowed_liabilities_tag_options': 'allowedLiabilitiesTagOptions',
        'asset_header_account_options': 'assetHeaderAccountOptions',
        'disabled': 'disabled',
        'equity_header_account_options': 'equityHeaderAccountOptions',
        'expense_header_account_options': 'expenseHeaderAccountOptions',
        'liability_header_account_options': 'liabilityHeaderAccountOptions',
        'manual_entries_allowed': 'manualEntriesAllowed',
        'type': 'type',
        'usage': 'usage',
        'usage_options': 'usageOptions'
    }

    def __init__(self, account_type_options=None, allowed_assets_tag_options=None, allowed_equity_tag_options=None, allowed_expenses_tag_options=None, allowed_income_tag_options=None, allowed_liabilities_tag_options=None, asset_header_account_options=None, disabled=None, equity_header_account_options=None, expense_header_account_options=None, liability_header_account_options=None, manual_entries_allowed=None, type=None, usage=None, usage_options=None):  # noqa: E501
        """GetGLAccountsTemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._account_type_options = None
        self._allowed_assets_tag_options = None
        self._allowed_equity_tag_options = None
        self._allowed_expenses_tag_options = None
        self._allowed_income_tag_options = None
        self._allowed_liabilities_tag_options = None
        self._asset_header_account_options = None
        self._disabled = None
        self._equity_header_account_options = None
        self._expense_header_account_options = None
        self._liability_header_account_options = None
        self._manual_entries_allowed = None
        self._type = None
        self._usage = None
        self._usage_options = None
        self.discriminator = None
        if account_type_options is not None:
            self.account_type_options = account_type_options
        if allowed_assets_tag_options is not None:
            self.allowed_assets_tag_options = allowed_assets_tag_options
        if allowed_equity_tag_options is not None:
            self.allowed_equity_tag_options = allowed_equity_tag_options
        if allowed_expenses_tag_options is not None:
            self.allowed_expenses_tag_options = allowed_expenses_tag_options
        if allowed_income_tag_options is not None:
            self.allowed_income_tag_options = allowed_income_tag_options
        if allowed_liabilities_tag_options is not None:
            self.allowed_liabilities_tag_options = allowed_liabilities_tag_options
        if asset_header_account_options is not None:
            self.asset_header_account_options = asset_header_account_options
        if disabled is not None:
            self.disabled = disabled
        if equity_header_account_options is not None:
            self.equity_header_account_options = equity_header_account_options
        if expense_header_account_options is not None:
            self.expense_header_account_options = expense_header_account_options
        if liability_header_account_options is not None:
            self.liability_header_account_options = liability_header_account_options
        if manual_entries_allowed is not None:
            self.manual_entries_allowed = manual_entries_allowed
        if type is not None:
            self.type = type
        if usage is not None:
            self.usage = usage
        if usage_options is not None:
            self.usage_options = usage_options

    @property
    def account_type_options(self):
        """Gets the account_type_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The account_type_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._account_type_options

    @account_type_options.setter
    def account_type_options(self, account_type_options):
        """Sets the account_type_options of this GetGLAccountsTemplateResponse.


        :param account_type_options: The account_type_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._account_type_options = account_type_options

    @property
    def allowed_assets_tag_options(self):
        """Gets the allowed_assets_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The allowed_assets_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._allowed_assets_tag_options

    @allowed_assets_tag_options.setter
    def allowed_assets_tag_options(self, allowed_assets_tag_options):
        """Sets the allowed_assets_tag_options of this GetGLAccountsTemplateResponse.


        :param allowed_assets_tag_options: The allowed_assets_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._allowed_assets_tag_options = allowed_assets_tag_options

    @property
    def allowed_equity_tag_options(self):
        """Gets the allowed_equity_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The allowed_equity_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._allowed_equity_tag_options

    @allowed_equity_tag_options.setter
    def allowed_equity_tag_options(self, allowed_equity_tag_options):
        """Sets the allowed_equity_tag_options of this GetGLAccountsTemplateResponse.


        :param allowed_equity_tag_options: The allowed_equity_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._allowed_equity_tag_options = allowed_equity_tag_options

    @property
    def allowed_expenses_tag_options(self):
        """Gets the allowed_expenses_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The allowed_expenses_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._allowed_expenses_tag_options

    @allowed_expenses_tag_options.setter
    def allowed_expenses_tag_options(self, allowed_expenses_tag_options):
        """Sets the allowed_expenses_tag_options of this GetGLAccountsTemplateResponse.


        :param allowed_expenses_tag_options: The allowed_expenses_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._allowed_expenses_tag_options = allowed_expenses_tag_options

    @property
    def allowed_income_tag_options(self):
        """Gets the allowed_income_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The allowed_income_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._allowed_income_tag_options

    @allowed_income_tag_options.setter
    def allowed_income_tag_options(self, allowed_income_tag_options):
        """Sets the allowed_income_tag_options of this GetGLAccountsTemplateResponse.


        :param allowed_income_tag_options: The allowed_income_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._allowed_income_tag_options = allowed_income_tag_options

    @property
    def allowed_liabilities_tag_options(self):
        """Gets the allowed_liabilities_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The allowed_liabilities_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._allowed_liabilities_tag_options

    @allowed_liabilities_tag_options.setter
    def allowed_liabilities_tag_options(self, allowed_liabilities_tag_options):
        """Sets the allowed_liabilities_tag_options of this GetGLAccountsTemplateResponse.


        :param allowed_liabilities_tag_options: The allowed_liabilities_tag_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._allowed_liabilities_tag_options = allowed_liabilities_tag_options

    @property
    def asset_header_account_options(self):
        """Gets the asset_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The asset_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[GLAccountData]
        """
        return self._asset_header_account_options

    @asset_header_account_options.setter
    def asset_header_account_options(self, asset_header_account_options):
        """Sets the asset_header_account_options of this GetGLAccountsTemplateResponse.


        :param asset_header_account_options: The asset_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[GLAccountData]
        """

        self._asset_header_account_options = asset_header_account_options

    @property
    def disabled(self):
        """Gets the disabled of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The disabled of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this GetGLAccountsTemplateResponse.


        :param disabled: The disabled of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def equity_header_account_options(self):
        """Gets the equity_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The equity_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[GLAccountData]
        """
        return self._equity_header_account_options

    @equity_header_account_options.setter
    def equity_header_account_options(self, equity_header_account_options):
        """Sets the equity_header_account_options of this GetGLAccountsTemplateResponse.


        :param equity_header_account_options: The equity_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[GLAccountData]
        """

        self._equity_header_account_options = equity_header_account_options

    @property
    def expense_header_account_options(self):
        """Gets the expense_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The expense_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[GLAccountData]
        """
        return self._expense_header_account_options

    @expense_header_account_options.setter
    def expense_header_account_options(self, expense_header_account_options):
        """Sets the expense_header_account_options of this GetGLAccountsTemplateResponse.


        :param expense_header_account_options: The expense_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[GLAccountData]
        """

        self._expense_header_account_options = expense_header_account_options

    @property
    def liability_header_account_options(self):
        """Gets the liability_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The liability_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[GLAccountData]
        """
        return self._liability_header_account_options

    @liability_header_account_options.setter
    def liability_header_account_options(self, liability_header_account_options):
        """Sets the liability_header_account_options of this GetGLAccountsTemplateResponse.


        :param liability_header_account_options: The liability_header_account_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[GLAccountData]
        """

        self._liability_header_account_options = liability_header_account_options

    @property
    def manual_entries_allowed(self):
        """Gets the manual_entries_allowed of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The manual_entries_allowed of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._manual_entries_allowed

    @manual_entries_allowed.setter
    def manual_entries_allowed(self, manual_entries_allowed):
        """Sets the manual_entries_allowed of this GetGLAccountsTemplateResponse.


        :param manual_entries_allowed: The manual_entries_allowed of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: bool
        """

        self._manual_entries_allowed = manual_entries_allowed

    @property
    def type(self):
        """Gets the type of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The type of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetGLAccountsTemplateResponse.


        :param type: The type of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: EnumOptionData
        """

        self._type = type

    @property
    def usage(self):
        """Gets the usage of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The usage of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this GetGLAccountsTemplateResponse.


        :param usage: The usage of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: EnumOptionData
        """

        self._usage = usage

    @property
    def usage_options(self):
        """Gets the usage_options of this GetGLAccountsTemplateResponse.  # noqa: E501


        :return: The usage_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._usage_options

    @usage_options.setter
    def usage_options(self, usage_options):
        """Sets the usage_options of this GetGLAccountsTemplateResponse.


        :param usage_options: The usage_options of this GetGLAccountsTemplateResponse.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._usage_options = usage_options

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
        if issubclass(GetGLAccountsTemplateResponse, dict):
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
        if not isinstance(other, GetGLAccountsTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
