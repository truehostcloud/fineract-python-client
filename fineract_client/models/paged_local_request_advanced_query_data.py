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

class PagedLocalRequestAdvancedQueryData(object):
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
        'date_format': 'str',
        'date_time_format': 'str',
        'locale': 'str',
        'locale_object': 'PagedLocalRequestAdvancedQueryDataLocaleObject',
        'page': 'int',
        'request': 'AdvancedQueryData',
        'size': 'int',
        'sorts': 'list[SortOrder]'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'date_time_format': 'dateTimeFormat',
        'locale': 'locale',
        'locale_object': 'localeObject',
        'page': 'page',
        'request': 'request',
        'size': 'size',
        'sorts': 'sorts'
    }

    def __init__(self, date_format=None, date_time_format=None, locale=None, locale_object=None, page=None, request=None, size=None, sorts=None):  # noqa: E501
        """PagedLocalRequestAdvancedQueryData - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._date_time_format = None
        self._locale = None
        self._locale_object = None
        self._page = None
        self._request = None
        self._size = None
        self._sorts = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if date_time_format is not None:
            self.date_time_format = date_time_format
        if locale is not None:
            self.locale = locale
        if locale_object is not None:
            self.locale_object = locale_object
        if page is not None:
            self.page = page
        if request is not None:
            self.request = request
        if size is not None:
            self.size = size
        if sorts is not None:
            self.sorts = sorts

    @property
    def date_format(self):
        """Gets the date_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The date_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PagedLocalRequestAdvancedQueryData.


        :param date_format: The date_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def date_time_format(self):
        """Gets the date_time_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The date_time_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: str
        """
        return self._date_time_format

    @date_time_format.setter
    def date_time_format(self, date_time_format):
        """Sets the date_time_format of this PagedLocalRequestAdvancedQueryData.


        :param date_time_format: The date_time_format of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: str
        """

        self._date_time_format = date_time_format

    @property
    def locale(self):
        """Gets the locale of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The locale of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PagedLocalRequestAdvancedQueryData.


        :param locale: The locale of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def locale_object(self):
        """Gets the locale_object of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The locale_object of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: PagedLocalRequestAdvancedQueryDataLocaleObject
        """
        return self._locale_object

    @locale_object.setter
    def locale_object(self, locale_object):
        """Sets the locale_object of this PagedLocalRequestAdvancedQueryData.


        :param locale_object: The locale_object of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: PagedLocalRequestAdvancedQueryDataLocaleObject
        """

        self._locale_object = locale_object

    @property
    def page(self):
        """Gets the page of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The page of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PagedLocalRequestAdvancedQueryData.


        :param page: The page of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def request(self):
        """Gets the request of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The request of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: AdvancedQueryData
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this PagedLocalRequestAdvancedQueryData.


        :param request: The request of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: AdvancedQueryData
        """

        self._request = request

    @property
    def size(self):
        """Gets the size of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The size of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PagedLocalRequestAdvancedQueryData.


        :param size: The size of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def sorts(self):
        """Gets the sorts of this PagedLocalRequestAdvancedQueryData.  # noqa: E501


        :return: The sorts of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :rtype: list[SortOrder]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """Sets the sorts of this PagedLocalRequestAdvancedQueryData.


        :param sorts: The sorts of this PagedLocalRequestAdvancedQueryData.  # noqa: E501
        :type: list[SortOrder]
        """

        self._sorts = sorts

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
        if issubclass(PagedLocalRequestAdvancedQueryData, dict):
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
        if not isinstance(other, PagedLocalRequestAdvancedQueryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
