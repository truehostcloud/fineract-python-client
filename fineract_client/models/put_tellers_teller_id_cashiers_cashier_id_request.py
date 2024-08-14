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

class PutTellersTellerIdCashiersCashierIdRequest(object):
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
        'end_date': 'date',
        'is_full_day': 'bool',
        'locale': 'str',
        'staff_id': 'int',
        'start_date': 'date'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'description': 'description',
        'end_date': 'endDate',
        'is_full_day': 'isFullDay',
        'locale': 'locale',
        'staff_id': 'staffId',
        'start_date': 'startDate'
    }

    def __init__(self, date_format=None, description=None, end_date=None, is_full_day=None, locale=None, staff_id=None, start_date=None):  # noqa: E501
        """PutTellersTellerIdCashiersCashierIdRequest - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._description = None
        self._end_date = None
        self._is_full_day = None
        self._locale = None
        self._staff_id = None
        self._start_date = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if is_full_day is not None:
            self.is_full_day = is_full_day
        if locale is not None:
            self.locale = locale
        if staff_id is not None:
            self.staff_id = staff_id
        if start_date is not None:
            self.start_date = start_date

    @property
    def date_format(self):
        """Gets the date_format of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The date_format of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PutTellersTellerIdCashiersCashierIdRequest.


        :param date_format: The date_format of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def description(self):
        """Gets the description of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The description of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutTellersTellerIdCashiersCashierIdRequest.


        :param description: The description of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The end_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PutTellersTellerIdCashiersCashierIdRequest.


        :param end_date: The end_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def is_full_day(self):
        """Gets the is_full_day of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The is_full_day of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_full_day

    @is_full_day.setter
    def is_full_day(self, is_full_day):
        """Sets the is_full_day of this PutTellersTellerIdCashiersCashierIdRequest.


        :param is_full_day: The is_full_day of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: bool
        """

        self._is_full_day = is_full_day

    @property
    def locale(self):
        """Gets the locale of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The locale of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutTellersTellerIdCashiersCashierIdRequest.


        :param locale: The locale of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def staff_id(self):
        """Gets the staff_id of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The staff_id of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this PutTellersTellerIdCashiersCashierIdRequest.


        :param staff_id: The staff_id of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def start_date(self):
        """Gets the start_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501


        :return: The start_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PutTellersTellerIdCashiersCashierIdRequest.


        :param start_date: The start_date of this PutTellersTellerIdCashiersCashierIdRequest.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

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
        if issubclass(PutTellersTellerIdCashiersCashierIdRequest, dict):
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
        if not isinstance(other, PutTellersTellerIdCashiersCashierIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
