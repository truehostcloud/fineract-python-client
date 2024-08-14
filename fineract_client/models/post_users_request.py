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

class PostUsersRequest(object):
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
        'clients': 'list[int]',
        'email': 'str',
        'firstname': 'str',
        'is_self_service_user': 'bool',
        'lastname': 'str',
        'office_id': 'int',
        'password': 'str',
        'password_never_expires': 'bool',
        'repeat_password': 'str',
        'roles': 'list[int]',
        'send_password_to_email': 'bool',
        'staff_id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'clients': 'clients',
        'email': 'email',
        'firstname': 'firstname',
        'is_self_service_user': 'isSelfServiceUser',
        'lastname': 'lastname',
        'office_id': 'officeId',
        'password': 'password',
        'password_never_expires': 'passwordNeverExpires',
        'repeat_password': 'repeatPassword',
        'roles': 'roles',
        'send_password_to_email': 'sendPasswordToEmail',
        'staff_id': 'staffId',
        'username': 'username'
    }

    def __init__(self, clients=None, email=None, firstname=None, is_self_service_user=None, lastname=None, office_id=None, password=None, password_never_expires=None, repeat_password=None, roles=None, send_password_to_email=None, staff_id=None, username=None):  # noqa: E501
        """PostUsersRequest - a model defined in Swagger"""  # noqa: E501
        self._clients = None
        self._email = None
        self._firstname = None
        self._is_self_service_user = None
        self._lastname = None
        self._office_id = None
        self._password = None
        self._password_never_expires = None
        self._repeat_password = None
        self._roles = None
        self._send_password_to_email = None
        self._staff_id = None
        self._username = None
        self.discriminator = None
        if clients is not None:
            self.clients = clients
        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if is_self_service_user is not None:
            self.is_self_service_user = is_self_service_user
        if lastname is not None:
            self.lastname = lastname
        if office_id is not None:
            self.office_id = office_id
        if password is not None:
            self.password = password
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires
        if repeat_password is not None:
            self.repeat_password = repeat_password
        if roles is not None:
            self.roles = roles
        if send_password_to_email is not None:
            self.send_password_to_email = send_password_to_email
        if staff_id is not None:
            self.staff_id = staff_id
        if username is not None:
            self.username = username

    @property
    def clients(self):
        """Gets the clients of this PostUsersRequest.  # noqa: E501


        :return: The clients of this PostUsersRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this PostUsersRequest.


        :param clients: The clients of this PostUsersRequest.  # noqa: E501
        :type: list[int]
        """

        self._clients = clients

    @property
    def email(self):
        """Gets the email of this PostUsersRequest.  # noqa: E501


        :return: The email of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostUsersRequest.


        :param email: The email of this PostUsersRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this PostUsersRequest.  # noqa: E501


        :return: The firstname of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this PostUsersRequest.


        :param firstname: The firstname of this PostUsersRequest.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def is_self_service_user(self):
        """Gets the is_self_service_user of this PostUsersRequest.  # noqa: E501


        :return: The is_self_service_user of this PostUsersRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_self_service_user

    @is_self_service_user.setter
    def is_self_service_user(self, is_self_service_user):
        """Sets the is_self_service_user of this PostUsersRequest.


        :param is_self_service_user: The is_self_service_user of this PostUsersRequest.  # noqa: E501
        :type: bool
        """

        self._is_self_service_user = is_self_service_user

    @property
    def lastname(self):
        """Gets the lastname of this PostUsersRequest.  # noqa: E501


        :return: The lastname of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PostUsersRequest.


        :param lastname: The lastname of this PostUsersRequest.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def office_id(self):
        """Gets the office_id of this PostUsersRequest.  # noqa: E501


        :return: The office_id of this PostUsersRequest.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this PostUsersRequest.


        :param office_id: The office_id of this PostUsersRequest.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def password(self):
        """Gets the password of this PostUsersRequest.  # noqa: E501


        :return: The password of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostUsersRequest.


        :param password: The password of this PostUsersRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this PostUsersRequest.  # noqa: E501


        :return: The password_never_expires of this PostUsersRequest.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this PostUsersRequest.


        :param password_never_expires: The password_never_expires of this PostUsersRequest.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

    @property
    def repeat_password(self):
        """Gets the repeat_password of this PostUsersRequest.  # noqa: E501


        :return: The repeat_password of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._repeat_password

    @repeat_password.setter
    def repeat_password(self, repeat_password):
        """Sets the repeat_password of this PostUsersRequest.


        :param repeat_password: The repeat_password of this PostUsersRequest.  # noqa: E501
        :type: str
        """

        self._repeat_password = repeat_password

    @property
    def roles(self):
        """Gets the roles of this PostUsersRequest.  # noqa: E501


        :return: The roles of this PostUsersRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this PostUsersRequest.


        :param roles: The roles of this PostUsersRequest.  # noqa: E501
        :type: list[int]
        """

        self._roles = roles

    @property
    def send_password_to_email(self):
        """Gets the send_password_to_email of this PostUsersRequest.  # noqa: E501


        :return: The send_password_to_email of this PostUsersRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_password_to_email

    @send_password_to_email.setter
    def send_password_to_email(self, send_password_to_email):
        """Sets the send_password_to_email of this PostUsersRequest.


        :param send_password_to_email: The send_password_to_email of this PostUsersRequest.  # noqa: E501
        :type: bool
        """

        self._send_password_to_email = send_password_to_email

    @property
    def staff_id(self):
        """Gets the staff_id of this PostUsersRequest.  # noqa: E501


        :return: The staff_id of this PostUsersRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this PostUsersRequest.


        :param staff_id: The staff_id of this PostUsersRequest.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def username(self):
        """Gets the username of this PostUsersRequest.  # noqa: E501


        :return: The username of this PostUsersRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PostUsersRequest.


        :param username: The username of this PostUsersRequest.  # noqa: E501
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
        if issubclass(PostUsersRequest, dict):
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
        if not isinstance(other, PostUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
