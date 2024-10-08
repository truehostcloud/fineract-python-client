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

class GetMakerCheckerResponse(object):
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
        'action_name': 'str',
        'checked_on_date': 'datetime',
        'checker': 'str',
        'client_id': 'int',
        'client_name': 'str',
        'command_as_json': 'str',
        'entity_name': 'str',
        'group_level_name': 'str',
        'group_name': 'str',
        'id': 'int',
        'loan_account_no': 'str',
        'loan_id': 'int',
        'made_on_date': 'datetime',
        'maker': 'str',
        'office_name': 'str',
        'processing_result': 'str',
        'resource_id': 'int',
        'savings_account_no': 'str',
        'subresource_id': 'int',
        'url': 'str'
    }

    attribute_map = {
        'action_name': 'actionName',
        'checked_on_date': 'checkedOnDate',
        'checker': 'checker',
        'client_id': 'clientId',
        'client_name': 'clientName',
        'command_as_json': 'commandAsJson',
        'entity_name': 'entityName',
        'group_level_name': 'groupLevelName',
        'group_name': 'groupName',
        'id': 'id',
        'loan_account_no': 'loanAccountNo',
        'loan_id': 'loanId',
        'made_on_date': 'madeOnDate',
        'maker': 'maker',
        'office_name': 'officeName',
        'processing_result': 'processingResult',
        'resource_id': 'resourceId',
        'savings_account_no': 'savingsAccountNo',
        'subresource_id': 'subresourceId',
        'url': 'url'
    }

    def __init__(self, action_name=None, checked_on_date=None, checker=None, client_id=None, client_name=None, command_as_json=None, entity_name=None, group_level_name=None, group_name=None, id=None, loan_account_no=None, loan_id=None, made_on_date=None, maker=None, office_name=None, processing_result=None, resource_id=None, savings_account_no=None, subresource_id=None, url=None):  # noqa: E501
        """GetMakerCheckerResponse - a model defined in Swagger"""  # noqa: E501
        self._action_name = None
        self._checked_on_date = None
        self._checker = None
        self._client_id = None
        self._client_name = None
        self._command_as_json = None
        self._entity_name = None
        self._group_level_name = None
        self._group_name = None
        self._id = None
        self._loan_account_no = None
        self._loan_id = None
        self._made_on_date = None
        self._maker = None
        self._office_name = None
        self._processing_result = None
        self._resource_id = None
        self._savings_account_no = None
        self._subresource_id = None
        self._url = None
        self.discriminator = None
        if action_name is not None:
            self.action_name = action_name
        if checked_on_date is not None:
            self.checked_on_date = checked_on_date
        if checker is not None:
            self.checker = checker
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if command_as_json is not None:
            self.command_as_json = command_as_json
        if entity_name is not None:
            self.entity_name = entity_name
        if group_level_name is not None:
            self.group_level_name = group_level_name
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if loan_account_no is not None:
            self.loan_account_no = loan_account_no
        if loan_id is not None:
            self.loan_id = loan_id
        if made_on_date is not None:
            self.made_on_date = made_on_date
        if maker is not None:
            self.maker = maker
        if office_name is not None:
            self.office_name = office_name
        if processing_result is not None:
            self.processing_result = processing_result
        if resource_id is not None:
            self.resource_id = resource_id
        if savings_account_no is not None:
            self.savings_account_no = savings_account_no
        if subresource_id is not None:
            self.subresource_id = subresource_id
        if url is not None:
            self.url = url

    @property
    def action_name(self):
        """Gets the action_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The action_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this GetMakerCheckerResponse.


        :param action_name: The action_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._action_name = action_name

    @property
    def checked_on_date(self):
        """Gets the checked_on_date of this GetMakerCheckerResponse.  # noqa: E501


        :return: The checked_on_date of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._checked_on_date

    @checked_on_date.setter
    def checked_on_date(self, checked_on_date):
        """Sets the checked_on_date of this GetMakerCheckerResponse.


        :param checked_on_date: The checked_on_date of this GetMakerCheckerResponse.  # noqa: E501
        :type: datetime
        """

        self._checked_on_date = checked_on_date

    @property
    def checker(self):
        """Gets the checker of this GetMakerCheckerResponse.  # noqa: E501


        :return: The checker of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._checker

    @checker.setter
    def checker(self, checker):
        """Sets the checker of this GetMakerCheckerResponse.


        :param checker: The checker of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._checker = checker

    @property
    def client_id(self):
        """Gets the client_id of this GetMakerCheckerResponse.  # noqa: E501


        :return: The client_id of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetMakerCheckerResponse.


        :param client_id: The client_id of this GetMakerCheckerResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The client_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this GetMakerCheckerResponse.


        :param client_name: The client_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def command_as_json(self):
        """Gets the command_as_json of this GetMakerCheckerResponse.  # noqa: E501


        :return: The command_as_json of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._command_as_json

    @command_as_json.setter
    def command_as_json(self, command_as_json):
        """Sets the command_as_json of this GetMakerCheckerResponse.


        :param command_as_json: The command_as_json of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._command_as_json = command_as_json

    @property
    def entity_name(self):
        """Gets the entity_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The entity_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this GetMakerCheckerResponse.


        :param entity_name: The entity_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def group_level_name(self):
        """Gets the group_level_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The group_level_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_level_name

    @group_level_name.setter
    def group_level_name(self, group_level_name):
        """Sets the group_level_name of this GetMakerCheckerResponse.


        :param group_level_name: The group_level_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._group_level_name = group_level_name

    @property
    def group_name(self):
        """Gets the group_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The group_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this GetMakerCheckerResponse.


        :param group_name: The group_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this GetMakerCheckerResponse.  # noqa: E501


        :return: The id of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetMakerCheckerResponse.


        :param id: The id of this GetMakerCheckerResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def loan_account_no(self):
        """Gets the loan_account_no of this GetMakerCheckerResponse.  # noqa: E501


        :return: The loan_account_no of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._loan_account_no

    @loan_account_no.setter
    def loan_account_no(self, loan_account_no):
        """Sets the loan_account_no of this GetMakerCheckerResponse.


        :param loan_account_no: The loan_account_no of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._loan_account_no = loan_account_no

    @property
    def loan_id(self):
        """Gets the loan_id of this GetMakerCheckerResponse.  # noqa: E501


        :return: The loan_id of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this GetMakerCheckerResponse.


        :param loan_id: The loan_id of this GetMakerCheckerResponse.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

    @property
    def made_on_date(self):
        """Gets the made_on_date of this GetMakerCheckerResponse.  # noqa: E501


        :return: The made_on_date of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._made_on_date

    @made_on_date.setter
    def made_on_date(self, made_on_date):
        """Sets the made_on_date of this GetMakerCheckerResponse.


        :param made_on_date: The made_on_date of this GetMakerCheckerResponse.  # noqa: E501
        :type: datetime
        """

        self._made_on_date = made_on_date

    @property
    def maker(self):
        """Gets the maker of this GetMakerCheckerResponse.  # noqa: E501


        :return: The maker of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._maker

    @maker.setter
    def maker(self, maker):
        """Sets the maker of this GetMakerCheckerResponse.


        :param maker: The maker of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._maker = maker

    @property
    def office_name(self):
        """Gets the office_name of this GetMakerCheckerResponse.  # noqa: E501


        :return: The office_name of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetMakerCheckerResponse.


        :param office_name: The office_name of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def processing_result(self):
        """Gets the processing_result of this GetMakerCheckerResponse.  # noqa: E501


        :return: The processing_result of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._processing_result

    @processing_result.setter
    def processing_result(self, processing_result):
        """Sets the processing_result of this GetMakerCheckerResponse.


        :param processing_result: The processing_result of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._processing_result = processing_result

    @property
    def resource_id(self):
        """Gets the resource_id of this GetMakerCheckerResponse.  # noqa: E501


        :return: The resource_id of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this GetMakerCheckerResponse.


        :param resource_id: The resource_id of this GetMakerCheckerResponse.  # noqa: E501
        :type: int
        """

        self._resource_id = resource_id

    @property
    def savings_account_no(self):
        """Gets the savings_account_no of this GetMakerCheckerResponse.  # noqa: E501


        :return: The savings_account_no of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._savings_account_no

    @savings_account_no.setter
    def savings_account_no(self, savings_account_no):
        """Sets the savings_account_no of this GetMakerCheckerResponse.


        :param savings_account_no: The savings_account_no of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._savings_account_no = savings_account_no

    @property
    def subresource_id(self):
        """Gets the subresource_id of this GetMakerCheckerResponse.  # noqa: E501


        :return: The subresource_id of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: int
        """
        return self._subresource_id

    @subresource_id.setter
    def subresource_id(self, subresource_id):
        """Sets the subresource_id of this GetMakerCheckerResponse.


        :param subresource_id: The subresource_id of this GetMakerCheckerResponse.  # noqa: E501
        :type: int
        """

        self._subresource_id = subresource_id

    @property
    def url(self):
        """Gets the url of this GetMakerCheckerResponse.  # noqa: E501


        :return: The url of this GetMakerCheckerResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetMakerCheckerResponse.


        :param url: The url of this GetMakerCheckerResponse.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(GetMakerCheckerResponse, dict):
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
        if not isinstance(other, GetMakerCheckerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
