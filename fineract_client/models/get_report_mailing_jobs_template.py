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

class GetReportMailingJobsTemplate(object):
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
        'email_attachment_file_format_options': 'list[EnumOptionData]',
        'is_active': 'bool',
        'stretchy_report_param_date_options': 'list[EnumOptionData]'
    }

    attribute_map = {
        'email_attachment_file_format_options': 'emailAttachmentFileFormatOptions',
        'is_active': 'isActive',
        'stretchy_report_param_date_options': 'stretchyReportParamDateOptions'
    }

    def __init__(self, email_attachment_file_format_options=None, is_active=None, stretchy_report_param_date_options=None):  # noqa: E501
        """GetReportMailingJobsTemplate - a model defined in Swagger"""  # noqa: E501
        self._email_attachment_file_format_options = None
        self._is_active = None
        self._stretchy_report_param_date_options = None
        self.discriminator = None
        if email_attachment_file_format_options is not None:
            self.email_attachment_file_format_options = email_attachment_file_format_options
        if is_active is not None:
            self.is_active = is_active
        if stretchy_report_param_date_options is not None:
            self.stretchy_report_param_date_options = stretchy_report_param_date_options

    @property
    def email_attachment_file_format_options(self):
        """Gets the email_attachment_file_format_options of this GetReportMailingJobsTemplate.  # noqa: E501


        :return: The email_attachment_file_format_options of this GetReportMailingJobsTemplate.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._email_attachment_file_format_options

    @email_attachment_file_format_options.setter
    def email_attachment_file_format_options(self, email_attachment_file_format_options):
        """Sets the email_attachment_file_format_options of this GetReportMailingJobsTemplate.


        :param email_attachment_file_format_options: The email_attachment_file_format_options of this GetReportMailingJobsTemplate.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._email_attachment_file_format_options = email_attachment_file_format_options

    @property
    def is_active(self):
        """Gets the is_active of this GetReportMailingJobsTemplate.  # noqa: E501


        :return: The is_active of this GetReportMailingJobsTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this GetReportMailingJobsTemplate.


        :param is_active: The is_active of this GetReportMailingJobsTemplate.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def stretchy_report_param_date_options(self):
        """Gets the stretchy_report_param_date_options of this GetReportMailingJobsTemplate.  # noqa: E501


        :return: The stretchy_report_param_date_options of this GetReportMailingJobsTemplate.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._stretchy_report_param_date_options

    @stretchy_report_param_date_options.setter
    def stretchy_report_param_date_options(self, stretchy_report_param_date_options):
        """Sets the stretchy_report_param_date_options of this GetReportMailingJobsTemplate.


        :param stretchy_report_param_date_options: The stretchy_report_param_date_options of this GetReportMailingJobsTemplate.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._stretchy_report_param_date_options = stretchy_report_param_date_options

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
        if issubclass(GetReportMailingJobsTemplate, dict):
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
        if not isinstance(other, GetReportMailingJobsTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
