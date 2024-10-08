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

class GroupGeneralData(object):
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
        'activation_date': 'date',
        'active': 'bool',
        'active_client_members': 'list[ClientData]',
        'available_roles': 'list[CodeValueData]',
        'calendars_data': 'list[CalendarData]',
        'center_id': 'int',
        'center_name': 'str',
        'center_options': 'list[CenterData]',
        'child_group': 'bool',
        'client_members': 'list[ClientData]',
        'client_options': 'list[ClientData]',
        'closure_reasons': 'list[CodeValueData]',
        'collection_meeting_calendar': 'CalendarData',
        'datatables': 'list[DatatableData]',
        'date_format': 'str',
        'external_id': 'str',
        'group_level': 'str',
        'group_roles': 'list[GroupRoleData]',
        'hierarchy': 'str',
        'id': 'int',
        'locale': 'str',
        'name': 'str',
        'office_id': 'int',
        'office_name': 'str',
        'office_options': 'list[OfficeData]',
        'parent_id': 'int',
        'row_index': 'int',
        'selected_role': 'GroupRoleData',
        'staff_id': 'int',
        'staff_name': 'str',
        'staff_options': 'list[StaffData]',
        'status': 'EnumOptionData',
        'submitted_on_date': 'date',
        'timeline': 'GroupTimelineData'
    }

    attribute_map = {
        'account_no': 'accountNo',
        'activation_date': 'activationDate',
        'active': 'active',
        'active_client_members': 'activeClientMembers',
        'available_roles': 'availableRoles',
        'calendars_data': 'calendarsData',
        'center_id': 'centerId',
        'center_name': 'centerName',
        'center_options': 'centerOptions',
        'child_group': 'childGroup',
        'client_members': 'clientMembers',
        'client_options': 'clientOptions',
        'closure_reasons': 'closureReasons',
        'collection_meeting_calendar': 'collectionMeetingCalendar',
        'datatables': 'datatables',
        'date_format': 'dateFormat',
        'external_id': 'externalId',
        'group_level': 'groupLevel',
        'group_roles': 'groupRoles',
        'hierarchy': 'hierarchy',
        'id': 'id',
        'locale': 'locale',
        'name': 'name',
        'office_id': 'officeId',
        'office_name': 'officeName',
        'office_options': 'officeOptions',
        'parent_id': 'parentId',
        'row_index': 'rowIndex',
        'selected_role': 'selectedRole',
        'staff_id': 'staffId',
        'staff_name': 'staffName',
        'staff_options': 'staffOptions',
        'status': 'status',
        'submitted_on_date': 'submittedOnDate',
        'timeline': 'timeline'
    }

    def __init__(self, account_no=None, activation_date=None, active=None, active_client_members=None, available_roles=None, calendars_data=None, center_id=None, center_name=None, center_options=None, child_group=None, client_members=None, client_options=None, closure_reasons=None, collection_meeting_calendar=None, datatables=None, date_format=None, external_id=None, group_level=None, group_roles=None, hierarchy=None, id=None, locale=None, name=None, office_id=None, office_name=None, office_options=None, parent_id=None, row_index=None, selected_role=None, staff_id=None, staff_name=None, staff_options=None, status=None, submitted_on_date=None, timeline=None):  # noqa: E501
        """GroupGeneralData - a model defined in Swagger"""  # noqa: E501
        self._account_no = None
        self._activation_date = None
        self._active = None
        self._active_client_members = None
        self._available_roles = None
        self._calendars_data = None
        self._center_id = None
        self._center_name = None
        self._center_options = None
        self._child_group = None
        self._client_members = None
        self._client_options = None
        self._closure_reasons = None
        self._collection_meeting_calendar = None
        self._datatables = None
        self._date_format = None
        self._external_id = None
        self._group_level = None
        self._group_roles = None
        self._hierarchy = None
        self._id = None
        self._locale = None
        self._name = None
        self._office_id = None
        self._office_name = None
        self._office_options = None
        self._parent_id = None
        self._row_index = None
        self._selected_role = None
        self._staff_id = None
        self._staff_name = None
        self._staff_options = None
        self._status = None
        self._submitted_on_date = None
        self._timeline = None
        self.discriminator = None
        if account_no is not None:
            self.account_no = account_no
        if activation_date is not None:
            self.activation_date = activation_date
        if active is not None:
            self.active = active
        if active_client_members is not None:
            self.active_client_members = active_client_members
        if available_roles is not None:
            self.available_roles = available_roles
        if calendars_data is not None:
            self.calendars_data = calendars_data
        if center_id is not None:
            self.center_id = center_id
        if center_name is not None:
            self.center_name = center_name
        if center_options is not None:
            self.center_options = center_options
        if child_group is not None:
            self.child_group = child_group
        if client_members is not None:
            self.client_members = client_members
        if client_options is not None:
            self.client_options = client_options
        if closure_reasons is not None:
            self.closure_reasons = closure_reasons
        if collection_meeting_calendar is not None:
            self.collection_meeting_calendar = collection_meeting_calendar
        if datatables is not None:
            self.datatables = datatables
        if date_format is not None:
            self.date_format = date_format
        if external_id is not None:
            self.external_id = external_id
        if group_level is not None:
            self.group_level = group_level
        if group_roles is not None:
            self.group_roles = group_roles
        if hierarchy is not None:
            self.hierarchy = hierarchy
        if id is not None:
            self.id = id
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if office_id is not None:
            self.office_id = office_id
        if office_name is not None:
            self.office_name = office_name
        if office_options is not None:
            self.office_options = office_options
        if parent_id is not None:
            self.parent_id = parent_id
        if row_index is not None:
            self.row_index = row_index
        if selected_role is not None:
            self.selected_role = selected_role
        if staff_id is not None:
            self.staff_id = staff_id
        if staff_name is not None:
            self.staff_name = staff_name
        if staff_options is not None:
            self.staff_options = staff_options
        if status is not None:
            self.status = status
        if submitted_on_date is not None:
            self.submitted_on_date = submitted_on_date
        if timeline is not None:
            self.timeline = timeline

    @property
    def account_no(self):
        """Gets the account_no of this GroupGeneralData.  # noqa: E501


        :return: The account_no of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        """Sets the account_no of this GroupGeneralData.


        :param account_no: The account_no of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._account_no = account_no

    @property
    def activation_date(self):
        """Gets the activation_date of this GroupGeneralData.  # noqa: E501


        :return: The activation_date of this GroupGeneralData.  # noqa: E501
        :rtype: date
        """
        return self._activation_date

    @activation_date.setter
    def activation_date(self, activation_date):
        """Sets the activation_date of this GroupGeneralData.


        :param activation_date: The activation_date of this GroupGeneralData.  # noqa: E501
        :type: date
        """

        self._activation_date = activation_date

    @property
    def active(self):
        """Gets the active of this GroupGeneralData.  # noqa: E501


        :return: The active of this GroupGeneralData.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GroupGeneralData.


        :param active: The active of this GroupGeneralData.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def active_client_members(self):
        """Gets the active_client_members of this GroupGeneralData.  # noqa: E501


        :return: The active_client_members of this GroupGeneralData.  # noqa: E501
        :rtype: list[ClientData]
        """
        return self._active_client_members

    @active_client_members.setter
    def active_client_members(self, active_client_members):
        """Sets the active_client_members of this GroupGeneralData.


        :param active_client_members: The active_client_members of this GroupGeneralData.  # noqa: E501
        :type: list[ClientData]
        """

        self._active_client_members = active_client_members

    @property
    def available_roles(self):
        """Gets the available_roles of this GroupGeneralData.  # noqa: E501


        :return: The available_roles of this GroupGeneralData.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._available_roles

    @available_roles.setter
    def available_roles(self, available_roles):
        """Sets the available_roles of this GroupGeneralData.


        :param available_roles: The available_roles of this GroupGeneralData.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._available_roles = available_roles

    @property
    def calendars_data(self):
        """Gets the calendars_data of this GroupGeneralData.  # noqa: E501


        :return: The calendars_data of this GroupGeneralData.  # noqa: E501
        :rtype: list[CalendarData]
        """
        return self._calendars_data

    @calendars_data.setter
    def calendars_data(self, calendars_data):
        """Sets the calendars_data of this GroupGeneralData.


        :param calendars_data: The calendars_data of this GroupGeneralData.  # noqa: E501
        :type: list[CalendarData]
        """

        self._calendars_data = calendars_data

    @property
    def center_id(self):
        """Gets the center_id of this GroupGeneralData.  # noqa: E501


        :return: The center_id of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._center_id

    @center_id.setter
    def center_id(self, center_id):
        """Sets the center_id of this GroupGeneralData.


        :param center_id: The center_id of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._center_id = center_id

    @property
    def center_name(self):
        """Gets the center_name of this GroupGeneralData.  # noqa: E501


        :return: The center_name of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._center_name

    @center_name.setter
    def center_name(self, center_name):
        """Sets the center_name of this GroupGeneralData.


        :param center_name: The center_name of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._center_name = center_name

    @property
    def center_options(self):
        """Gets the center_options of this GroupGeneralData.  # noqa: E501


        :return: The center_options of this GroupGeneralData.  # noqa: E501
        :rtype: list[CenterData]
        """
        return self._center_options

    @center_options.setter
    def center_options(self, center_options):
        """Sets the center_options of this GroupGeneralData.


        :param center_options: The center_options of this GroupGeneralData.  # noqa: E501
        :type: list[CenterData]
        """

        self._center_options = center_options

    @property
    def child_group(self):
        """Gets the child_group of this GroupGeneralData.  # noqa: E501


        :return: The child_group of this GroupGeneralData.  # noqa: E501
        :rtype: bool
        """
        return self._child_group

    @child_group.setter
    def child_group(self, child_group):
        """Sets the child_group of this GroupGeneralData.


        :param child_group: The child_group of this GroupGeneralData.  # noqa: E501
        :type: bool
        """

        self._child_group = child_group

    @property
    def client_members(self):
        """Gets the client_members of this GroupGeneralData.  # noqa: E501


        :return: The client_members of this GroupGeneralData.  # noqa: E501
        :rtype: list[ClientData]
        """
        return self._client_members

    @client_members.setter
    def client_members(self, client_members):
        """Sets the client_members of this GroupGeneralData.


        :param client_members: The client_members of this GroupGeneralData.  # noqa: E501
        :type: list[ClientData]
        """

        self._client_members = client_members

    @property
    def client_options(self):
        """Gets the client_options of this GroupGeneralData.  # noqa: E501


        :return: The client_options of this GroupGeneralData.  # noqa: E501
        :rtype: list[ClientData]
        """
        return self._client_options

    @client_options.setter
    def client_options(self, client_options):
        """Sets the client_options of this GroupGeneralData.


        :param client_options: The client_options of this GroupGeneralData.  # noqa: E501
        :type: list[ClientData]
        """

        self._client_options = client_options

    @property
    def closure_reasons(self):
        """Gets the closure_reasons of this GroupGeneralData.  # noqa: E501


        :return: The closure_reasons of this GroupGeneralData.  # noqa: E501
        :rtype: list[CodeValueData]
        """
        return self._closure_reasons

    @closure_reasons.setter
    def closure_reasons(self, closure_reasons):
        """Sets the closure_reasons of this GroupGeneralData.


        :param closure_reasons: The closure_reasons of this GroupGeneralData.  # noqa: E501
        :type: list[CodeValueData]
        """

        self._closure_reasons = closure_reasons

    @property
    def collection_meeting_calendar(self):
        """Gets the collection_meeting_calendar of this GroupGeneralData.  # noqa: E501


        :return: The collection_meeting_calendar of this GroupGeneralData.  # noqa: E501
        :rtype: CalendarData
        """
        return self._collection_meeting_calendar

    @collection_meeting_calendar.setter
    def collection_meeting_calendar(self, collection_meeting_calendar):
        """Sets the collection_meeting_calendar of this GroupGeneralData.


        :param collection_meeting_calendar: The collection_meeting_calendar of this GroupGeneralData.  # noqa: E501
        :type: CalendarData
        """

        self._collection_meeting_calendar = collection_meeting_calendar

    @property
    def datatables(self):
        """Gets the datatables of this GroupGeneralData.  # noqa: E501


        :return: The datatables of this GroupGeneralData.  # noqa: E501
        :rtype: list[DatatableData]
        """
        return self._datatables

    @datatables.setter
    def datatables(self, datatables):
        """Sets the datatables of this GroupGeneralData.


        :param datatables: The datatables of this GroupGeneralData.  # noqa: E501
        :type: list[DatatableData]
        """

        self._datatables = datatables

    @property
    def date_format(self):
        """Gets the date_format of this GroupGeneralData.  # noqa: E501


        :return: The date_format of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this GroupGeneralData.


        :param date_format: The date_format of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def external_id(self):
        """Gets the external_id of this GroupGeneralData.  # noqa: E501


        :return: The external_id of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GroupGeneralData.


        :param external_id: The external_id of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def group_level(self):
        """Gets the group_level of this GroupGeneralData.  # noqa: E501


        :return: The group_level of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._group_level

    @group_level.setter
    def group_level(self, group_level):
        """Sets the group_level of this GroupGeneralData.


        :param group_level: The group_level of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._group_level = group_level

    @property
    def group_roles(self):
        """Gets the group_roles of this GroupGeneralData.  # noqa: E501


        :return: The group_roles of this GroupGeneralData.  # noqa: E501
        :rtype: list[GroupRoleData]
        """
        return self._group_roles

    @group_roles.setter
    def group_roles(self, group_roles):
        """Sets the group_roles of this GroupGeneralData.


        :param group_roles: The group_roles of this GroupGeneralData.  # noqa: E501
        :type: list[GroupRoleData]
        """

        self._group_roles = group_roles

    @property
    def hierarchy(self):
        """Gets the hierarchy of this GroupGeneralData.  # noqa: E501


        :return: The hierarchy of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        """Sets the hierarchy of this GroupGeneralData.


        :param hierarchy: The hierarchy of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._hierarchy = hierarchy

    @property
    def id(self):
        """Gets the id of this GroupGeneralData.  # noqa: E501


        :return: The id of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupGeneralData.


        :param id: The id of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def locale(self):
        """Gets the locale of this GroupGeneralData.  # noqa: E501


        :return: The locale of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this GroupGeneralData.


        :param locale: The locale of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this GroupGeneralData.  # noqa: E501


        :return: The name of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupGeneralData.


        :param name: The name of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def office_id(self):
        """Gets the office_id of this GroupGeneralData.  # noqa: E501


        :return: The office_id of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GroupGeneralData.


        :param office_id: The office_id of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

    @property
    def office_name(self):
        """Gets the office_name of this GroupGeneralData.  # noqa: E501


        :return: The office_name of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._office_name

    @office_name.setter
    def office_name(self, office_name):
        """Sets the office_name of this GroupGeneralData.


        :param office_name: The office_name of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._office_name = office_name

    @property
    def office_options(self):
        """Gets the office_options of this GroupGeneralData.  # noqa: E501


        :return: The office_options of this GroupGeneralData.  # noqa: E501
        :rtype: list[OfficeData]
        """
        return self._office_options

    @office_options.setter
    def office_options(self, office_options):
        """Sets the office_options of this GroupGeneralData.


        :param office_options: The office_options of this GroupGeneralData.  # noqa: E501
        :type: list[OfficeData]
        """

        self._office_options = office_options

    @property
    def parent_id(self):
        """Gets the parent_id of this GroupGeneralData.  # noqa: E501


        :return: The parent_id of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this GroupGeneralData.


        :param parent_id: The parent_id of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def row_index(self):
        """Gets the row_index of this GroupGeneralData.  # noqa: E501


        :return: The row_index of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this GroupGeneralData.


        :param row_index: The row_index of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def selected_role(self):
        """Gets the selected_role of this GroupGeneralData.  # noqa: E501


        :return: The selected_role of this GroupGeneralData.  # noqa: E501
        :rtype: GroupRoleData
        """
        return self._selected_role

    @selected_role.setter
    def selected_role(self, selected_role):
        """Sets the selected_role of this GroupGeneralData.


        :param selected_role: The selected_role of this GroupGeneralData.  # noqa: E501
        :type: GroupRoleData
        """

        self._selected_role = selected_role

    @property
    def staff_id(self):
        """Gets the staff_id of this GroupGeneralData.  # noqa: E501


        :return: The staff_id of this GroupGeneralData.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GroupGeneralData.


        :param staff_id: The staff_id of this GroupGeneralData.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def staff_name(self):
        """Gets the staff_name of this GroupGeneralData.  # noqa: E501


        :return: The staff_name of this GroupGeneralData.  # noqa: E501
        :rtype: str
        """
        return self._staff_name

    @staff_name.setter
    def staff_name(self, staff_name):
        """Sets the staff_name of this GroupGeneralData.


        :param staff_name: The staff_name of this GroupGeneralData.  # noqa: E501
        :type: str
        """

        self._staff_name = staff_name

    @property
    def staff_options(self):
        """Gets the staff_options of this GroupGeneralData.  # noqa: E501


        :return: The staff_options of this GroupGeneralData.  # noqa: E501
        :rtype: list[StaffData]
        """
        return self._staff_options

    @staff_options.setter
    def staff_options(self, staff_options):
        """Sets the staff_options of this GroupGeneralData.


        :param staff_options: The staff_options of this GroupGeneralData.  # noqa: E501
        :type: list[StaffData]
        """

        self._staff_options = staff_options

    @property
    def status(self):
        """Gets the status of this GroupGeneralData.  # noqa: E501


        :return: The status of this GroupGeneralData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GroupGeneralData.


        :param status: The status of this GroupGeneralData.  # noqa: E501
        :type: EnumOptionData
        """

        self._status = status

    @property
    def submitted_on_date(self):
        """Gets the submitted_on_date of this GroupGeneralData.  # noqa: E501


        :return: The submitted_on_date of this GroupGeneralData.  # noqa: E501
        :rtype: date
        """
        return self._submitted_on_date

    @submitted_on_date.setter
    def submitted_on_date(self, submitted_on_date):
        """Sets the submitted_on_date of this GroupGeneralData.


        :param submitted_on_date: The submitted_on_date of this GroupGeneralData.  # noqa: E501
        :type: date
        """

        self._submitted_on_date = submitted_on_date

    @property
    def timeline(self):
        """Gets the timeline of this GroupGeneralData.  # noqa: E501


        :return: The timeline of this GroupGeneralData.  # noqa: E501
        :rtype: GroupTimelineData
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this GroupGeneralData.


        :param timeline: The timeline of this GroupGeneralData.  # noqa: E501
        :type: GroupTimelineData
        """

        self._timeline = timeline

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
        if issubclass(GroupGeneralData, dict):
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
        if not isinstance(other, GroupGeneralData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
