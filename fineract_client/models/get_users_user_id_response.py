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

class GetUsersUserIdResponse(object):
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
        'available_roles': 'list[RoleData]',
        'email': 'str',
        'firstname': 'str',
        'id': 'int',
        'lastname': 'str',
        'office_id': 'int',
        'office_name': 'str',
        'password_never_expires': 'bool',
        'selected_roles': 'list[RoleData]',
        'staff': 'StaffData',
        'username': 'str'
    }

    attribute_map = {
        'available_roles': 'availableRoles',
        'email': 'email',
        'firstname': 'firstname',
        'id': 'id',
        'lastname': 'lastname',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'password_never_expires': 'passwordNeverExpires',
        'selected_roles': 'selectedRoles',
        'staff': 'staff',
        'username': 'username'
    }

    def __init__(self, available_roles=None, email=None, firstname=None, id=None, lastname=None, office_id=None, office_name=None, password_never_expires=None, selected_roles=None, staff=None, username=None):  # noqa: E501
        """GetUsersUserIdResponse - a model defined in Swagger"""  # noqa: E501
        self._available_roles = None
        self._email = None
        self._firstname = None
        self._id = None
        self._lastname = None
        self._office_id = None
        self._office_name = None
        self._password_never_expires = None
        self._selected_roles = None
        self._staff = None
        self._username = None
        self.discriminator = None
        if available_roles is not None:
            self.available_roles = available_roles
        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if id is not None:
            self.id = id
        if lastname is not None:
            self.lastname = lastname
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires
        if selected_roles is not None:
            self.selected_roles = selected_roles
        if staff is not None:
            self.staff = staff
        if username is not None:
            self.username = username

    @property
    def available_roles(self):
        """Gets the available_roles of this GetUsersUserIdResponse.  # noqa: E501


        :return: The available_roles of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: list[RoleData]
        """
        return self._available_roles

    @available_roles.setter
    def available_roles(self, available_roles):
        """Sets the available_roles of this GetUsersUserIdResponse.


        :param available_roles: The available_roles of this GetUsersUserIdResponse.  # noqa: E501
        :type: list[RoleData]
        """

        self._available_roles = available_roles

    @property
    def email(self):
        """Gets the email of this GetUsersUserIdResponse.  # noqa: E501


        :return: The email of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetUsersUserIdResponse.


        :param email: The email of this GetUsersUserIdResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this GetUsersUserIdResponse.  # noqa: E501


        :return: The firstname of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this GetUsersUserIdResponse.


        :param firstname: The firstname of this GetUsersUserIdResponse.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def id(self):
        """Gets the id of this GetUsersUserIdResponse.  # noqa: E501


        :return: The id of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetUsersUserIdResponse.


        :param id: The id of this GetUsersUserIdResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lastname(self):
        """Gets the lastname of this GetUsersUserIdResponse.  # noqa: E501


        :return: The lastname of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this GetUsersUserIdResponse.


        :param lastname: The lastname of this GetUsersUserIdResponse.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def office_id(self):
        """Gets the office_id of this GetUsersUserIdResponse.  # noqa: E501


        :return: The office_id of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetUsersUserIdResponse.


        :param office_id: The office_id of this GetUsersUserIdResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetUsersUserIdResponse.  # noqa: E501


        :return: The office_name of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetUsersUserIdResponse.


        :param office_name: The office_name of this GetUsersUserIdResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this GetUsersUserIdResponse.  # noqa: E501


        :return: The password_never_expires of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this GetUsersUserIdResponse.


        :param password_never_expires: The password_never_expires of this GetUsersUserIdResponse.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

    @property
    def selected_roles(self):
        """Gets the selected_roles of this GetUsersUserIdResponse.  # noqa: E501


        :return: The selected_roles of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: list[RoleData]
        """
        return self._selected_roles

    @selected_roles.setter
    def selected_roles(self, selected_roles):
        """Sets the selected_roles of this GetUsersUserIdResponse.


        :param selected_roles: The selected_roles of this GetUsersUserIdResponse.  # noqa: E501
        :type: list[RoleData]
        """

        self._selected_roles = selected_roles

    @property
    def staff(self):
        """Gets the staff of this GetUsersUserIdResponse.  # noqa: E501


        :return: The staff of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: StaffData
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """Sets the staff of this GetUsersUserIdResponse.


        :param staff: The staff of this GetUsersUserIdResponse.  # noqa: E501
        :type: StaffData
        """

        self._staff = staff

    @property
    def username(self):
        """Gets the username of this GetUsersUserIdResponse.  # noqa: E501


        :return: The username of this GetUsersUserIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetUsersUserIdResponse.


        :param username: The username of this GetUsersUserIdResponse.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(GetUsersUserIdResponse, dict):
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
        if not isinstance(other, GetUsersUserIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
