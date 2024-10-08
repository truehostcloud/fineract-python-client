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

class GetProvisioningCriteriaCriteriaIdResponse(object):
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
        'created_by': 'str',
        'criteria_id': 'int',
        'criteria_name': 'str',
        'loan_products': 'list[LoanProductData]',
        'provisioningcriteria': 'list[ProvisioningCriteriaDefinitionData]'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'criteria_id': 'criteriaId',
        'criteria_name': 'criteriaName',
        'loan_products': 'loanProducts',
        'provisioningcriteria': 'provisioningcriteria'
    }

    def __init__(self, created_by=None, criteria_id=None, criteria_name=None, loan_products=None, provisioningcriteria=None):  # noqa: E501
        """GetProvisioningCriteriaCriteriaIdResponse - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._criteria_id = None
        self._criteria_name = None
        self._loan_products = None
        self._provisioningcriteria = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if criteria_id is not None:
            self.criteria_id = criteria_id
        if criteria_name is not None:
            self.criteria_name = criteria_name
        if loan_products is not None:
            self.loan_products = loan_products
        if provisioningcriteria is not None:
            self.provisioningcriteria = provisioningcriteria

    @property
    def created_by(self):
        """Gets the created_by of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501


        :return: The created_by of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetProvisioningCriteriaCriteriaIdResponse.


        :param created_by: The created_by of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def criteria_id(self):
        """Gets the criteria_id of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501


        :return: The criteria_id of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :rtype: int
        """
        return self._criteria_id

    @criteria_id.setter
    def criteria_id(self, criteria_id):
        """Sets the criteria_id of this GetProvisioningCriteriaCriteriaIdResponse.


        :param criteria_id: The criteria_id of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :type: int
        """

        self._criteria_id = criteria_id

    @property
    def criteria_name(self):
        """Gets the criteria_name of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501


        :return: The criteria_name of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._criteria_name

    @criteria_name.setter
    def criteria_name(self, criteria_name):
        """Sets the criteria_name of this GetProvisioningCriteriaCriteriaIdResponse.


        :param criteria_name: The criteria_name of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :type: str
        """

        self._criteria_name = criteria_name

    @property
    def loan_products(self):
        """Gets the loan_products of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501


        :return: The loan_products of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :rtype: list[LoanProductData]
        """
        return self._loan_products

    @loan_products.setter
    def loan_products(self, loan_products):
        """Sets the loan_products of this GetProvisioningCriteriaCriteriaIdResponse.


        :param loan_products: The loan_products of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :type: list[LoanProductData]
        """

        self._loan_products = loan_products

    @property
    def provisioningcriteria(self):
        """Gets the provisioningcriteria of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501


        :return: The provisioningcriteria of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :rtype: list[ProvisioningCriteriaDefinitionData]
        """
        return self._provisioningcriteria

    @provisioningcriteria.setter
    def provisioningcriteria(self, provisioningcriteria):
        """Sets the provisioningcriteria of this GetProvisioningCriteriaCriteriaIdResponse.


        :param provisioningcriteria: The provisioningcriteria of this GetProvisioningCriteriaCriteriaIdResponse.  # noqa: E501
        :type: list[ProvisioningCriteriaDefinitionData]
        """

        self._provisioningcriteria = provisioningcriteria

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
        if issubclass(GetProvisioningCriteriaCriteriaIdResponse, dict):
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
        if not isinstance(other, GetProvisioningCriteriaCriteriaIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
