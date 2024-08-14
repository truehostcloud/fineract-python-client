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

class GetAccountsTimeline(object):
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
        'activated_date': 'date',
        'approved_by_firstname': 'str',
        'approved_by_lastname': 'str',
        'approved_by_username': 'str',
        'approved_date': 'date',
        'submitted_by_firstname': 'str',
        'submitted_by_lastname': 'str',
        'submitted_by_username': 'str',
        'submitted_on_date': 'date'
    }

    attribute_map = {
        'activated_date': 'activatedDate',
        'approved_by_firstname': 'approvedByFirstname',
        'approved_by_lastname': 'approvedByLastname',
        'approved_by_username': 'approvedByUsername',
        'approved_date': 'approvedDate',
        'submitted_by_firstname': 'submittedByFirstname',
        'submitted_by_lastname': 'submittedByLastname',
        'submitted_by_username': 'submittedByUsername',
        'submitted_on_date': 'submittedOnDate'
    }

    def __init__(self, activated_date=None, approved_by_firstname=None, approved_by_lastname=None, approved_by_username=None, approved_date=None, submitted_by_firstname=None, submitted_by_lastname=None, submitted_by_username=None, submitted_on_date=None):  # noqa: E501
        """GetAccountsTimeline - a model defined in Swagger"""  # noqa: E501
        self._activated_date = None
        self._approved_by_firstname = None
        self._approved_by_lastname = None
        self._approved_by_username = None
        self._approved_date = None
        self._submitted_by_firstname = None
        self._submitted_by_lastname = None
        self._submitted_by_username = None
        self._submitted_on_date = None
        self.discriminator = None
        if activated_date is not None:
            self.activated_date = activated_date
        if approved_by_firstname is not None:
            self.approved_by_firstname = approved_by_firstname
        if approved_by_lastname is not None:
            self.approved_by_lastname = approved_by_lastname
        if approved_by_username is not None:
            self.approved_by_username = approved_by_username
        if approved_date is not None:
            self.approved_date = approved_date
        if submitted_by_firstname is not None:
            self.submitted_by_firstname = submitted_by_firstname
        if submitted_by_lastname is not None:
            self.submitted_by_lastname = submitted_by_lastname
        if submitted_by_username is not None:
            self.submitted_by_username = submitted_by_username
        if submitted_on_date is not None:
            self.submitted_on_date = submitted_on_date

    @property
    def activated_date(self):
        """Gets the activated_date of this GetAccountsTimeline.  # noqa: E501


        :return: The activated_date of this GetAccountsTimeline.  # noqa: E501
        :rtype: date
        """
        return self._activated_date

    @activated_date.setter
    def activated_date(self, activated_date):
        """Sets the activated_date of this GetAccountsTimeline.


        :param activated_date: The activated_date of this GetAccountsTimeline.  # noqa: E501
        :type: date
        """

        self._activated_date = activated_date

    @property
    def approved_by_firstname(self):
        """Gets the approved_by_firstname of this GetAccountsTimeline.  # noqa: E501


        :return: The approved_by_firstname of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._approved_by_firstname

    @approved_by_firstname.setter
    def approved_by_firstname(self, approved_by_firstname):
        """Sets the approved_by_firstname of this GetAccountsTimeline.


        :param approved_by_firstname: The approved_by_firstname of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._approved_by_firstname = approved_by_firstname

    @property
    def approved_by_lastname(self):
        """Gets the approved_by_lastname of this GetAccountsTimeline.  # noqa: E501


        :return: The approved_by_lastname of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._approved_by_lastname

    @approved_by_lastname.setter
    def approved_by_lastname(self, approved_by_lastname):
        """Sets the approved_by_lastname of this GetAccountsTimeline.


        :param approved_by_lastname: The approved_by_lastname of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._approved_by_lastname = approved_by_lastname

    @property
    def approved_by_username(self):
        """Gets the approved_by_username of this GetAccountsTimeline.  # noqa: E501


        :return: The approved_by_username of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._approved_by_username

    @approved_by_username.setter
    def approved_by_username(self, approved_by_username):
        """Sets the approved_by_username of this GetAccountsTimeline.


        :param approved_by_username: The approved_by_username of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._approved_by_username = approved_by_username

    @property
    def approved_date(self):
        """Gets the approved_date of this GetAccountsTimeline.  # noqa: E501


        :return: The approved_date of this GetAccountsTimeline.  # noqa: E501
        :rtype: date
        """
        return self._approved_date

    @approved_date.setter
    def approved_date(self, approved_date):
        """Sets the approved_date of this GetAccountsTimeline.


        :param approved_date: The approved_date of this GetAccountsTimeline.  # noqa: E501
        :type: date
        """

        self._approved_date = approved_date

    @property
    def submitted_by_firstname(self):
        """Gets the submitted_by_firstname of this GetAccountsTimeline.  # noqa: E501


        :return: The submitted_by_firstname of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_firstname

    @submitted_by_firstname.setter
    def submitted_by_firstname(self, submitted_by_firstname):
        """Sets the submitted_by_firstname of this GetAccountsTimeline.


        :param submitted_by_firstname: The submitted_by_firstname of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._submitted_by_firstname = submitted_by_firstname

    @property
    def submitted_by_lastname(self):
        """Gets the submitted_by_lastname of this GetAccountsTimeline.  # noqa: E501


        :return: The submitted_by_lastname of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_lastname

    @submitted_by_lastname.setter
    def submitted_by_lastname(self, submitted_by_lastname):
        """Sets the submitted_by_lastname of this GetAccountsTimeline.


        :param submitted_by_lastname: The submitted_by_lastname of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._submitted_by_lastname = submitted_by_lastname

    @property
    def submitted_by_username(self):
        """Gets the submitted_by_username of this GetAccountsTimeline.  # noqa: E501


        :return: The submitted_by_username of this GetAccountsTimeline.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_username

    @submitted_by_username.setter
    def submitted_by_username(self, submitted_by_username):
        """Sets the submitted_by_username of this GetAccountsTimeline.


        :param submitted_by_username: The submitted_by_username of this GetAccountsTimeline.  # noqa: E501
        :type: str
        """

        self._submitted_by_username = submitted_by_username

    @property
    def submitted_on_date(self):
        """Gets the submitted_on_date of this GetAccountsTimeline.  # noqa: E501


        :return: The submitted_on_date of this GetAccountsTimeline.  # noqa: E501
        :rtype: date
        """
        return self._submitted_on_date

    @submitted_on_date.setter
    def submitted_on_date(self, submitted_on_date):
        """Sets the submitted_on_date of this GetAccountsTimeline.


        :param submitted_on_date: The submitted_on_date of this GetAccountsTimeline.  # noqa: E501
        :type: date
        """

        self._submitted_on_date = submitted_on_date

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
        if issubclass(GetAccountsTimeline, dict):
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
        if not isinstance(other, GetAccountsTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
