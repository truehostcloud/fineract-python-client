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

class PutReportResponseChanges(object):
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
        'report_name': 'str',
        'report_parameters': 'list[ReportParameterData]'
    }

    attribute_map = {
        'report_name': 'reportName',
        'report_parameters': 'reportParameters'
    }

    def __init__(self, report_name=None, report_parameters=None):  # noqa: E501
        """PutReportResponseChanges - a model defined in Swagger"""  # noqa: E501
        self._report_name = None
        self._report_parameters = None
        self.discriminator = None
        if report_name is not None:
            self.report_name = report_name
        if report_parameters is not None:
            self.report_parameters = report_parameters

    @property
    def report_name(self):
        """Gets the report_name of this PutReportResponseChanges.  # noqa: E501


        :return: The report_name of this PutReportResponseChanges.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this PutReportResponseChanges.


        :param report_name: The report_name of this PutReportResponseChanges.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_parameters(self):
        """Gets the report_parameters of this PutReportResponseChanges.  # noqa: E501


        :return: The report_parameters of this PutReportResponseChanges.  # noqa: E501
        :rtype: list[ReportParameterData]
        """
        return self._report_parameters

    @report_parameters.setter
    def report_parameters(self, report_parameters):
        """Sets the report_parameters of this PutReportResponseChanges.


        :param report_parameters: The report_parameters of this PutReportResponseChanges.  # noqa: E501
        :type: list[ReportParameterData]
        """

        self._report_parameters = report_parameters

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
        if issubclass(PutReportResponseChanges, dict):
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
        if not isinstance(other, PutReportResponseChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
