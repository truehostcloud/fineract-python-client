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

class CenterData(object):
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
        'account_no': 'str',
        'collection_meeting_calendar': 'CalendarData',
        'datatables': 'list[DatatableData]',
        'hierarchy': 'str',
        'id': 'int',
        'name': 'str',
        'office_name': 'str',
        'row_index': 'int',
        'staff_name': 'str'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'collection_meeting_calendar': 'collectionMeetingCalendar',
        'datatables': 'datatables',
        'hierarchy': 'hierarchy',
        'id': 'id',
        'name': 'name',
        'office_name': 'officeName',
        'row_index': 'rowIndex',
        'staff_name': 'staffName'
    }

    def __init__(self, account_no=None, collection_meeting_calendar=None, datatables=None, hierarchy=None, id=None, name=None, office_name=None, row_index=None, staff_name=None):  # noqa: E501
        """CenterData - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._collection_meeting_calendar = None
        self._datatables = None
        self._hierarchy = None
        self._id = None
        self._name = None
        self._office_name = None
        self._row_index = None
        self._staff_name = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if collection_meeting_calendar is not None:
            self.collection_meeting_calendar = collection_meeting_calendar
        if datatables is not None:
            self.datatables = datatables
        if hierarchy is not None:
            self.hierarchy = hierarchy
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if office_name is not None:
            self.office_name = office_name
        if row_index is not None:
            self.row_index = row_index
        if staff_name is not None:
            self.staff_name = staff_name

    @property
    def account_no(self):
        """Gets the account_no of this CenterData.  # noqa: E501


        :return: The account_no of this CenterData.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this CenterData.


        :param account_no: The account_no of this CenterData.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def collection_meeting_calendar(self):
        """Gets the collection_meeting_calendar of this CenterData.  # noqa: E501


        :return: The collection_meeting_calendar of this CenterData.  # noqa: E501
        :rtype: CalendarData
        """
        return self._collection_meeting_calendar

    @collection_meeting_calendar.setter
    def collection_meeting_calendar(self, collection_meeting_calendar):
        """Sets the collection_meeting_calendar of this CenterData.


        :param collection_meeting_calendar: The collection_meeting_calendar of this CenterData.  # noqa: E501
        :type: CalendarData
        """

        self._collection_meeting_calendar = collection_meeting_calendar

    @property
    def datatables(self):
        """Gets the datatables of this CenterData.  # noqa: E501


        :return: The datatables of this CenterData.  # noqa: E501
        :rtype: list[DatatableData]
        """
        return self._datatables

    @datatables.setter
    def datatables(self, datatables):
        """Sets the datatables of this CenterData.


        :param datatables: The datatables of this CenterData.  # noqa: E501
        :type: list[DatatableData]
        """

        self._datatables = datatables

    @property
    def hierarchy(self):
        """Gets the hierarchy of this CenterData.  # noqa: E501


        :return: The hierarchy of this CenterData.  # noqa: E501
        :rtype: str
        """
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        """Sets the hierarchy of this CenterData.


        :param hierarchy: The hierarchy of this CenterData.  # noqa: E501
        :type: str
        """

        self._hierarchy = hierarchy

    @property
    def id(self):
        """Gets the id of this CenterData.  # noqa: E501


        :return: The id of this CenterData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CenterData.


        :param id: The id of this CenterData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CenterData.  # noqa: E501


        :return: The name of this CenterData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CenterData.


        :param name: The name of this CenterData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def office_name(self):
        """Gets the office_name of this CenterData.  # noqa: E501


        :return: The office_name of this CenterData.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this CenterData.


        :param office_name: The office_name of this CenterData.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def row_index(self):
        """Gets the row_index of this CenterData.  # noqa: E501


        :return: The row_index of this CenterData.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this CenterData.


        :param row_index: The row_index of this CenterData.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def staff_name(self):
        """Gets the staff_name of this CenterData.  # noqa: E501


        :return: The staff_name of this CenterData.  # noqa: E501
        :rtype: str
        """
        return self._staff_name

    @staff_name.setter
    def staff_name(self, staff_name):
        """Sets the staff_name of this CenterData.


        :param staff_name: The staff_name of this CenterData.  # noqa: E501
        :type: str
        """

        self._staff_name = staff_name

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
        if issubclass(CenterData, dict):
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
        if not isinstance(other, CenterData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
