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

class PutWorkingDaysRequest(object):
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
        'extend_term_for_daily_repayments': 'bool',
        'locale': 'str',
        'recurrence': 'str',
        'repayment_reschedule_type': 'EnumOptionData'
    }

    attribute_map = {
        'extend_term_for_daily_repayments': 'extendTermForDailyRepayments',
        'locale': 'locale',
        'recurrence': 'recurrence',
        'repayment_reschedule_type': 'repaymentRescheduleType'
    }

    def __init__(self, extend_term_for_daily_repayments=None, locale=None, recurrence=None, repayment_reschedule_type=None):  # noqa: E501
        """PutWorkingDaysRequest - a model defined in Swagger"""  # noqa: E501
        self._extend_term_for_daily_repayments = None
        self._locale = None
        self._recurrence = None
        self._repayment_reschedule_type = None
        self.discriminator = None
        if extend_term_for_daily_repayments is not None:
            self.extend_term_for_daily_repayments = extend_term_for_daily_repayments
        if locale is not None:
            self.locale = locale
        if recurrence is not None:
            self.recurrence = recurrence
        if repayment_reschedule_type is not None:
            self.repayment_reschedule_type = repayment_reschedule_type

    @property
    def extend_term_for_daily_repayments(self):
        """Gets the extend_term_for_daily_repayments of this PutWorkingDaysRequest.  # noqa: E501


        :return: The extend_term_for_daily_repayments of this PutWorkingDaysRequest.  # noqa: E501
        :rtype: bool
        """
        return self._extend_term_for_daily_repayments

    @extend_term_for_daily_repayments.setter
    def extend_term_for_daily_repayments(self, extend_term_for_daily_repayments):
        """Sets the extend_term_for_daily_repayments of this PutWorkingDaysRequest.


        :param extend_term_for_daily_repayments: The extend_term_for_daily_repayments of this PutWorkingDaysRequest.  # noqa: E501
        :type: bool
        """

        self._extend_term_for_daily_repayments = extend_term_for_daily_repayments

    @property
    def locale(self):
        """Gets the locale of this PutWorkingDaysRequest.  # noqa: E501


        :return: The locale of this PutWorkingDaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PutWorkingDaysRequest.


        :param locale: The locale of this PutWorkingDaysRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def recurrence(self):
        """Gets the recurrence of this PutWorkingDaysRequest.  # noqa: E501


        :return: The recurrence of this PutWorkingDaysRequest.  # noqa: E501
        :rtype: str
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this PutWorkingDaysRequest.


        :param recurrence: The recurrence of this PutWorkingDaysRequest.  # noqa: E501
        :type: str
        """

        self._recurrence = recurrence

    @property
    def repayment_reschedule_type(self):
        """Gets the repayment_reschedule_type of this PutWorkingDaysRequest.  # noqa: E501


        :return: The repayment_reschedule_type of this PutWorkingDaysRequest.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._repayment_reschedule_type

    @repayment_reschedule_type.setter
    def repayment_reschedule_type(self, repayment_reschedule_type):
        """Sets the repayment_reschedule_type of this PutWorkingDaysRequest.


        :param repayment_reschedule_type: The repayment_reschedule_type of this PutWorkingDaysRequest.  # noqa: E501
        :type: EnumOptionData
        """

        self._repayment_reschedule_type = repayment_reschedule_type

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
        if issubclass(PutWorkingDaysRequest, dict):
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
        if not isinstance(other, PutWorkingDaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
