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

class Rate(object):
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
        'active': 'bool',
        'approve_user': 'AppUser',
        'created_by': 'int',
        'created_date': 'datetime',
        'id': 'int',
        'last_modified_by': 'int',
        'last_modified_date': 'datetime',
        'name': 'str',
        'new': 'bool',
        'percentage': 'float',
        'product_apply': 'int'
    }

    attribute_map = {
        'active': 'active',
        'approve_user': 'approveUser',
        'created_by': 'createdBy',
        'created_date': 'createdDate',
        'id': 'id',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_date': 'lastModifiedDate',
        'name': 'name',
        'new': 'new',
        'percentage': 'percentage',
        'product_apply': 'productApply'
    }

    def __init__(self, active=None, approve_user=None, created_by=None, created_date=None, id=None, last_modified_by=None, last_modified_date=None, name=None, new=None, percentage=None, product_apply=None):  # noqa: E501
        """Rate - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._approve_user = None
        self._created_by = None
        self._created_date = None
        self._id = None
        self._last_modified_by = None
        self._last_modified_date = None
        self._name = None
        self._new = None
        self._percentage = None
        self._product_apply = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if approve_user is not None:
            self.approve_user = approve_user
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if name is not None:
            self.name = name
        if new is not None:
            self.new = new
        if percentage is not None:
            self.percentage = percentage
        if product_apply is not None:
            self.product_apply = product_apply

    @property
    def active(self):
        """Gets the active of this Rate.  # noqa: E501


        :return: The active of this Rate.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Rate.


        :param active: The active of this Rate.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def approve_user(self):
        """Gets the approve_user of this Rate.  # noqa: E501


        :return: The approve_user of this Rate.  # noqa: E501
        :rtype: AppUser
        """
        return self._approve_user

    @approve_user.setter
    def approve_user(self, approve_user):
        """Sets the approve_user of this Rate.


        :param approve_user: The approve_user of this Rate.  # noqa: E501
        :type: AppUser
        """

        self._approve_user = approve_user

    @property
    def created_by(self):
        """Gets the created_by of this Rate.  # noqa: E501


        :return: The created_by of this Rate.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Rate.


        :param created_by: The created_by of this Rate.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def created_date(self):
        """Gets the created_date of this Rate.  # noqa: E501


        :return: The created_date of this Rate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Rate.


        :param created_date: The created_date of this Rate.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this Rate.  # noqa: E501


        :return: The id of this Rate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rate.


        :param id: The id of this Rate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Rate.  # noqa: E501


        :return: The last_modified_by of this Rate.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Rate.


        :param last_modified_by: The last_modified_by of this Rate.  # noqa: E501
        :type: int
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Rate.  # noqa: E501


        :return: The last_modified_date of this Rate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Rate.


        :param last_modified_date: The last_modified_date of this Rate.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def name(self):
        """Gets the name of this Rate.  # noqa: E501


        :return: The name of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rate.


        :param name: The name of this Rate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new(self):
        """Gets the new of this Rate.  # noqa: E501


        :return: The new of this Rate.  # noqa: E501
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this Rate.


        :param new: The new of this Rate.  # noqa: E501
        :type: bool
        """

        self._new = new

    @property
    def percentage(self):
        """Gets the percentage of this Rate.  # noqa: E501


        :return: The percentage of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Rate.


        :param percentage: The percentage of this Rate.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def product_apply(self):
        """Gets the product_apply of this Rate.  # noqa: E501


        :return: The product_apply of this Rate.  # noqa: E501
        :rtype: int
        """
        return self._product_apply

    @product_apply.setter
    def product_apply(self, product_apply):
        """Sets the product_apply of this Rate.


        :param product_apply: The product_apply of this Rate.  # noqa: E501
        :type: int
        """

        self._product_apply = product_apply

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
        if issubclass(Rate, dict):
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
        if not isinstance(other, Rate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
