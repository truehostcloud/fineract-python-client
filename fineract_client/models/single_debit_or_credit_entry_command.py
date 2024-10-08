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

class SingleDebitOrCreditEntryCommand(object):
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
        'amount': 'float',
        'comments': 'str',
        'comments_changed': 'bool',
        'gl_account_id': 'int',
        'gl_account_id_changed': 'bool',
        'gl_amount_changed': 'bool',
        'parameters_passed_in_request': 'list[str]'
    }

    attribute_map = {
        'amount': 'amount',
        'comments': 'comments',
        'comments_changed': 'commentsChanged',
        'gl_account_id': 'glAccountId',
        'gl_account_id_changed': 'glAccountIdChanged',
        'gl_amount_changed': 'glAmountChanged',
        'parameters_passed_in_request': 'parametersPassedInRequest'
    }

    def __init__(self, amount=None, comments=None, comments_changed=None, gl_account_id=None, gl_account_id_changed=None, gl_amount_changed=None, parameters_passed_in_request=None):  # noqa: E501
        """SingleDebitOrCreditEntryCommand - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._comments = None
        self._comments_changed = None
        self._gl_account_id = None
        self._gl_account_id_changed = None
        self._gl_amount_changed = None
        self._parameters_passed_in_request = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if comments is not None:
            self.comments = comments
        if comments_changed is not None:
            self.comments_changed = comments_changed
        if gl_account_id is not None:
            self.gl_account_id = gl_account_id
        if gl_account_id_changed is not None:
            self.gl_account_id_changed = gl_account_id_changed
        if gl_amount_changed is not None:
            self.gl_amount_changed = gl_amount_changed
        if parameters_passed_in_request is not None:
            self.parameters_passed_in_request = parameters_passed_in_request

    @property
    def amount(self):
        """Gets the amount of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The amount of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SingleDebitOrCreditEntryCommand.


        :param amount: The amount of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def comments(self):
        """Gets the comments of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The comments of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this SingleDebitOrCreditEntryCommand.


        :param comments: The comments of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def comments_changed(self):
        """Gets the comments_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The comments_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: bool
        """
        return self._comments_changed

    @comments_changed.setter
    def comments_changed(self, comments_changed):
        """Sets the comments_changed of this SingleDebitOrCreditEntryCommand.


        :param comments_changed: The comments_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: bool
        """

        self._comments_changed = comments_changed

    @property
    def gl_account_id(self):
        """Gets the gl_account_id of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The gl_account_id of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: int
        """
        return self._gl_account_id

    @gl_account_id.setter
    def gl_account_id(self, gl_account_id):
        """Sets the gl_account_id of this SingleDebitOrCreditEntryCommand.


        :param gl_account_id: The gl_account_id of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: int
        """

        self._gl_account_id = gl_account_id

    @property
    def gl_account_id_changed(self):
        """Gets the gl_account_id_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The gl_account_id_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: bool
        """
        return self._gl_account_id_changed

    @gl_account_id_changed.setter
    def gl_account_id_changed(self, gl_account_id_changed):
        """Sets the gl_account_id_changed of this SingleDebitOrCreditEntryCommand.


        :param gl_account_id_changed: The gl_account_id_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: bool
        """

        self._gl_account_id_changed = gl_account_id_changed

    @property
    def gl_amount_changed(self):
        """Gets the gl_amount_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The gl_amount_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: bool
        """
        return self._gl_amount_changed

    @gl_amount_changed.setter
    def gl_amount_changed(self, gl_amount_changed):
        """Sets the gl_amount_changed of this SingleDebitOrCreditEntryCommand.


        :param gl_amount_changed: The gl_amount_changed of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: bool
        """

        self._gl_amount_changed = gl_amount_changed

    @property
    def parameters_passed_in_request(self):
        """Gets the parameters_passed_in_request of this SingleDebitOrCreditEntryCommand.  # noqa: E501


        :return: The parameters_passed_in_request of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters_passed_in_request

    @parameters_passed_in_request.setter
    def parameters_passed_in_request(self, parameters_passed_in_request):
        """Sets the parameters_passed_in_request of this SingleDebitOrCreditEntryCommand.


        :param parameters_passed_in_request: The parameters_passed_in_request of this SingleDebitOrCreditEntryCommand.  # noqa: E501
        :type: list[str]
        """

        self._parameters_passed_in_request = parameters_passed_in_request

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
        if issubclass(SingleDebitOrCreditEntryCommand, dict):
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
        if not isinstance(other, SingleDebitOrCreditEntryCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
