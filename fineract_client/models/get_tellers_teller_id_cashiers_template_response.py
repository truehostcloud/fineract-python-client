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

class GetTellersTellerIdCashiersTemplateResponse(object):
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
        'office_id': 'int',
        'office_name': 'str',
        'staff_options': 'list[StaffData]',
        'teller_id': 'int',
        'teller_name': 'str'
    }

    attribute_map = {
        'office_id': 'officeId',
        'office_name': 'officeName',
        'staff_options': 'staffOptions',
        'teller_id': 'tellerId',
        'teller_name': 'tellerName'
    }

    def __init__(self, office_id=None, office_name=None, staff_options=None, teller_id=None, teller_name=None):  # noqa: E501
        """GetTellersTellerIdCashiersTemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._office_id = None
        self._office_name = None
        self._staff_options = None
        self._teller_id = None
        self._teller_name = None
        self.discriminator = None
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if staff_options is not None:
            self.staff_options = staff_options
        if teller_id is not None:
            self.teller_id = teller_id
        if teller_name is not None:
            self.teller_name = teller_name

    @property
    def office_id(self):
        """Gets the office_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501


        :return: The office_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetTellersTellerIdCashiersTemplateResponse.


        :param office_id: The office_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501


        :return: The office_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GetTellersTellerIdCashiersTemplateResponse.


        :param office_name: The office_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def staff_options(self):
        """Gets the staff_options of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501


        :return: The staff_options of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :rtype: list[StaffData]
        """
        return self._staff_options

    @staff_options.setter
    def staff_options(self, staff_options):
        """Sets the staff_options of this GetTellersTellerIdCashiersTemplateResponse.


        :param staff_options: The staff_options of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :type: list[StaffData]
        """

        self._staff_options = staff_options

    @property
    def teller_id(self):
        """Gets the teller_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501


        :return: The teller_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :rtype: int
        """
        return self._teller_id

    @teller_id.setter
    def teller_id(self, teller_id):
        """Sets the teller_id of this GetTellersTellerIdCashiersTemplateResponse.


        :param teller_id: The teller_id of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :type: int
        """

        self._teller_id = teller_id

    @property
    def teller_name(self):
        """Gets the teller_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501


        :return: The teller_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._teller_name

    @teller_name.setter
    def teller_name(self, teller_name):
        """Sets the teller_name of this GetTellersTellerIdCashiersTemplateResponse.


        :param teller_name: The teller_name of this GetTellersTellerIdCashiersTemplateResponse.  # noqa: E501
        :type: str
        """

        self._teller_name = teller_name

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
        if issubclass(GetTellersTellerIdCashiersTemplateResponse, dict):
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
        if not isinstance(other, GetTellersTellerIdCashiersTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
