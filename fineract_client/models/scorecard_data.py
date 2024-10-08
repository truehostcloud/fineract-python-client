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

class ScorecardData(object):
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
        'id': 'int',
        'scorecard_values': 'list[ScorecardValue]',
        'survey_id': 'int',
        'survey_name': 'str',
        'user_id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'id': 'id',
        'scorecard_values': 'scorecardValues',
        'survey_id': 'surveyId',
        'survey_name': 'surveyName',
        'user_id': 'userId',
        'username': 'username'
    }

    def __init__(self, client_id=None, id=None, scorecard_values=None, survey_id=None, survey_name=None, user_id=None, username=None):  # noqa: E501
        """ScorecardData - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._id = None
        self._scorecard_values = None
        self._survey_id = None
        self._survey_name = None
        self._user_id = None
        self._username = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if id is not None:
            self.id = id
        if scorecard_values is not None:
            self.scorecard_values = scorecard_values
        if survey_id is not None:
            self.survey_id = survey_id
        if survey_name is not None:
            self.survey_name = survey_name
        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username

    @property
    def client_id(self):
        """Gets the client_id of this ScorecardData.  # noqa: E501


        :return: The client_id of this ScorecardData.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ScorecardData.


        :param client_id: The client_id of this ScorecardData.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def id(self):
        """Gets the id of this ScorecardData.  # noqa: E501


        :return: The id of this ScorecardData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScorecardData.


        :param id: The id of this ScorecardData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def scorecard_values(self):
        """Gets the scorecard_values of this ScorecardData.  # noqa: E501


        :return: The scorecard_values of this ScorecardData.  # noqa: E501
        :rtype: list[ScorecardValue]
        """
        return self._scorecard_values

    @scorecard_values.setter
    def scorecard_values(self, scorecard_values):
        """Sets the scorecard_values of this ScorecardData.


        :param scorecard_values: The scorecard_values of this ScorecardData.  # noqa: E501
        :type: list[ScorecardValue]
        """

        self._scorecard_values = scorecard_values

    @property
    def survey_id(self):
        """Gets the survey_id of this ScorecardData.  # noqa: E501


        :return: The survey_id of this ScorecardData.  # noqa: E501
        :rtype: int
        """
        return self._survey_id

    @survey_id.setter
    def survey_id(self, survey_id):
        """Sets the survey_id of this ScorecardData.


        :param survey_id: The survey_id of this ScorecardData.  # noqa: E501
        :type: int
        """

        self._survey_id = survey_id

    @property
    def survey_name(self):
        """Gets the survey_name of this ScorecardData.  # noqa: E501


        :return: The survey_name of this ScorecardData.  # noqa: E501
        :rtype: str
        """
        return self._survey_name

    @survey_name.setter
    def survey_name(self, survey_name):
        """Sets the survey_name of this ScorecardData.


        :param survey_name: The survey_name of this ScorecardData.  # noqa: E501
        :type: str
        """

        self._survey_name = survey_name

    @property
    def user_id(self):
        """Gets the user_id of this ScorecardData.  # noqa: E501


        :return: The user_id of this ScorecardData.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ScorecardData.


        :param user_id: The user_id of this ScorecardData.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this ScorecardData.  # noqa: E501


        :return: The username of this ScorecardData.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ScorecardData.


        :param username: The username of this ScorecardData.  # noqa: E501
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
        if issubclass(ScorecardData, dict):
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
        if not isinstance(other, ScorecardData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
