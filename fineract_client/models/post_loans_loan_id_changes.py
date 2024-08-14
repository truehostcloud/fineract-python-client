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

class PostLoansLoanIdChanges(object):
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
        'approved_on_date': 'str',
        'date_format': 'str',
        'locale': 'str',
        'note': 'str',
        'status': 'PostLoansLoanIdStatus'
    }

    attribute_map = {
        'approved_on_date': 'approvedOnDate',
        'date_format': 'dateFormat',
        'locale': 'locale',
        'note': 'note',
        'status': 'status'
    }

    def __init__(self, approved_on_date=None, date_format=None, locale=None, note=None, status=None):  # noqa: E501
        """PostLoansLoanIdChanges - a model defined in Swagger"""  # noqa: E501
        self._approved_on_date = None
        self._date_format = None
        self._locale = None
        self._note = None
        self._status = None
        self.discriminator = None
        if approved_on_date is not None:
            self.approved_on_date = approved_on_date
        if date_format is not None:
            self.date_format = date_format
        if locale is not None:
            self.locale = locale
        if note is not None:
            self.note = note
        if status is not None:
            self.status = status

    @property
    def approved_on_date(self):
        """Gets the approved_on_date of this PostLoansLoanIdChanges.  # noqa: E501


        :return: The approved_on_date of this PostLoansLoanIdChanges.  # noqa: E501
        :rtype: str
        """
        return self._approved_on_date

    @approved_on_date.setter
    def approved_on_date(self, approved_on_date):
        """Sets the approved_on_date of this PostLoansLoanIdChanges.


        :param approved_on_date: The approved_on_date of this PostLoansLoanIdChanges.  # noqa: E501
        :type: str
        """

        self._approved_on_date = approved_on_date

    @property
    def date_format(self):
        """Gets the date_format of this PostLoansLoanIdChanges.  # noqa: E501


        :return: The date_format of this PostLoansLoanIdChanges.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostLoansLoanIdChanges.


        :param date_format: The date_format of this PostLoansLoanIdChanges.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def locale(self):
        """Gets the locale of this PostLoansLoanIdChanges.  # noqa: E501


        :return: The locale of this PostLoansLoanIdChanges.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostLoansLoanIdChanges.


        :param locale: The locale of this PostLoansLoanIdChanges.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def note(self):
        """Gets the note of this PostLoansLoanIdChanges.  # noqa: E501


        :return: The note of this PostLoansLoanIdChanges.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PostLoansLoanIdChanges.


        :param note: The note of this PostLoansLoanIdChanges.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def status(self):
        """Gets the status of this PostLoansLoanIdChanges.  # noqa: E501


        :return: The status of this PostLoansLoanIdChanges.  # noqa: E501
        :rtype: PostLoansLoanIdStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostLoansLoanIdChanges.


        :param status: The status of this PostLoansLoanIdChanges.  # noqa: E501
        :type: PostLoansLoanIdStatus
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
        if issubclass(PostLoansLoanIdChanges, dict):
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
        if not isinstance(other, PostLoansLoanIdChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
