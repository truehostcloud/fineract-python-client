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

class PostTellersRequest(object):
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
        'date_format': 'str',
        'description': 'str',
        'locale': 'str',
        'name': 'str',
        'office_id': 'int',
        'start_date': 'date',
        'status': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'description': 'description',
        'locale': 'locale',
        'name': 'name',
        'office_id': 'officeId',
        'start_date': 'startDate',
        'status': 'status'
    }

    def __init__(self, date_format=None, description=None, locale=None, name=None, office_id=None, start_date=None, status=None):  # noqa: E501
        """PostTellersRequest - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._description = None
        self._locale = None
        self._name = None
        self._office_id = None
        self._start_date = None
        self._status = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if description is not None:
            self.description = description
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if office_id is not None:
            self.office_id = office_id
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status

    @property
    def date_format(self):
        """Gets the date_format of this PostTellersRequest.  # noqa: E501


        :return: The date_format of this PostTellersRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostTellersRequest.


        :param date_format: The date_format of this PostTellersRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def description(self):
        """Gets the description of this PostTellersRequest.  # noqa: E501


        :return: The description of this PostTellersRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostTellersRequest.


        :param description: The description of this PostTellersRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def locale(self):
        """Gets the locale of this PostTellersRequest.  # noqa: E501


        :return: The locale of this PostTellersRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostTellersRequest.


        :param locale: The locale of this PostTellersRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this PostTellersRequest.  # noqa: E501


        :return: The name of this PostTellersRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostTellersRequest.


        :param name: The name of this PostTellersRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def office_id(self):
        """Gets the office_id of this PostTellersRequest.  # noqa: E501


        :return: The office_id of this PostTellersRequest.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this PostTellersRequest.


        :param office_id: The office_id of this PostTellersRequest.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def start_date(self):
        """Gets the start_date of this PostTellersRequest.  # noqa: E501


        :return: The start_date of this PostTellersRequest.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PostTellersRequest.


        :param start_date: The start_date of this PostTellersRequest.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this PostTellersRequest.  # noqa: E501


        :return: The status of this PostTellersRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostTellersRequest.


        :param status: The status of this PostTellersRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVALID", "PENDING", "ACTIVE", "INACTIVE", "CLOSED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if issubclass(PostTellersRequest, dict):
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
        if not isinstance(other, PostTellersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
