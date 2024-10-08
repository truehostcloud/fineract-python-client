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

class BatchRequest(object):
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
        'body': 'str',
        'headers': 'list[Header]',
        'method': 'str',
        'reference': 'int',
        'relative_url': 'str',
        'request_id': 'int'
    }

    attribute_map = {
        'body': 'body',
        'headers': 'headers',
        'method': 'method',
        'reference': 'reference',
        'relative_url': 'relativeUrl',
        'request_id': 'requestId'
    }

    def __init__(self, body=None, headers=None, method=None, reference=None, relative_url=None, request_id=None):  # noqa: E501
        """BatchRequest - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._headers = None
        self._method = None
        self._reference = None
        self._relative_url = None
        self._request_id = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if headers is not None:
            self.headers = headers
        if method is not None:
            self.method = method
        if reference is not None:
            self.reference = reference
        if relative_url is not None:
            self.relative_url = relative_url
        if request_id is not None:
            self.request_id = request_id

    @property
    def body(self):
        """Gets the body of this BatchRequest.  # noqa: E501


        :return: The body of this BatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchRequest.


        :param body: The body of this BatchRequest.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def headers(self):
        """Gets the headers of this BatchRequest.  # noqa: E501


        :return: The headers of this BatchRequest.  # noqa: E501
        :rtype: list[Header]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this BatchRequest.


        :param headers: The headers of this BatchRequest.  # noqa: E501
        :type: list[Header]
        """

        self._headers = headers

    @property
    def method(self):
        """Gets the method of this BatchRequest.  # noqa: E501


        :return: The method of this BatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BatchRequest.


        :param method: The method of this BatchRequest.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def reference(self):
        """Gets the reference of this BatchRequest.  # noqa: E501


        :return: The reference of this BatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BatchRequest.


        :param reference: The reference of this BatchRequest.  # noqa: E501
        :type: int
        """

        self._reference = reference

    @property
    def relative_url(self):
        """Gets the relative_url of this BatchRequest.  # noqa: E501


        :return: The relative_url of this BatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._relative_url

    @relative_url.setter
    def relative_url(self, relative_url):
        """Sets the relative_url of this BatchRequest.


        :param relative_url: The relative_url of this BatchRequest.  # noqa: E501
        :type: str
        """

        self._relative_url = relative_url

    @property
    def request_id(self):
        """Gets the request_id of this BatchRequest.  # noqa: E501


        :return: The request_id of this BatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this BatchRequest.


        :param request_id: The request_id of this BatchRequest.  # noqa: E501
        :type: int
        """

        self._request_id = request_id

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
        if issubclass(BatchRequest, dict):
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
        if not isinstance(other, BatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
