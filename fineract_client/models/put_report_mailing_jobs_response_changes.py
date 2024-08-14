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

class PutReportMailingJobsResponseChanges(object):
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
        'start_date_time': 'datetime'
    }

    attribute_map = {
        'start_date_time': 'startDateTime'
    }

    def __init__(self, start_date_time=None):  # noqa: E501
        """PutReportMailingJobsResponseChanges - a model defined in Swagger"""  # noqa: E501
        self._start_date_time = None
        self.discriminator = None
        if start_date_time is not None:
            self.start_date_time = start_date_time

    @property
    def start_date_time(self):
        """Gets the start_date_time of this PutReportMailingJobsResponseChanges.  # noqa: E501


        :return: The start_date_time of this PutReportMailingJobsResponseChanges.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this PutReportMailingJobsResponseChanges.


        :param start_date_time: The start_date_time of this PutReportMailingJobsResponseChanges.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

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
        if issubclass(PutReportMailingJobsResponseChanges, dict):
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
        if not isinstance(other, PutReportMailingJobsResponseChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
