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

class GetSavingsAccountTransactionsPageItem(object):
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
        'account_id': 'int',
        'account_no': 'str',
        'amount': 'float',
        'charges_paid_by_data': 'list[GetSavingsAccountChargesPaidByData]',
        'currency': 'GetTransactionsCurrency',
        '_date': 'date',
        'entry_type': 'str',
        'id': 'int',
        'interested_posted_as_on': 'bool',
        'is_manual_transaction': 'bool',
        'is_reversal': 'bool',
        'lien_transaction': 'bool',
        'original_transaction_id': 'int',
        'payment_detail_data': 'GetTransactionsPaymentDetailData',
        'release_transaction_id': 'int',
        'reversed': 'bool',
        'running_balance': 'float',
        'submitted_by_username': 'str',
        'submitted_on_date': 'date',
        'transaction_type': 'GetTranscationEnumData'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_no': 'accountNo',
        'amount': 'amount',
        'charges_paid_by_data': 'chargesPaidByData',
        'currency': 'currency',
        '_date': 'date',
        'entry_type': 'entryType',
        'id': 'id',
        'interested_posted_as_on': 'interestedPostedAsOn',
        'is_manual_transaction': 'isManualTransaction',
        'is_reversal': 'isReversal',
        'lien_transaction': 'lienTransaction',
        'original_transaction_id': 'originalTransactionId',
        'payment_detail_data': 'paymentDetailData',
        'release_transaction_id': 'releaseTransactionId',
        'reversed': 'reversed',
        'running_balance': 'runningBalance',
        'submitted_by_username': 'submittedByUsername',
        'submitted_on_date': 'submittedOnDate',
        'transaction_type': 'transactionType'
    }

    def __init__(self, account_id=None, account_no=None, amount=None, charges_paid_by_data=None, currency=None, _date=None, entry_type=None, id=None, interested_posted_as_on=None, is_manual_transaction=None, is_reversal=None, lien_transaction=None, original_transaction_id=None, payment_detail_data=None, release_transaction_id=None, reversed=None, running_balance=None, submitted_by_username=None, submitted_on_date=None, transaction_type=None):  # noqa: E501
        """GetSavingsAccountTransactionsPageItem - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._account_no = None
        self._amount = None
        self._charges_paid_by_data = None
        self._currency = None
        self.__date = None
        self._entry_type = None
        self._id = None
        self._interested_posted_as_on = None
        self._is_manual_transaction = None
        self._is_reversal = None
        self._lien_transaction = None
        self._original_transaction_id = None
        self._payment_detail_data = None
        self._release_transaction_id = None
        self._reversed = None
        self._running_balance = None
        self._submitted_by_username = None
        self._submitted_on_date = None
        self._transaction_type = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if account_no is not None:
            self.account_no = account_no
        if amount is not None:
            self.amount = amount
        if charges_paid_by_data is not None:
            self.charges_paid_by_data = charges_paid_by_data
        if currency is not None:
            self.currency = currency
        if _date is not None:
            self._date = _date
        if entry_type is not None:
            self.entry_type = entry_type
        if id is not None:
            self.id = id
        if interested_posted_as_on is not None:
            self.interested_posted_as_on = interested_posted_as_on
        if is_manual_transaction is not None:
            self.is_manual_transaction = is_manual_transaction
        if is_reversal is not None:
            self.is_reversal = is_reversal
        if lien_transaction is not None:
            self.lien_transaction = lien_transaction
        if original_transaction_id is not None:
            self.original_transaction_id = original_transaction_id
        if payment_detail_data is not None:
            self.payment_detail_data = payment_detail_data
        if release_transaction_id is not None:
            self.release_transaction_id = release_transaction_id
        if reversed is not None:
            self.reversed = reversed
        if running_balance is not None:
            self.running_balance = running_balance
        if submitted_by_username is not None:
            self.submitted_by_username = submitted_by_username
        if submitted_on_date is not None:
            self.submitted_on_date = submitted_on_date
        if transaction_type is not None:
            self.transaction_type = transaction_type

    @property
    def account_id(self):
        """Gets the account_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The account_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GetSavingsAccountTransactionsPageItem.


        :param account_id: The account_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def account_no(self):
        """Gets the account_no of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The account_no of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetSavingsAccountTransactionsPageItem.


        :param account_no: The account_no of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def amount(self):
        """Gets the amount of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The amount of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetSavingsAccountTransactionsPageItem.


        :param amount: The amount of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def charges_paid_by_data(self):
        """Gets the charges_paid_by_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The charges_paid_by_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: list[GetSavingsAccountChargesPaidByData]
        """
        return self._charges_paid_by_data

    @charges_paid_by_data.setter
    def charges_paid_by_data(self, charges_paid_by_data):
        """Sets the charges_paid_by_data of this GetSavingsAccountTransactionsPageItem.


        :param charges_paid_by_data: The charges_paid_by_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: list[GetSavingsAccountChargesPaidByData]
        """

        self._charges_paid_by_data = charges_paid_by_data

    @property
    def currency(self):
        """Gets the currency of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The currency of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: GetTransactionsCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetSavingsAccountTransactionsPageItem.


        :param currency: The currency of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: GetTransactionsCurrency
        """

        self._currency = currency

    @property
    def _date(self):
        """Gets the _date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The _date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this GetSavingsAccountTransactionsPageItem.


        :param _date: The _date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def entry_type(self):
        """Gets the entry_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The entry_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this GetSavingsAccountTransactionsPageItem.


        :param entry_type: The entry_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREDIT", "DEBIT"]  # noqa: E501
        if entry_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entry_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entry_type, allowed_values)
            )

        self._entry_type = entry_type

    @property
    def id(self):
        """Gets the id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSavingsAccountTransactionsPageItem.


        :param id: The id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interested_posted_as_on(self):
        """Gets the interested_posted_as_on of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The interested_posted_as_on of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: bool
        """
        return self._interested_posted_as_on

    @interested_posted_as_on.setter
    def interested_posted_as_on(self, interested_posted_as_on):
        """Sets the interested_posted_as_on of this GetSavingsAccountTransactionsPageItem.


        :param interested_posted_as_on: The interested_posted_as_on of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: bool
        """

        self._interested_posted_as_on = interested_posted_as_on

    @property
    def is_manual_transaction(self):
        """Gets the is_manual_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The is_manual_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_manual_transaction

    @is_manual_transaction.setter
    def is_manual_transaction(self, is_manual_transaction):
        """Sets the is_manual_transaction of this GetSavingsAccountTransactionsPageItem.


        :param is_manual_transaction: The is_manual_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: bool
        """

        self._is_manual_transaction = is_manual_transaction

    @property
    def is_reversal(self):
        """Gets the is_reversal of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The is_reversal of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_reversal

    @is_reversal.setter
    def is_reversal(self, is_reversal):
        """Sets the is_reversal of this GetSavingsAccountTransactionsPageItem.


        :param is_reversal: The is_reversal of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: bool
        """

        self._is_reversal = is_reversal

    @property
    def lien_transaction(self):
        """Gets the lien_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The lien_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: bool
        """
        return self._lien_transaction

    @lien_transaction.setter
    def lien_transaction(self, lien_transaction):
        """Sets the lien_transaction of this GetSavingsAccountTransactionsPageItem.


        :param lien_transaction: The lien_transaction of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: bool
        """

        self._lien_transaction = lien_transaction

    @property
    def original_transaction_id(self):
        """Gets the original_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The original_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: int
        """
        return self._original_transaction_id

    @original_transaction_id.setter
    def original_transaction_id(self, original_transaction_id):
        """Sets the original_transaction_id of this GetSavingsAccountTransactionsPageItem.


        :param original_transaction_id: The original_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: int
        """

        self._original_transaction_id = original_transaction_id

    @property
    def payment_detail_data(self):
        """Gets the payment_detail_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The payment_detail_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: GetTransactionsPaymentDetailData
        """
        return self._payment_detail_data

    @payment_detail_data.setter
    def payment_detail_data(self, payment_detail_data):
        """Sets the payment_detail_data of this GetSavingsAccountTransactionsPageItem.


        :param payment_detail_data: The payment_detail_data of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: GetTransactionsPaymentDetailData
        """

        self._payment_detail_data = payment_detail_data

    @property
    def release_transaction_id(self):
        """Gets the release_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The release_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: int
        """
        return self._release_transaction_id

    @release_transaction_id.setter
    def release_transaction_id(self, release_transaction_id):
        """Sets the release_transaction_id of this GetSavingsAccountTransactionsPageItem.


        :param release_transaction_id: The release_transaction_id of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: int
        """

        self._release_transaction_id = release_transaction_id

    @property
    def reversed(self):
        """Gets the reversed of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The reversed of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: bool
        """
        return self._reversed

    @reversed.setter
    def reversed(self, reversed):
        """Sets the reversed of this GetSavingsAccountTransactionsPageItem.


        :param reversed: The reversed of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: bool
        """

        self._reversed = reversed

    @property
    def running_balance(self):
        """Gets the running_balance of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The running_balance of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: float
        """
        return self._running_balance

    @running_balance.setter
    def running_balance(self, running_balance):
        """Sets the running_balance of this GetSavingsAccountTransactionsPageItem.


        :param running_balance: The running_balance of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: float
        """

        self._running_balance = running_balance

    @property
    def submitted_by_username(self):
        """Gets the submitted_by_username of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The submitted_by_username of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_username

    @submitted_by_username.setter
    def submitted_by_username(self, submitted_by_username):
        """Sets the submitted_by_username of this GetSavingsAccountTransactionsPageItem.


        :param submitted_by_username: The submitted_by_username of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: str
        """

        self._submitted_by_username = submitted_by_username

    @property
    def submitted_on_date(self):
        """Gets the submitted_on_date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The submitted_on_date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: date
        """
        return self._submitted_on_date

    @submitted_on_date.setter
    def submitted_on_date(self, submitted_on_date):
        """Sets the submitted_on_date of this GetSavingsAccountTransactionsPageItem.


        :param submitted_on_date: The submitted_on_date of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: date
        """

        self._submitted_on_date = submitted_on_date

    @property
    def transaction_type(self):
        """Gets the transaction_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501


        :return: The transaction_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :rtype: GetTranscationEnumData
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this GetSavingsAccountTransactionsPageItem.


        :param transaction_type: The transaction_type of this GetSavingsAccountTransactionsPageItem.  # noqa: E501
        :type: GetTranscationEnumData
        """

        self._transaction_type = transaction_type

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
        if issubclass(GetSavingsAccountTransactionsPageItem, dict):
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
        if not isinstance(other, GetSavingsAccountTransactionsPageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
