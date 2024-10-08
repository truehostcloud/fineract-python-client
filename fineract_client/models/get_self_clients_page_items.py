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

class GetSelfClientsPageItems(object):
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
        'account_no': 'int',
        'activation_date': 'date',
        'active': 'bool',
        'display_name': 'str',
        'fullname': 'str',
        'id': 'int',
        'office_id': 'int',
        'office_name': 'str',
        'status': 'GetSelfClientsStatus'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'activation_date': 'activationDate',
        'active': 'active',
        'display_name': 'displayName',
        'fullname': 'fullname',
        'id': 'id',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'status': 'status'
    }

    def __init__(self, account_no=None, activation_date=None, active=None, display_name=None, fullname=None, id=None, office_id=None, office_name=None, status=None):  # noqa: E501
        """GetSelfClientsPageItems - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._activation_date = None
        self._active = None
        self._display_name = None
        self._fullname = None
        self._id = None
        self._office_id = None
        self._office_name = None
        self._status = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if activation_date is not None:
            self.activation_date = activation_date
        if active is not None:
            self.active = active
        if display_name is not None:
            self.display_name = display_name
        if fullname is not None:
            self.fullname = fullname
        if id is not None:
            self.id = id
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if status is not None:
            self.status = status

    @property
    def account_no(self):
        """Gets the account_no of this GetSelfClientsPageItems.  # noqa: E501


        :return: The account_no of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GetSelfClientsPageItems.


        :param account_no: The account_no of this GetSelfClientsPageItems.  # noqa: E501
        :type: int
        """

        self._account_no = account_no

    @property
    def activation_date(self):
        """Gets the activation_date of this GetSelfClientsPageItems.  # noqa: E501


        :return: The activation_date of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: date
        """
        return self._activation_date

    @activation_date.setter
    def activation_date(self, activation_date):
        """Sets the activation_date of this GetSelfClientsPageItems.


        :param activation_date: The activation_date of this GetSelfClientsPageItems.  # noqa: E501
        :type: date
        """

        self._activation_date = activation_date

    @property
    def active(self):
        """Gets the active of this GetSelfClientsPageItems.  # noqa: E501


        :return: The active of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GetSelfClientsPageItems.


        :param active: The active of this GetSelfClientsPageItems.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def display_name(self):
        """Gets the display_name of this GetSelfClientsPageItems.  # noqa: E501


        :return: The display_name of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetSelfClientsPageItems.


        :param display_name: The display_name of this GetSelfClientsPageItems.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def fullname(self):
        """Gets the fullname of this GetSelfClientsPageItems.  # noqa: E501


        :return: The fullname of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this GetSelfClientsPageItems.


        :param fullname: The fullname of this GetSelfClientsPageItems.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def id(self):
        """Gets the id of this GetSelfClientsPageItems.  # noqa: E501


        :return: The id of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSelfClientsPageItems.


        :param id: The id of this GetSelfClientsPageItems.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def office_id(self):
        """Gets the office_id of this GetSelfClientsPageItems.  # noqa: E501


        :return: The office_id of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetSelfClientsPageItems.


        :param office_id: The office_id of this GetSelfClientsPageItems.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetSelfClientsPageItems.  # noqa: E501


        :return: The office_name of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetSelfClientsPageItems.


        :param office_name: The office_name of this GetSelfClientsPageItems.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def status(self):
        """Gets the status of this GetSelfClientsPageItems.  # noqa: E501


        :return: The status of this GetSelfClientsPageItems.  # noqa: E501
        :rtype: GetSelfClientsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetSelfClientsPageItems.


        :param status: The status of this GetSelfClientsPageItems.  # noqa: E501
        :type: GetSelfClientsStatus
        """

        self._status = status

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
        if issubclass(GetSelfClientsPageItems, dict):
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
        if not isinstance(other, GetSelfClientsPageItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
