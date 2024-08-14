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

class PutExternalEventConfigurationsRequest(object):
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
        'external_event_configurations': 'dict(str, bool)'
    }

    attribute_map = {
        'external_event_configurations': 'externalEventConfigurations'
    }

    def __init__(self, external_event_configurations=None):  # noqa: E501
        """PutExternalEventConfigurationsRequest - a model defined in Swagger"""  # noqa: E501
        self._external_event_configurations = None
        self.discriminator = None
        if external_event_configurations is not None:
            self.external_event_configurations = external_event_configurations

    @property
    def external_event_configurations(self):
        """Gets the external_event_configurations of this PutExternalEventConfigurationsRequest.  # noqa: E501


        :return: The external_event_configurations of this PutExternalEventConfigurationsRequest.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._external_event_configurations

    @external_event_configurations.setter
    def external_event_configurations(self, external_event_configurations):
        """Sets the external_event_configurations of this PutExternalEventConfigurationsRequest.


        :param external_event_configurations: The external_event_configurations of this PutExternalEventConfigurationsRequest.  # noqa: E501
        :type: dict(str, bool)
        """

        self._external_event_configurations = external_event_configurations

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
        if issubclass(PutExternalEventConfigurationsRequest, dict):
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
        if not isinstance(other, PutExternalEventConfigurationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
