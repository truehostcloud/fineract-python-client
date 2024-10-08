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

class GetDelinquencyActionsResponse(object):
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
        'action': 'str',
        'created_by_id': 'int',
        'created_on': 'datetime',
        'end_date': 'date',
        'id': 'int',
        'last_modified_on': 'datetime',
        'start_date': 'date',
        'updated_by_id': 'int'
    }

    attribute_map = {
        'action': 'action',
        'created_by_id': 'createdById',
        'created_on': 'createdOn',
        'end_date': 'endDate',
        'id': 'id',
        'last_modified_on': 'lastModifiedOn',
        'start_date': 'startDate',
        'updated_by_id': 'updatedById'
    }

    def __init__(self, action=None, created_by_id=None, created_on=None, end_date=None, id=None, last_modified_on=None, start_date=None, updated_by_id=None):  # noqa: E501
        """GetDelinquencyActionsResponse - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._created_by_id = None
        self._created_on = None
        self._end_date = None
        self._id = None
        self._last_modified_on = None
        self._start_date = None
        self._updated_by_id = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_on is not None:
            self.created_on = created_on
        if end_date is not None:
            self.end_date = end_date
        if id is not None:
            self.id = id
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if start_date is not None:
            self.start_date = start_date
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id

    @property
    def action(self):
        """Gets the action of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The action of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GetDelinquencyActionsResponse.


        :param action: The action of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The created_by_id of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetDelinquencyActionsResponse.


        :param created_by_id: The created_by_id of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_on(self):
        """Gets the created_on of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The created_on of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GetDelinquencyActionsResponse.


        :param created_on: The created_on of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def end_date(self):
        """Gets the end_date of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The end_date of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetDelinquencyActionsResponse.


        :param end_date: The end_date of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def id(self):
        """Gets the id of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The id of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetDelinquencyActionsResponse.


        :param id: The id of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The last_modified_on of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this GetDelinquencyActionsResponse.


        :param last_modified_on: The last_modified_on of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def start_date(self):
        """Gets the start_date of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The start_date of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetDelinquencyActionsResponse.


        :param start_date: The start_date of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GetDelinquencyActionsResponse.  # noqa: E501


        :return: The updated_by_id of this GetDelinquencyActionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GetDelinquencyActionsResponse.


        :param updated_by_id: The updated_by_id of this GetDelinquencyActionsResponse.  # noqa: E501
        :type: int
        """

        self._updated_by_id = updated_by_id

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
        if issubclass(GetDelinquencyActionsResponse, dict):
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
        if not isinstance(other, GetDelinquencyActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
