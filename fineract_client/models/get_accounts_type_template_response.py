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

class GetAccountsTypeTemplateResponse(object):
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
        'client_id': 'int',
        'client_name': 'str',
        'product_options': 'list[GetAccountsTypeProductOptions]'
    }

    attribute_map = {
        'client_id': 'clientId',
        'client_name': 'clientName',
        'product_options': 'productOptions'
    }

    def __init__(self, client_id=None, client_name=None, product_options=None):  # noqa: E501
        """GetAccountsTypeTemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._client_name = None
        self._product_options = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if product_options is not None:
            self.product_options = product_options

    @property
    def client_id(self):
        """Gets the client_id of this GetAccountsTypeTemplateResponse.  # noqa: E501


        :return: The client_id of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetAccountsTypeTemplateResponse.


        :param client_id: The client_id of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this GetAccountsTypeTemplateResponse.  # noqa: E501


        :return: The client_name of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this GetAccountsTypeTemplateResponse.


        :param client_name: The client_name of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def product_options(self):
        """Gets the product_options of this GetAccountsTypeTemplateResponse.  # noqa: E501


        :return: The product_options of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :rtype: list[GetAccountsTypeProductOptions]
        """
        return self._product_options

    @product_options.setter
    def product_options(self, product_options):
        """Sets the product_options of this GetAccountsTypeTemplateResponse.


        :param product_options: The product_options of this GetAccountsTypeTemplateResponse.  # noqa: E501
        :type: list[GetAccountsTypeProductOptions]
        """

        self._product_options = product_options

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
        if issubclass(GetAccountsTypeTemplateResponse, dict):
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
        if not isinstance(other, GetAccountsTypeTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
