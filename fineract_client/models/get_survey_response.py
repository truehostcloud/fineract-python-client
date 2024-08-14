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

class GetSurveyResponse(object):
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
        'datatable_data': 'GetSurveyResponseDatatableData',
        'enabled': 'bool'
    }

    attribute_map = {
        'datatable_data': 'datatableData',
        'enabled': 'enabled'
    }

    def __init__(self, datatable_data=None, enabled=None):  # noqa: E501
        """GetSurveyResponse - a model defined in Swagger"""  # noqa: E501
        self._datatable_data = None
        self._enabled = None
        self.discriminator = None
        if datatable_data is not None:
            self.datatable_data = datatable_data
        if enabled is not None:
            self.enabled = enabled

    @property
    def datatable_data(self):
        """Gets the datatable_data of this GetSurveyResponse.  # noqa: E501


        :return: The datatable_data of this GetSurveyResponse.  # noqa: E501
        :rtype: GetSurveyResponseDatatableData
        """
        return self._datatable_data

    @datatable_data.setter
    def datatable_data(self, datatable_data):
        """Sets the datatable_data of this GetSurveyResponse.


        :param datatable_data: The datatable_data of this GetSurveyResponse.  # noqa: E501
        :type: GetSurveyResponseDatatableData
        """

        self._datatable_data = datatable_data

    @property
    def enabled(self):
        """Gets the enabled of this GetSurveyResponse.  # noqa: E501


        :return: The enabled of this GetSurveyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetSurveyResponse.


        :param enabled: The enabled of this GetSurveyResponse.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(GetSurveyResponse, dict):
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
        if not isinstance(other, GetSurveyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
