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

class GetStandingInstructionHistoryPageItemsResponse(object):
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
        'error_log': 'str',
        'execution_time': 'date',
        'from_account': 'GetStandingInstructionHistoryFromAccount',
        'from_account_type': 'GetFromAccountTypeStandingInstructionSwagger',
        'from_client': 'GetStandingInstructionHistoryPageItemsFromClient',
        'from_office': 'GetFromOfficeStandingInstructionSwagger',
        'name': 'str',
        'standing_instruction_id': 'int',
        'status': 'str',
        'to_account': 'GetStandingInstructionHistoryToAccount',
        'to_account_type': 'GetToAccountTypeStandingInstructionSwagger',
        'to_client': 'GetStandingInstructionHistoryToClient',
        'to_office': 'GetToOfficeStandingInstructionSwagger'
    }

    attribute_map = {
        'amount': 'amount',
        'error_log': 'errorLog',
        'execution_time': 'executionTime',
        'from_account': 'fromAccount',
        'from_account_type': 'fromAccountType',
        'from_client': 'fromClient',
        'from_office': 'fromOffice',
        'name': 'name',
        'standing_instruction_id': 'standingInstructionId',
        'status': 'status',
        'to_account': 'toAccount',
        'to_account_type': 'toAccountType',
        'to_client': 'toClient',
        'to_office': 'toOffice'
    }

    def __init__(self, amount=None, error_log=None, execution_time=None, from_account=None, from_account_type=None, from_client=None, from_office=None, name=None, standing_instruction_id=None, status=None, to_account=None, to_account_type=None, to_client=None, to_office=None):  # noqa: E501
        """GetStandingInstructionHistoryPageItemsResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._error_log = None
        self._execution_time = None
        self._from_account = None
        self._from_account_type = None
        self._from_client = None
        self._from_office = None
        self._name = None
        self._standing_instruction_id = None
        self._status = None
        self._to_account = None
        self._to_account_type = None
        self._to_client = None
        self._to_office = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if error_log is not None:
            self.error_log = error_log
        if execution_time is not None:
            self.execution_time = execution_time
        if from_account is not None:
            self.from_account = from_account
        if from_account_type is not None:
            self.from_account_type = from_account_type
        if from_client is not None:
            self.from_client = from_client
        if from_office is not None:
            self.from_office = from_office
        if name is not None:
            self.name = name
        if standing_instruction_id is not None:
            self.standing_instruction_id = standing_instruction_id
        if status is not None:
            self.status = status
        if to_account is not None:
            self.to_account = to_account
        if to_account_type is not None:
            self.to_account_type = to_account_type
        if to_client is not None:
            self.to_client = to_client
        if to_office is not None:
            self.to_office = to_office

    @property
    def amount(self):
        """Gets the amount of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The amount of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetStandingInstructionHistoryPageItemsResponse.


        :param amount: The amount of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def error_log(self):
        """Gets the error_log of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The error_log of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_log

    @error_log.setter
    def error_log(self, error_log):
        """Sets the error_log of this GetStandingInstructionHistoryPageItemsResponse.


        :param error_log: The error_log of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: str
        """

        self._error_log = error_log

    @property
    def execution_time(self):
        """Gets the execution_time of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The execution_time of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: date
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this GetStandingInstructionHistoryPageItemsResponse.


        :param execution_time: The execution_time of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: date
        """

        self._execution_time = execution_time

    @property
    def from_account(self):
        """Gets the from_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The from_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetStandingInstructionHistoryFromAccount
        """
        return self._from_account

    @from_account.setter
    def from_account(self, from_account):
        """Sets the from_account of this GetStandingInstructionHistoryPageItemsResponse.


        :param from_account: The from_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetStandingInstructionHistoryFromAccount
        """

        self._from_account = from_account

    @property
    def from_account_type(self):
        """Gets the from_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The from_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetFromAccountTypeStandingInstructionSwagger
        """
        return self._from_account_type

    @from_account_type.setter
    def from_account_type(self, from_account_type):
        """Sets the from_account_type of this GetStandingInstructionHistoryPageItemsResponse.


        :param from_account_type: The from_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetFromAccountTypeStandingInstructionSwagger
        """

        self._from_account_type = from_account_type

    @property
    def from_client(self):
        """Gets the from_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The from_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetStandingInstructionHistoryPageItemsFromClient
        """
        return self._from_client

    @from_client.setter
    def from_client(self, from_client):
        """Sets the from_client of this GetStandingInstructionHistoryPageItemsResponse.


        :param from_client: The from_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetStandingInstructionHistoryPageItemsFromClient
        """

        self._from_client = from_client

    @property
    def from_office(self):
        """Gets the from_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The from_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetFromOfficeStandingInstructionSwagger
        """
        return self._from_office

    @from_office.setter
    def from_office(self, from_office):
        """Sets the from_office of this GetStandingInstructionHistoryPageItemsResponse.


        :param from_office: The from_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetFromOfficeStandingInstructionSwagger
        """

        self._from_office = from_office

    @property
    def name(self):
        """Gets the name of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The name of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetStandingInstructionHistoryPageItemsResponse.


        :param name: The name of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def standing_instruction_id(self):
        """Gets the standing_instruction_id of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The standing_instruction_id of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: int
        """
        return self._standing_instruction_id

    @standing_instruction_id.setter
    def standing_instruction_id(self, standing_instruction_id):
        """Sets the standing_instruction_id of this GetStandingInstructionHistoryPageItemsResponse.


        :param standing_instruction_id: The standing_instruction_id of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: int
        """

        self._standing_instruction_id = standing_instruction_id

    @property
    def status(self):
        """Gets the status of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The status of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetStandingInstructionHistoryPageItemsResponse.


        :param status: The status of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def to_account(self):
        """Gets the to_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The to_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetStandingInstructionHistoryToAccount
        """
        return self._to_account

    @to_account.setter
    def to_account(self, to_account):
        """Sets the to_account of this GetStandingInstructionHistoryPageItemsResponse.


        :param to_account: The to_account of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetStandingInstructionHistoryToAccount
        """

        self._to_account = to_account

    @property
    def to_account_type(self):
        """Gets the to_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The to_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetToAccountTypeStandingInstructionSwagger
        """
        return self._to_account_type

    @to_account_type.setter
    def to_account_type(self, to_account_type):
        """Sets the to_account_type of this GetStandingInstructionHistoryPageItemsResponse.


        :param to_account_type: The to_account_type of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetToAccountTypeStandingInstructionSwagger
        """

        self._to_account_type = to_account_type

    @property
    def to_client(self):
        """Gets the to_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The to_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetStandingInstructionHistoryToClient
        """
        return self._to_client

    @to_client.setter
    def to_client(self, to_client):
        """Sets the to_client of this GetStandingInstructionHistoryPageItemsResponse.


        :param to_client: The to_client of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetStandingInstructionHistoryToClient
        """

        self._to_client = to_client

    @property
    def to_office(self):
        """Gets the to_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501


        :return: The to_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :rtype: GetToOfficeStandingInstructionSwagger
        """
        return self._to_office

    @to_office.setter
    def to_office(self, to_office):
        """Sets the to_office of this GetStandingInstructionHistoryPageItemsResponse.


        :param to_office: The to_office of this GetStandingInstructionHistoryPageItemsResponse.  # noqa: E501
        :type: GetToOfficeStandingInstructionSwagger
        """

        self._to_office = to_office

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
        if issubclass(GetStandingInstructionHistoryPageItemsResponse, dict):
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
        if not isinstance(other, GetStandingInstructionHistoryPageItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
