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

class GetSelfUserDetailsResponse(object):
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
        'authenticated': 'bool',
        'base64_encoded_authentication_key': 'str',
        'clients': 'list[int]',
        'is_self_service_user': 'bool',
        'office_id': 'int',
        'office_name': 'str',
        'organisational_role': 'GetSelfUserDetailsOrganisationalRole',
        'permissions': 'list[str]',
        'roles': 'list[GetSelfUserDetailsRoles]',
        'staff_display_name': 'str',
        'staff_id': 'int',
        'user_id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'authenticated': 'authenticated',
        'base64_encoded_authentication_key': 'base64EncodedAuthenticationKey',
        'clients': 'clients',
        'is_self_service_user': 'isSelfServiceUser',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'organisational_role': 'organisationalRole',
        'permissions': 'permissions',
        'roles': 'roles',
        'staff_display_name': 'staffDisplayName',
        'staff_id': 'staffId',
        'user_id': 'userId',
        'username': 'username'
    }

    def __init__(self, authenticated=None, base64_encoded_authentication_key=None, clients=None, is_self_service_user=None, office_id=None, office_name=None, organisational_role=None, permissions=None, roles=None, staff_display_name=None, staff_id=None, user_id=None, username=None):  # noqa: E501
        """GetSelfUserDetailsResponse - a model defined in Swagger"""  # noqa: E501
        self._authenticated = None
        self._base64_encoded_authentication_key = None
        self._clients = None
        self._is_self_service_user = None
        self._office_id = None
        self._office_name = None
        self._organisational_role = None
        self._permissions = None
        self._roles = None
        self._staff_display_name = None
        self._staff_id = None
        self._user_id = None
        self._username = None
        self.discriminator = None
        if authenticated is not None:
            self.authenticated = authenticated
        if base64_encoded_authentication_key is not None:
            self.base64_encoded_authentication_key = base64_encoded_authentication_key
        if clients is not None:
            self.clients = clients
        if is_self_service_user is not None:
            self.is_self_service_user = is_self_service_user
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if organisational_role is not None:
            self.organisational_role = organisational_role
        if permissions is not None:
            self.permissions = permissions
        if roles is not None:
            self.roles = roles
        if staff_display_name is not None:
            self.staff_display_name = staff_display_name
        if staff_id is not None:
            self.staff_id = staff_id
        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username

    @property
    def authenticated(self):
        """Gets the authenticated of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The authenticated of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """Sets the authenticated of this GetSelfUserDetailsResponse.


        :param authenticated: The authenticated of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._authenticated = authenticated

    @property
    def base64_encoded_authentication_key(self):
        """Gets the base64_encoded_authentication_key of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The base64_encoded_authentication_key of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._base64_encoded_authentication_key

    @base64_encoded_authentication_key.setter
    def base64_encoded_authentication_key(self, base64_encoded_authentication_key):
        """Sets the base64_encoded_authentication_key of this GetSelfUserDetailsResponse.


        :param base64_encoded_authentication_key: The base64_encoded_authentication_key of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._base64_encoded_authentication_key = base64_encoded_authentication_key

    @property
    def clients(self):
        """Gets the clients of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The clients of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this GetSelfUserDetailsResponse.


        :param clients: The clients of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: list[int]
        """

        self._clients = clients

    @property
    def is_self_service_user(self):
        """Gets the is_self_service_user of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The is_self_service_user of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_self_service_user

    @is_self_service_user.setter
    def is_self_service_user(self, is_self_service_user):
        """Sets the is_self_service_user of this GetSelfUserDetailsResponse.


        :param is_self_service_user: The is_self_service_user of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._is_self_service_user = is_self_service_user

    @property
    def office_id(self):
        """Gets the office_id of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The office_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetSelfUserDetailsResponse.


        :param office_id: The office_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The office_name of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetSelfUserDetailsResponse.


        :param office_name: The office_name of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def organisational_role(self):
        """Gets the organisational_role of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The organisational_role of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: GetSelfUserDetailsOrganisationalRole
        """
        return self._organisational_role

    @organisational_role.setter
    def organisational_role(self, organisational_role):
        """Sets the organisational_role of this GetSelfUserDetailsResponse.


        :param organisational_role: The organisational_role of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: GetSelfUserDetailsOrganisationalRole
        """

        self._organisational_role = organisational_role

    @property
    def permissions(self):
        """Gets the permissions of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The permissions of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GetSelfUserDetailsResponse.


        :param permissions: The permissions of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def roles(self):
        """Gets the roles of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The roles of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: list[GetSelfUserDetailsRoles]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this GetSelfUserDetailsResponse.


        :param roles: The roles of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: list[GetSelfUserDetailsRoles]
        """

        self._roles = roles

    @property
    def staff_display_name(self):
        """Gets the staff_display_name of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The staff_display_name of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._staff_display_name

    @staff_display_name.setter
    def staff_display_name(self, staff_display_name):
        """Sets the staff_display_name of this GetSelfUserDetailsResponse.


        :param staff_display_name: The staff_display_name of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._staff_display_name = staff_display_name

    @property
    def staff_id(self):
        """Gets the staff_id of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The staff_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GetSelfUserDetailsResponse.


        :param staff_id: The staff_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def user_id(self):
        """Gets the user_id of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The user_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GetSelfUserDetailsResponse.


        :param user_id: The user_id of this GetSelfUserDetailsResponse.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this GetSelfUserDetailsResponse.  # noqa: E501


        :return: The username of this GetSelfUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetSelfUserDetailsResponse.


        :param username: The username of this GetSelfUserDetailsResponse.  # noqa: E501
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
        if issubclass(GetSelfUserDetailsResponse, dict):
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
        if not isinstance(other, GetSelfUserDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
