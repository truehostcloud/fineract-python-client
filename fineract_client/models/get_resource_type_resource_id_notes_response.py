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

class GetResourceTypeResourceIdNotesResponse(object):
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
        'client_id': 'int',
        'created_by_id': 'int',
        'created_by_username': 'str',
        'created_on': 'datetime',
        'id': 'int',
        'note': 'str',
        'note_type': 'GetNotesNoteType',
        'updated_by_id': 'int',
        'updated_by_username': 'str',
        'updated_on': 'datetime'
    }

    attribute_map = {
        'client_id': 'clientId',
        'created_by_id': 'createdById',
        'created_by_username': 'createdByUsername',
        'created_on': 'createdOn',
        'id': 'id',
        'note': 'note',
        'note_type': 'noteType',
        'updated_by_id': 'updatedById',
        'updated_by_username': 'updatedByUsername',
        'updated_on': 'updatedOn'
    }

    def __init__(self, client_id=None, created_by_id=None, created_by_username=None, created_on=None, id=None, note=None, note_type=None, updated_by_id=None, updated_by_username=None, updated_on=None):  # noqa: E501
        """GetResourceTypeResourceIdNotesResponse - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._created_by_id = None
        self._created_by_username = None
        self._created_on = None
        self._id = None
        self._note = None
        self._note_type = None
        self._updated_by_id = None
        self._updated_by_username = None
        self._updated_on = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by_username is not None:
            self.created_by_username = created_by_username
        if created_on is not None:
            self.created_on = created_on
        if id is not None:
            self.id = id
        if note is not None:
            self.note = note
        if note_type is not None:
            self.note_type = note_type
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_by_username is not None:
            self.updated_by_username = updated_by_username
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def client_id(self):
        """Gets the client_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The client_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetResourceTypeResourceIdNotesResponse.


        :param client_id: The client_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The created_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetResourceTypeResourceIdNotesResponse.


        :param created_by_id: The created_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_by_username(self):
        """Gets the created_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The created_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_username

    @created_by_username.setter
    def created_by_username(self, created_by_username):
        """Sets the created_by_username of this GetResourceTypeResourceIdNotesResponse.


        :param created_by_username: The created_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: str
        """

        self._created_by_username = created_by_username

    @property
    def created_on(self):
        """Gets the created_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The created_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GetResourceTypeResourceIdNotesResponse.


        :param created_on: The created_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def id(self):
        """Gets the id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetResourceTypeResourceIdNotesResponse.


        :param id: The id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def note(self):
        """Gets the note of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The note of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this GetResourceTypeResourceIdNotesResponse.


        :param note: The note of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def note_type(self):
        """Gets the note_type of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The note_type of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: GetNotesNoteType
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        """Sets the note_type of this GetResourceTypeResourceIdNotesResponse.


        :param note_type: The note_type of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: GetNotesNoteType
        """

        self._note_type = note_type

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The updated_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GetResourceTypeResourceIdNotesResponse.


        :param updated_by_id: The updated_by_id of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: int
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_by_username(self):
        """Gets the updated_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The updated_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_username

    @updated_by_username.setter
    def updated_by_username(self, updated_by_username):
        """Sets the updated_by_username of this GetResourceTypeResourceIdNotesResponse.


        :param updated_by_username: The updated_by_username of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: str
        """

        self._updated_by_username = updated_by_username

    @property
    def updated_on(self):
        """Gets the updated_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501


        :return: The updated_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this GetResourceTypeResourceIdNotesResponse.


        :param updated_on: The updated_on of this GetResourceTypeResourceIdNotesResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

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
        if issubclass(GetResourceTypeResourceIdNotesResponse, dict):
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
        if not isinstance(other, GetResourceTypeResourceIdNotesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
