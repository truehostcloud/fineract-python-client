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

class GetGlClosureResponse(object):
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
        'closing_date': 'date',
        'comments': 'str',
        'created_by_user_id': 'int',
        'created_by_username': 'str',
        'created_date': 'date',
        'deleted': 'bool',
        'id': 'int',
        'last_updated_by_user_id': 'int',
        'last_updated_by_username': 'str',
        'last_updated_date': 'date',
        'office_id': 'int',
        'office_name': 'str'
    }

    attribute_map = {
        'closing_date': 'closingDate',
        'comments': 'comments',
        'created_by_user_id': 'createdByUserId',
        'created_by_username': 'createdByUsername',
        'created_date': 'createdDate',
        'deleted': 'deleted',
        'id': 'id',
        'last_updated_by_user_id': 'lastUpdatedByUserId',
        'last_updated_by_username': 'lastUpdatedByUsername',
        'last_updated_date': 'lastUpdatedDate',
        'office_id': 'officeId',
        'office_name': 'officeName'
    }

    def __init__(self, closing_date=None, comments=None, created_by_user_id=None, created_by_username=None, created_date=None, deleted=None, id=None, last_updated_by_user_id=None, last_updated_by_username=None, last_updated_date=None, office_id=None, office_name=None):  # noqa: E501
        """GetGlClosureResponse - a model defined in Swagger"""  # noqa: E501
        self._closing_date = None
        self._comments = None
        self._created_by_user_id = None
        self._created_by_username = None
        self._created_date = None
        self._deleted = None
        self._id = None
        self._last_updated_by_user_id = None
        self._last_updated_by_username = None
        self._last_updated_date = None
        self._office_id = None
        self._office_name = None
        self.discriminator = None
        if closing_date is not None:
            self.closing_date = closing_date
        if comments is not None:
            self.comments = comments
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if created_by_username is not None:
            self.created_by_username = created_by_username
        if created_date is not None:
            self.created_date = created_date
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if last_updated_by_user_id is not None:
            self.last_updated_by_user_id = last_updated_by_user_id
        if last_updated_by_username is not None:
            self.last_updated_by_username = last_updated_by_username
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name

    @property
    def closing_date(self):
        """Gets the closing_date of this GetGlClosureResponse.  # noqa: E501


        :return: The closing_date of this GetGlClosureResponse.  # noqa: E501
        :rtype: date
        """
        return self._closing_date

    @closing_date.setter
    def closing_date(self, closing_date):
        """Sets the closing_date of this GetGlClosureResponse.


        :param closing_date: The closing_date of this GetGlClosureResponse.  # noqa: E501
        :type: date
        """

        self._closing_date = closing_date

    @property
    def comments(self):
        """Gets the comments of this GetGlClosureResponse.  # noqa: E501


        :return: The comments of this GetGlClosureResponse.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this GetGlClosureResponse.


        :param comments: The comments of this GetGlClosureResponse.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this GetGlClosureResponse.  # noqa: E501


        :return: The created_by_user_id of this GetGlClosureResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this GetGlClosureResponse.


        :param created_by_user_id: The created_by_user_id of this GetGlClosureResponse.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def created_by_username(self):
        """Gets the created_by_username of this GetGlClosureResponse.  # noqa: E501


        :return: The created_by_username of this GetGlClosureResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_username

    @created_by_username.setter
    def created_by_username(self, created_by_username):
        """Sets the created_by_username of this GetGlClosureResponse.


        :param created_by_username: The created_by_username of this GetGlClosureResponse.  # noqa: E501
        :type: str
        """

        self._created_by_username = created_by_username

    @property
    def created_date(self):
        """Gets the created_date of this GetGlClosureResponse.  # noqa: E501


        :return: The created_date of this GetGlClosureResponse.  # noqa: E501
        :rtype: date
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GetGlClosureResponse.


        :param created_date: The created_date of this GetGlClosureResponse.  # noqa: E501
        :type: date
        """

        self._created_date = created_date

    @property
    def deleted(self):
        """Gets the deleted of this GetGlClosureResponse.  # noqa: E501


        :return: The deleted of this GetGlClosureResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this GetGlClosureResponse.


        :param deleted: The deleted of this GetGlClosureResponse.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this GetGlClosureResponse.  # noqa: E501


        :return: The id of this GetGlClosureResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetGlClosureResponse.


        :param id: The id of this GetGlClosureResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_updated_by_user_id(self):
        """Gets the last_updated_by_user_id of this GetGlClosureResponse.  # noqa: E501


        :return: The last_updated_by_user_id of this GetGlClosureResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_by_user_id

    @last_updated_by_user_id.setter
    def last_updated_by_user_id(self, last_updated_by_user_id):
        """Sets the last_updated_by_user_id of this GetGlClosureResponse.


        :param last_updated_by_user_id: The last_updated_by_user_id of this GetGlClosureResponse.  # noqa: E501
        :type: int
        """

        self._last_updated_by_user_id = last_updated_by_user_id

    @property
    def last_updated_by_username(self):
        """Gets the last_updated_by_username of this GetGlClosureResponse.  # noqa: E501


        :return: The last_updated_by_username of this GetGlClosureResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by_username

    @last_updated_by_username.setter
    def last_updated_by_username(self, last_updated_by_username):
        """Sets the last_updated_by_username of this GetGlClosureResponse.


        :param last_updated_by_username: The last_updated_by_username of this GetGlClosureResponse.  # noqa: E501
        :type: str
        """

        self._last_updated_by_username = last_updated_by_username

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this GetGlClosureResponse.  # noqa: E501


        :return: The last_updated_date of this GetGlClosureResponse.  # noqa: E501
        :rtype: date
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this GetGlClosureResponse.


        :param last_updated_date: The last_updated_date of this GetGlClosureResponse.  # noqa: E501
        :type: date
        """

        self._last_updated_date = last_updated_date

    @property
    def office_id(self):
        """Gets the office_id of this GetGlClosureResponse.  # noqa: E501


        :return: The office_id of this GetGlClosureResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetGlClosureResponse.


        :param office_id: The office_id of this GetGlClosureResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetGlClosureResponse.  # noqa: E501


        :return: The office_name of this GetGlClosureResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetGlClosureResponse.


        :param office_name: The office_name of this GetGlClosureResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

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
        if issubclass(GetGlClosureResponse, dict):
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
        if not isinstance(other, GetGlClosureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
