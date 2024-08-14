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

class TransactionDetails(object):
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
        'note_data': 'GetResourceTypeResourceIdNotesResponse',
        'payment_details': 'PaymentDetailData',
        'transaction_id': 'int',
        'transaction_type': 'EnumOptionType'
    }

    attribute_map = {
        'note_data': 'noteData',
        'payment_details': 'paymentDetails',
        'transaction_id': 'transactionId',
        'transaction_type': 'transactionType'
    }

    def __init__(self, note_data=None, payment_details=None, transaction_id=None, transaction_type=None):  # noqa: E501
        """TransactionDetails - a model defined in Swagger"""  # noqa: E501
        self._note_data = None
        self._payment_details = None
        self._transaction_id = None
        self._transaction_type = None
        self.discriminator = None
        if note_data is not None:
            self.note_data = note_data
        if payment_details is not None:
            self.payment_details = payment_details
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_type is not None:
            self.transaction_type = transaction_type

    @property
    def note_data(self):
        """Gets the note_data of this TransactionDetails.  # noqa: E501


        :return: The note_data of this TransactionDetails.  # noqa: E501
        :rtype: GetResourceTypeResourceIdNotesResponse
        """
        return self._note_data

    @note_data.setter
    def note_data(self, note_data):
        """Sets the note_data of this TransactionDetails.


        :param note_data: The note_data of this TransactionDetails.  # noqa: E501
        :type: GetResourceTypeResourceIdNotesResponse
        """

        self._note_data = note_data

    @property
    def payment_details(self):
        """Gets the payment_details of this TransactionDetails.  # noqa: E501


        :return: The payment_details of this TransactionDetails.  # noqa: E501
        :rtype: PaymentDetailData
        """
        return self._payment_details

    @payment_details.setter
    def payment_details(self, payment_details):
        """Sets the payment_details of this TransactionDetails.


        :param payment_details: The payment_details of this TransactionDetails.  # noqa: E501
        :type: PaymentDetailData
        """

        self._payment_details = payment_details

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionDetails.  # noqa: E501


        :return: The transaction_id of this TransactionDetails.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionDetails.


        :param transaction_id: The transaction_id of this TransactionDetails.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this TransactionDetails.  # noqa: E501


        :return: The transaction_type of this TransactionDetails.  # noqa: E501
        :rtype: EnumOptionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this TransactionDetails.


        :param transaction_type: The transaction_type of this TransactionDetails.  # noqa: E501
        :type: EnumOptionType
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
        if issubclass(TransactionDetails, dict):
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
        if not isinstance(other, TransactionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
