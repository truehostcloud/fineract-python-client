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

class InteropIdentifiersResponseData(object):
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
        'changes': 'dict(str, object)',
        'client_id': 'int',
        'command_id': 'int',
        'credit_bureau_report_data': 'dict(str, object)',
        'glim_id': 'int',
        'group_id': 'int',
        'gsim_id': 'int',
        'loan_id': 'int',
        'office_id': 'int',
        'product_id': 'int',
        'resource_external_id': 'ExternalId',
        'resource_id': 'int',
        'resource_identifier': 'str',
        'rollback_transaction': 'bool',
        'savings_id': 'int',
        'sub_resource_external_id': 'ExternalId',
        'sub_resource_id': 'int',
        'transaction_id': 'str'
    }

    attribute_map = {
        'changes': 'changes',
        'client_id': 'clientId',
        'command_id': 'commandId',
        'credit_bureau_report_data': 'creditBureauReportData',
        'glim_id': 'glimId',
        'group_id': 'groupId',
        'gsim_id': 'gsimId',
        'loan_id': 'loanId',
        'office_id': 'officeId',
        'product_id': 'productId',
        'resource_external_id': 'resourceExternalId',
        'resource_id': 'resourceId',
        'resource_identifier': 'resourceIdentifier',
        'rollback_transaction': 'rollbackTransaction',
        'savings_id': 'savingsId',
        'sub_resource_external_id': 'subResourceExternalId',
        'sub_resource_id': 'subResourceId',
        'transaction_id': 'transactionId'
    }

    def __init__(self, changes=None, client_id=None, command_id=None, credit_bureau_report_data=None, glim_id=None, group_id=None, gsim_id=None, loan_id=None, office_id=None, product_id=None, resource_external_id=None, resource_id=None, resource_identifier=None, rollback_transaction=None, savings_id=None, sub_resource_external_id=None, sub_resource_id=None, transaction_id=None):  # noqa: E501
        """InteropIdentifiersResponseData - a model defined in Swagger"""  # noqa: E501
        self._changes = None
        self._client_id = None
        self._command_id = None
        self._credit_bureau_report_data = None
        self._glim_id = None
        self._group_id = None
        self._gsim_id = None
        self._loan_id = None
        self._office_id = None
        self._product_id = None
        self._resource_external_id = None
        self._resource_id = None
        self._resource_identifier = None
        self._rollback_transaction = None
        self._savings_id = None
        self._sub_resource_external_id = None
        self._sub_resource_id = None
        self._transaction_id = None
        self.discriminator = None
        if changes is not None:
            self.changes = changes
        if client_id is not None:
            self.client_id = client_id
        if command_id is not None:
            self.command_id = command_id
        if credit_bureau_report_data is not None:
            self.credit_bureau_report_data = credit_bureau_report_data
        if glim_id is not None:
            self.glim_id = glim_id
        if group_id is not None:
            self.group_id = group_id
        if gsim_id is not None:
            self.gsim_id = gsim_id
        if loan_id is not None:
            self.loan_id = loan_id
        if office_id is not None:
            self.office_id = office_id
        if product_id is not None:
            self.product_id = product_id
        if resource_external_id is not None:
            self.resource_external_id = resource_external_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_identifier is not None:
            self.resource_identifier = resource_identifier
        if rollback_transaction is not None:
            self.rollback_transaction = rollback_transaction
        if savings_id is not None:
            self.savings_id = savings_id
        if sub_resource_external_id is not None:
            self.sub_resource_external_id = sub_resource_external_id
        if sub_resource_id is not None:
            self.sub_resource_id = sub_resource_id
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def changes(self):
        """Gets the changes of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The changes of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this InteropIdentifiersResponseData.


        :param changes: The changes of this InteropIdentifiersResponseData.  # noqa: E501
        :type: dict(str, object)
        """

        self._changes = changes

    @property
    def client_id(self):
        """Gets the client_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The client_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InteropIdentifiersResponseData.


        :param client_id: The client_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def command_id(self):
        """Gets the command_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The command_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this InteropIdentifiersResponseData.


        :param command_id: The command_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._command_id = command_id

    @property
    def credit_bureau_report_data(self):
        """Gets the credit_bureau_report_data of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The credit_bureau_report_data of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._credit_bureau_report_data

    @credit_bureau_report_data.setter
    def credit_bureau_report_data(self, credit_bureau_report_data):
        """Sets the credit_bureau_report_data of this InteropIdentifiersResponseData.


        :param credit_bureau_report_data: The credit_bureau_report_data of this InteropIdentifiersResponseData.  # noqa: E501
        :type: dict(str, object)
        """

        self._credit_bureau_report_data = credit_bureau_report_data

    @property
    def glim_id(self):
        """Gets the glim_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The glim_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._glim_id

    @glim_id.setter
    def glim_id(self, glim_id):
        """Sets the glim_id of this InteropIdentifiersResponseData.


        :param glim_id: The glim_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._glim_id = glim_id

    @property
    def group_id(self):
        """Gets the group_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The group_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InteropIdentifiersResponseData.


        :param group_id: The group_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def gsim_id(self):
        """Gets the gsim_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The gsim_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._gsim_id

    @gsim_id.setter
    def gsim_id(self, gsim_id):
        """Sets the gsim_id of this InteropIdentifiersResponseData.


        :param gsim_id: The gsim_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._gsim_id = gsim_id

    @property
    def loan_id(self):
        """Gets the loan_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The loan_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this InteropIdentifiersResponseData.


        :param loan_id: The loan_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

    @property
    def office_id(self):
        """Gets the office_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The office_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this InteropIdentifiersResponseData.


        :param office_id: The office_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def product_id(self):
        """Gets the product_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The product_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this InteropIdentifiersResponseData.


        :param product_id: The product_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def resource_external_id(self):
        """Gets the resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: ExternalId
        """
        return self._resource_external_id

    @resource_external_id.setter
    def resource_external_id(self, resource_external_id):
        """Sets the resource_external_id of this InteropIdentifiersResponseData.


        :param resource_external_id: The resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: ExternalId
        """

        self._resource_external_id = resource_external_id

    @property
    def resource_id(self):
        """Gets the resource_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The resource_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this InteropIdentifiersResponseData.


        :param resource_id: The resource_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def resource_identifier(self):
        """Gets the resource_identifier of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The resource_identifier of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: str
        """
        return self._resource_identifier

    @resource_identifier.setter
    def resource_identifier(self, resource_identifier):
        """Sets the resource_identifier of this InteropIdentifiersResponseData.


        :param resource_identifier: The resource_identifier of this InteropIdentifiersResponseData.  # noqa: E501
        :type: str
        """

        self._resource_identifier = resource_identifier

    @property
    def rollback_transaction(self):
        """Gets the rollback_transaction of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The rollback_transaction of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._rollback_transaction

    @rollback_transaction.setter
    def rollback_transaction(self, rollback_transaction):
        """Sets the rollback_transaction of this InteropIdentifiersResponseData.


        :param rollback_transaction: The rollback_transaction of this InteropIdentifiersResponseData.  # noqa: E501
        :type: bool
        """

        self._rollback_transaction = rollback_transaction

    @property
    def savings_id(self):
        """Gets the savings_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The savings_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._savings_id

    @savings_id.setter
    def savings_id(self, savings_id):
        """Sets the savings_id of this InteropIdentifiersResponseData.


        :param savings_id: The savings_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._savings_id = savings_id

    @property
    def sub_resource_external_id(self):
        """Gets the sub_resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The sub_resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: ExternalId
        """
        return self._sub_resource_external_id

    @sub_resource_external_id.setter
    def sub_resource_external_id(self, sub_resource_external_id):
        """Sets the sub_resource_external_id of this InteropIdentifiersResponseData.


        :param sub_resource_external_id: The sub_resource_external_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: ExternalId
        """

        self._sub_resource_external_id = sub_resource_external_id

    @property
    def sub_resource_id(self):
        """Gets the sub_resource_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The sub_resource_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: int
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        """Sets the sub_resource_id of this InteropIdentifiersResponseData.


        :param sub_resource_id: The sub_resource_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: int
        """

        self._sub_resource_id = sub_resource_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InteropIdentifiersResponseData.  # noqa: E501


        :return: The transaction_id of this InteropIdentifiersResponseData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InteropIdentifiersResponseData.


        :param transaction_id: The transaction_id of this InteropIdentifiersResponseData.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

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
        if issubclass(InteropIdentifiersResponseData, dict):
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
        if not isinstance(other, InteropIdentifiersResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
