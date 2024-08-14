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

class PostLoansLoanIdTransactionsResponseChanges(object):
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
        'date_format': 'str',
        'external_id': 'str',
        'locale': 'str',
        'note': 'str',
        'payment_type_id': 'int',
        'reversal_external_id': 'str',
        'transaction_amount': 'str',
        'transaction_date': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'external_id': 'externalId',
        'locale': 'locale',
        'note': 'note',
        'payment_type_id': 'paymentTypeId',
        'reversal_external_id': 'reversalExternalId',
        'transaction_amount': 'transactionAmount',
        'transaction_date': 'transactionDate'
    }

    def __init__(self, date_format=None, external_id=None, locale=None, note=None, payment_type_id=None, reversal_external_id=None, transaction_amount=None, transaction_date=None):  # noqa: E501
        """PostLoansLoanIdTransactionsResponseChanges - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._external_id = None
        self._locale = None
        self._note = None
        self._payment_type_id = None
        self._reversal_external_id = None
        self._transaction_amount = None
        self._transaction_date = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if external_id is not None:
            self.external_id = external_id
        if locale is not None:
            self.locale = locale
        if note is not None:
            self.note = note
        if payment_type_id is not None:
            self.payment_type_id = payment_type_id
        if reversal_external_id is not None:
            self.reversal_external_id = reversal_external_id
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if transaction_date is not None:
            self.transaction_date = transaction_date

    @property
    def date_format(self):
        """Gets the date_format of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The date_format of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostLoansLoanIdTransactionsResponseChanges.


        :param date_format: The date_format of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def external_id(self):
        """Gets the external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PostLoansLoanIdTransactionsResponseChanges.


        :param external_id: The external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def locale(self):
        """Gets the locale of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The locale of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostLoansLoanIdTransactionsResponseChanges.


        :param locale: The locale of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def note(self):
        """Gets the note of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The note of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PostLoansLoanIdTransactionsResponseChanges.


        :param note: The note of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def payment_type_id(self):
        """Gets the payment_type_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The payment_type_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: int
        """
        return self._payment_type_id

    @payment_type_id.setter
    def payment_type_id(self, payment_type_id):
        """Sets the payment_type_id of this PostLoansLoanIdTransactionsResponseChanges.


        :param payment_type_id: The payment_type_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: int
        """

        self._payment_type_id = payment_type_id

    @property
    def reversal_external_id(self):
        """Gets the reversal_external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The reversal_external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._reversal_external_id

    @reversal_external_id.setter
    def reversal_external_id(self, reversal_external_id):
        """Sets the reversal_external_id of this PostLoansLoanIdTransactionsResponseChanges.


        :param reversal_external_id: The reversal_external_id of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._reversal_external_id = reversal_external_id

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The transaction_amount of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PostLoansLoanIdTransactionsResponseChanges.


        :param transaction_amount: The transaction_amount of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._transaction_amount = transaction_amount

    @property
    def transaction_date(self):
        """Gets the transaction_date of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501


        :return: The transaction_date of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this PostLoansLoanIdTransactionsResponseChanges.


        :param transaction_date: The transaction_date of this PostLoansLoanIdTransactionsResponseChanges.  # noqa: E501
        :type: str
        """

        self._transaction_date = transaction_date

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
        if issubclass(PostLoansLoanIdTransactionsResponseChanges, dict):
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
        if not isinstance(other, PostLoansLoanIdTransactionsResponseChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
