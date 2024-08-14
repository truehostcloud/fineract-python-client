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

class PostClientsClientIdIdentifiersRequest(object):
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
        'description': 'str',
        'document_key': 'str',
        'document_type_id': 'int',
        'status': 'str'
    }

    attribute_map = {
        'description': 'description',
        'document_key': 'documentKey',
        'document_type_id': 'documentTypeId',
        'status': 'status'
    }

    def __init__(self, description=None, document_key=None, document_type_id=None, status=None):  # noqa: E501
        """PostClientsClientIdIdentifiersRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._document_key = None
        self._document_type_id = None
        self._status = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if document_key is not None:
            self.document_key = document_key
        if document_type_id is not None:
            self.document_type_id = document_type_id
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this PostClientsClientIdIdentifiersRequest.  # noqa: E501


        :return: The description of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostClientsClientIdIdentifiersRequest.


        :param description: The description of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def document_key(self):
        """Gets the document_key of this PostClientsClientIdIdentifiersRequest.  # noqa: E501


        :return: The document_key of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :rtype: str
        """
        return self._document_key

    @document_key.setter
    def document_key(self, document_key):
        """Sets the document_key of this PostClientsClientIdIdentifiersRequest.


        :param document_key: The document_key of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :type: str
        """

        self._document_key = document_key

    @property
    def document_type_id(self):
        """Gets the document_type_id of this PostClientsClientIdIdentifiersRequest.  # noqa: E501


        :return: The document_type_id of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :rtype: int
        """
        return self._document_type_id

    @document_type_id.setter
    def document_type_id(self, document_type_id):
        """Sets the document_type_id of this PostClientsClientIdIdentifiersRequest.


        :param document_type_id: The document_type_id of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :type: int
        """

        self._document_type_id = document_type_id

    @property
    def status(self):
        """Gets the status of this PostClientsClientIdIdentifiersRequest.  # noqa: E501


        :return: The status of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostClientsClientIdIdentifiersRequest.


        :param status: The status of this PostClientsClientIdIdentifiersRequest.  # noqa: E501
        :type: str
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
        if issubclass(PostClientsClientIdIdentifiersRequest, dict):
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
        if not isinstance(other, PostClientsClientIdIdentifiersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
