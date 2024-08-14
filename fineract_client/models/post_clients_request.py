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

class PostClientsRequest(object):
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
        'activation_date': 'str',
        'active': 'bool',
        'address': 'list[PostClientsAddressRequest]',
        'datatables': 'list[PostClientsDatatable]',
        'date_format': 'str',
        'date_of_birth': 'date',
        'email_address': 'str',
        'external_id': 'str',
        'firstname': 'str',
        'fullname': 'str',
        'group_id': 'int',
        'lastname': 'str',
        'legal_form_id': 'int',
        'locale': 'str',
        'middlename': 'str',
        'mobile_no': 'str',
        'office_id': 'int'
    }

    attribute_map = {
        'activation_date': 'activationDate',
        'active': 'active',
        'address': 'address',
        'datatables': 'datatables',
        'date_format': 'dateFormat',
        'date_of_birth': 'dateOfBirth',
        'email_address': 'emailAddress',
        'external_id': 'externalId',
        'firstname': 'firstname',
        'fullname': 'fullname',
        'group_id': 'groupId',
        'lastname': 'lastname',
        'legal_form_id': 'legalFormId',
        'locale': 'locale',
        'middlename': 'middlename',
        'mobile_no': 'mobileNo',
        'office_id': 'officeId'
    }

    def __init__(self, activation_date=None, active=None, address=None, datatables=None, date_format=None, date_of_birth=None, email_address=None, external_id=None, firstname=None, fullname=None, group_id=None, lastname=None, legal_form_id=None, locale=None, middlename=None, mobile_no=None, office_id=None):  # noqa: E501
        """PostClientsRequest - a model defined in Swagger"""  # noqa: E501
        self._activation_date = None
        self._active = None
        self._address = None
        self._datatables = None
        self._date_format = None
        self._date_of_birth = None
        self._email_address = None
        self._external_id = None
        self._firstname = None
        self._fullname = None
        self._group_id = None
        self._lastname = None
        self._legal_form_id = None
        self._locale = None
        self._middlename = None
        self._mobile_no = None
        self._office_id = None
        self.discriminator = None
        if activation_date is not None:
            self.activation_date = activation_date
        if active is not None:
            self.active = active
        if address is not None:
            self.address = address
        if datatables is not None:
            self.datatables = datatables
        if date_format is not None:
            self.date_format = date_format
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if email_address is not None:
            self.email_address = email_address
        if external_id is not None:
            self.external_id = external_id
        if firstname is not None:
            self.firstname = firstname
        if fullname is not None:
            self.fullname = fullname
        if group_id is not None:
            self.group_id = group_id
        if lastname is not None:
            self.lastname = lastname
        if legal_form_id is not None:
            self.legal_form_id = legal_form_id
        if locale is not None:
            self.locale = locale
        if middlename is not None:
            self.middlename = middlename
        if mobile_no is not None:
            self.mobile_no = mobile_no
        if office_id is not None:
            self.office_id = office_id

    @property
    def activation_date(self):
        """Gets the activation_date of this PostClientsRequest.  # noqa: E501


        :return: The activation_date of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._activation_date

    @activation_date.setter
    def activation_date(self, activation_date):
        """Sets the activation_date of this PostClientsRequest.


        :param activation_date: The activation_date of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._activation_date = activation_date

    @property
    def active(self):
        """Gets the active of this PostClientsRequest.  # noqa: E501


        :return: The active of this PostClientsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PostClientsRequest.


        :param active: The active of this PostClientsRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def address(self):
        """Gets the address of this PostClientsRequest.  # noqa: E501

        Address requests  # noqa: E501

        :return: The address of this PostClientsRequest.  # noqa: E501
        :rtype: list[PostClientsAddressRequest]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PostClientsRequest.

        Address requests  # noqa: E501

        :param address: The address of this PostClientsRequest.  # noqa: E501
        :type: list[PostClientsAddressRequest]
        """

        self._address = address

    @property
    def datatables(self):
        """Gets the datatables of this PostClientsRequest.  # noqa: E501

        List of PostClientsDatatable  # noqa: E501

        :return: The datatables of this PostClientsRequest.  # noqa: E501
        :rtype: list[PostClientsDatatable]
        """
        return self._datatables

    @datatables.setter
    def datatables(self, datatables):
        """Sets the datatables of this PostClientsRequest.

        List of PostClientsDatatable  # noqa: E501

        :param datatables: The datatables of this PostClientsRequest.  # noqa: E501
        :type: list[PostClientsDatatable]
        """

        self._datatables = datatables

    @property
    def date_format(self):
        """Gets the date_format of this PostClientsRequest.  # noqa: E501


        :return: The date_format of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostClientsRequest.


        :param date_format: The date_format of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PostClientsRequest.  # noqa: E501


        :return: The date_of_birth of this PostClientsRequest.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PostClientsRequest.


        :param date_of_birth: The date_of_birth of this PostClientsRequest.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def email_address(self):
        """Gets the email_address of this PostClientsRequest.  # noqa: E501


        :return: The email_address of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this PostClientsRequest.


        :param email_address: The email_address of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def external_id(self):
        """Gets the external_id of this PostClientsRequest.  # noqa: E501


        :return: The external_id of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PostClientsRequest.


        :param external_id: The external_id of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def firstname(self):
        """Gets the firstname of this PostClientsRequest.  # noqa: E501


        :return: The firstname of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this PostClientsRequest.


        :param firstname: The firstname of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def fullname(self):
        """Gets the fullname of this PostClientsRequest.  # noqa: E501


        :return: The fullname of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this PostClientsRequest.


        :param fullname: The fullname of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def group_id(self):
        """Gets the group_id of this PostClientsRequest.  # noqa: E501


        :return: The group_id of this PostClientsRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PostClientsRequest.


        :param group_id: The group_id of this PostClientsRequest.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def lastname(self):
        """Gets the lastname of this PostClientsRequest.  # noqa: E501


        :return: The lastname of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PostClientsRequest.


        :param lastname: The lastname of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def legal_form_id(self):
        """Gets the legal_form_id of this PostClientsRequest.  # noqa: E501


        :return: The legal_form_id of this PostClientsRequest.  # noqa: E501
        :rtype: int
        """
        return self._legal_form_id

    @legal_form_id.setter
    def legal_form_id(self, legal_form_id):
        """Sets the legal_form_id of this PostClientsRequest.


        :param legal_form_id: The legal_form_id of this PostClientsRequest.  # noqa: E501
        :type: int
        """

        self._legal_form_id = legal_form_id

    @property
    def locale(self):
        """Gets the locale of this PostClientsRequest.  # noqa: E501


        :return: The locale of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostClientsRequest.


        :param locale: The locale of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def middlename(self):
        """Gets the middlename of this PostClientsRequest.  # noqa: E501


        :return: The middlename of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """Sets the middlename of this PostClientsRequest.


        :param middlename: The middlename of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._middlename = middlename

    @property
    def mobile_no(self):
        """Gets the mobile_no of this PostClientsRequest.  # noqa: E501


        :return: The mobile_no of this PostClientsRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        """Sets the mobile_no of this PostClientsRequest.


        :param mobile_no: The mobile_no of this PostClientsRequest.  # noqa: E501
        :type: str
        """

        self._mobile_no = mobile_no

    @property
    def office_id(self):
        """Gets the office_id of this PostClientsRequest.  # noqa: E501


        :return: The office_id of this PostClientsRequest.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this PostClientsRequest.


        :param office_id: The office_id of this PostClientsRequest.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

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
        if issubclass(PostClientsRequest, dict):
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
        if not isinstance(other, PostClientsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
