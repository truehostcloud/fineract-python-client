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

class PostLoansLoanIdChargesChargeIdResponse(object):
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
        'changes': 'PostLoansLoanIdChargesChargeIdChanges',
        'client_id': 'int',
        'loan_id': 'int',
        'office_id': 'int',
        'resource_external_id': 'str',
        'resource_id': 'int',
        'savings_id': 'int',
        'sub_resource_external_id': 'str',
        'sub_resource_id': 'int'
    }

    attribute_map = {
        'changes': 'changes',
        'client_id': 'clientId',
        'loan_id': 'loanId',
        'office_id': 'officeId',
        'resource_external_id': 'resourceExternalId',
        'resource_id': 'resourceId',
        'savings_id': 'savingsId',
        'sub_resource_external_id': 'subResourceExternalId',
        'sub_resource_id': 'subResourceId'
    }

    def __init__(self, changes=None, client_id=None, loan_id=None, office_id=None, resource_external_id=None, resource_id=None, savings_id=None, sub_resource_external_id=None, sub_resource_id=None):  # noqa: E501
        """PostLoansLoanIdChargesChargeIdResponse - a model defined in Swagger"""  # noqa: E501
        self._changes = None
        self._client_id = None
        self._loan_id = None
        self._office_id = None
        self._resource_external_id = None
        self._resource_id = None
        self._savings_id = None
        self._sub_resource_external_id = None
        self._sub_resource_id = None
        self.discriminator = None
        if changes is not None:
            self.changes = changes
        if client_id is not None:
            self.client_id = client_id
        if loan_id is not None:
            self.loan_id = loan_id
        if office_id is not None:
            self.office_id = office_id
        if resource_external_id is not None:
            self.resource_external_id = resource_external_id
        if resource_id is not None:
            self.resource_id = resource_id
        if savings_id is not None:
            self.savings_id = savings_id
        if sub_resource_external_id is not None:
            self.sub_resource_external_id = sub_resource_external_id
        if sub_resource_id is not None:
            self.sub_resource_id = sub_resource_id

    @property
    def changes(self):
        """Gets the changes of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The changes of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: PostLoansLoanIdChargesChargeIdChanges
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this PostLoansLoanIdChargesChargeIdResponse.


        :param changes: The changes of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: PostLoansLoanIdChargesChargeIdChanges
        """

        self._changes = changes

    @property
    def client_id(self):
        """Gets the client_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The client_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param client_id: The client_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def loan_id(self):
        """Gets the loan_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The loan_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param loan_id: The loan_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

    @property
    def office_id(self):
        """Gets the office_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The office_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param office_id: The office_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def resource_external_id(self):
        """Gets the resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_external_id

    @resource_external_id.setter
    def resource_external_id(self, resource_external_id):
        """Sets the resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param resource_external_id: The resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: str
        """

        self._resource_external_id = resource_external_id

    @property
    def resource_id(self):
        """Gets the resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param resource_id: The resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def savings_id(self):
        """Gets the savings_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The savings_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._savings_id

    @savings_id.setter
    def savings_id(self, savings_id):
        """Sets the savings_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param savings_id: The savings_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._savings_id = savings_id

    @property
    def sub_resource_external_id(self):
        """Gets the sub_resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The sub_resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_resource_external_id

    @sub_resource_external_id.setter
    def sub_resource_external_id(self, sub_resource_external_id):
        """Sets the sub_resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param sub_resource_external_id: The sub_resource_external_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: str
        """

        self._sub_resource_external_id = sub_resource_external_id

    @property
    def sub_resource_id(self):
        """Gets the sub_resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501


        :return: The sub_resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._sub_resource_id

    @sub_resource_id.setter
    def sub_resource_id(self, sub_resource_id):
        """Sets the sub_resource_id of this PostLoansLoanIdChargesChargeIdResponse.


        :param sub_resource_id: The sub_resource_id of this PostLoansLoanIdChargesChargeIdResponse.  # noqa: E501
        :type: int
        """

        self._sub_resource_id = sub_resource_id

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
        if issubclass(PostLoansLoanIdChargesChargeIdResponse, dict):
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
        if not isinstance(other, PostLoansLoanIdChargesChargeIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
