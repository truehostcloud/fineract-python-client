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

class PutDataTablesRequestChangeColumns(object):
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
        'code': 'str',
        'indexed': 'bool',
        'mandatory': 'bool',
        'name': 'str',
        'new_code': 'str',
        'new_name': 'str',
        'unique': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'indexed': 'indexed',
        'mandatory': 'mandatory',
        'name': 'name',
        'new_code': 'newCode',
        'new_name': 'newName',
        'unique': 'unique'
    }

    def __init__(self, code=None, indexed=None, mandatory=None, name=None, new_code=None, new_name=None, unique=None):  # noqa: E501
        """PutDataTablesRequestChangeColumns - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._indexed = None
        self._mandatory = None
        self._name = None
        self._new_code = None
        self._new_name = None
        self._unique = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if indexed is not None:
            self.indexed = indexed
        if mandatory is not None:
            self.mandatory = mandatory
        if name is not None:
            self.name = name
        if new_code is not None:
            self.new_code = new_code
        if new_name is not None:
            self.new_name = new_name
        if unique is not None:
            self.unique = unique

    @property
    def code(self):
        """Gets the code of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The code of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PutDataTablesRequestChangeColumns.


        :param code: The code of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def indexed(self):
        """Gets the indexed of this PutDataTablesRequestChangeColumns.  # noqa: E501

        Defaults to false  # noqa: E501

        :return: The indexed of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: bool
        """
        return self._indexed

    @indexed.setter
    def indexed(self, indexed):
        """Sets the indexed of this PutDataTablesRequestChangeColumns.

        Defaults to false  # noqa: E501

        :param indexed: The indexed of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: bool
        """

        self._indexed = indexed

    @property
    def mandatory(self):
        """Gets the mandatory of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The mandatory of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this PutDataTablesRequestChangeColumns.


        :param mandatory: The mandatory of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def name(self):
        """Gets the name of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The name of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutDataTablesRequestChangeColumns.


        :param name: The name of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_code(self):
        """Gets the new_code of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The new_code of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: str
        """
        return self._new_code

    @new_code.setter
    def new_code(self, new_code):
        """Sets the new_code of this PutDataTablesRequestChangeColumns.


        :param new_code: The new_code of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: str
        """

        self._new_code = new_code

    @property
    def new_name(self):
        """Gets the new_name of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The new_name of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this PutDataTablesRequestChangeColumns.


        :param new_name: The new_name of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def unique(self):
        """Gets the unique of this PutDataTablesRequestChangeColumns.  # noqa: E501


        :return: The unique of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :rtype: bool
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this PutDataTablesRequestChangeColumns.


        :param unique: The unique of this PutDataTablesRequestChangeColumns.  # noqa: E501
        :type: bool
        """

        self._unique = unique

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
        if issubclass(PutDataTablesRequestChangeColumns, dict):
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
        if not isinstance(other, PutDataTablesRequestChangeColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
