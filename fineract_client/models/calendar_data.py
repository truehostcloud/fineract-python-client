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

class CalendarData(object):
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
        'calendar_instance_id': 'int',
        'calendar_type_options': 'list[EnumOptionData]',
        'center_id': 'str',
        'created_by_user_id': 'int',
        'created_by_username': 'str',
        'created_date': 'datetime',
        'date_format': 'str',
        'description': 'str',
        'duration': 'int',
        'end_date': 'date',
        'entity_id': 'int',
        'entity_type': 'EnumOptionData',
        'entity_type_options': 'list[EnumOptionData]',
        'first_reminder': 'int',
        'frequency': 'EnumOptionData',
        'frequency_nth_day_type_options': 'list[EnumOptionData]',
        'frequency_options': 'list[EnumOptionData]',
        'human_readable': 'str',
        'id': 'int',
        'interval': 'int',
        'last_updated_by_user_id': 'int',
        'last_updated_by_username': 'str',
        'last_updated_date': 'datetime',
        'locale': 'str',
        'location': 'str',
        'meeting_time': 'LocalTime',
        'next_ten_recurring_dates': 'list[date]',
        'recent_eligible_meeting_date': 'date',
        'recurrence': 'str',
        'recurring_dates': 'list[date]',
        'remind_by': 'EnumOptionData',
        'remind_by_options': 'list[EnumOptionData]',
        'repeating': 'bool',
        'repeats_on_day': 'EnumOptionData',
        'repeats_on_day_of_month': 'int',
        'repeats_on_day_options': 'list[EnumOptionData]',
        'repeats_on_nth_day_of_month': 'EnumOptionData',
        'row_index': 'int',
        'second_reminder': 'int',
        'start_date': 'date',
        'title': 'str',
        'type': 'EnumOptionData',
        'type_id': 'str'
    }

    attribute_map = {
        'calendar_instance_id': 'calendarInstanceId',
        'calendar_type_options': 'calendarTypeOptions',
        'center_id': 'centerId',
        'created_by_user_id': 'createdByUserId',
        'created_by_username': 'createdByUsername',
        'created_date': 'createdDate',
        'date_format': 'dateFormat',
        'description': 'description',
        'duration': 'duration',
        'end_date': 'endDate',
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'entity_type_options': 'entityTypeOptions',
        'first_reminder': 'firstReminder',
        'frequency': 'frequency',
        'frequency_nth_day_type_options': 'frequencyNthDayTypeOptions',
        'frequency_options': 'frequencyOptions',
        'human_readable': 'humanReadable',
        'id': 'id',
        'interval': 'interval',
        'last_updated_by_user_id': 'lastUpdatedByUserId',
        'last_updated_by_username': 'lastUpdatedByUsername',
        'last_updated_date': 'lastUpdatedDate',
        'locale': 'locale',
        'location': 'location',
        'meeting_time': 'meetingTime',
        'next_ten_recurring_dates': 'nextTenRecurringDates',
        'recent_eligible_meeting_date': 'recentEligibleMeetingDate',
        'recurrence': 'recurrence',
        'recurring_dates': 'recurringDates',
        'remind_by': 'remindBy',
        'remind_by_options': 'remindByOptions',
        'repeating': 'repeating',
        'repeats_on_day': 'repeatsOnDay',
        'repeats_on_day_of_month': 'repeatsOnDayOfMonth',
        'repeats_on_day_options': 'repeatsOnDayOptions',
        'repeats_on_nth_day_of_month': 'repeatsOnNthDayOfMonth',
        'row_index': 'rowIndex',
        'second_reminder': 'secondReminder',
        'start_date': 'startDate',
        'title': 'title',
        'type': 'type',
        'type_id': 'typeId'
    }

    def __init__(self, calendar_instance_id=None, calendar_type_options=None, center_id=None, created_by_user_id=None, created_by_username=None, created_date=None, date_format=None, description=None, duration=None, end_date=None, entity_id=None, entity_type=None, entity_type_options=None, first_reminder=None, frequency=None, frequency_nth_day_type_options=None, frequency_options=None, human_readable=None, id=None, interval=None, last_updated_by_user_id=None, last_updated_by_username=None, last_updated_date=None, locale=None, location=None, meeting_time=None, next_ten_recurring_dates=None, recent_eligible_meeting_date=None, recurrence=None, recurring_dates=None, remind_by=None, remind_by_options=None, repeating=None, repeats_on_day=None, repeats_on_day_of_month=None, repeats_on_day_options=None, repeats_on_nth_day_of_month=None, row_index=None, second_reminder=None, start_date=None, title=None, type=None, type_id=None):  # noqa: E501
        """CalendarData - a model defined in Swagger"""  # noqa: E501
        self._calendar_instance_id = None
        self._calendar_type_options = None
        self._center_id = None
        self._created_by_user_id = None
        self._created_by_username = None
        self._created_date = None
        self._date_format = None
        self._description = None
        self._duration = None
        self._end_date = None
        self._entity_id = None
        self._entity_type = None
        self._entity_type_options = None
        self._first_reminder = None
        self._frequency = None
        self._frequency_nth_day_type_options = None
        self._frequency_options = None
        self._human_readable = None
        self._id = None
        self._interval = None
        self._last_updated_by_user_id = None
        self._last_updated_by_username = None
        self._last_updated_date = None
        self._locale = None
        self._location = None
        self._meeting_time = None
        self._next_ten_recurring_dates = None
        self._recent_eligible_meeting_date = None
        self._recurrence = None
        self._recurring_dates = None
        self._remind_by = None
        self._remind_by_options = None
        self._repeating = None
        self._repeats_on_day = None
        self._repeats_on_day_of_month = None
        self._repeats_on_day_options = None
        self._repeats_on_nth_day_of_month = None
        self._row_index = None
        self._second_reminder = None
        self._start_date = None
        self._title = None
        self._type = None
        self._type_id = None
        self.discriminator = None
        if calendar_instance_id is not None:
            self.calendar_instance_id = calendar_instance_id
        if calendar_type_options is not None:
            self.calendar_type_options = calendar_type_options
        if center_id is not None:
            self.center_id = center_id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if created_by_username is not None:
            self.created_by_username = created_by_username
        if created_date is not None:
            self.created_date = created_date
        if date_format is not None:
            self.date_format = date_format
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if end_date is not None:
            self.end_date = end_date
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        if entity_type_options is not None:
            self.entity_type_options = entity_type_options
        if first_reminder is not None:
            self.first_reminder = first_reminder
        if frequency is not None:
            self.frequency = frequency
        if frequency_nth_day_type_options is not None:
            self.frequency_nth_day_type_options = frequency_nth_day_type_options
        if frequency_options is not None:
            self.frequency_options = frequency_options
        if human_readable is not None:
            self.human_readable = human_readable
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if last_updated_by_user_id is not None:
            self.last_updated_by_user_id = last_updated_by_user_id
        if last_updated_by_username is not None:
            self.last_updated_by_username = last_updated_by_username
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if locale is not None:
            self.locale = locale
        if location is not None:
            self.location = location
        if meeting_time is not None:
            self.meeting_time = meeting_time
        if next_ten_recurring_dates is not None:
            self.next_ten_recurring_dates = next_ten_recurring_dates
        if recent_eligible_meeting_date is not None:
            self.recent_eligible_meeting_date = recent_eligible_meeting_date
        if recurrence is not None:
            self.recurrence = recurrence
        if recurring_dates is not None:
            self.recurring_dates = recurring_dates
        if remind_by is not None:
            self.remind_by = remind_by
        if remind_by_options is not None:
            self.remind_by_options = remind_by_options
        if repeating is not None:
            self.repeating = repeating
        if repeats_on_day is not None:
            self.repeats_on_day = repeats_on_day
        if repeats_on_day_of_month is not None:
            self.repeats_on_day_of_month = repeats_on_day_of_month
        if repeats_on_day_options is not None:
            self.repeats_on_day_options = repeats_on_day_options
        if repeats_on_nth_day_of_month is not None:
            self.repeats_on_nth_day_of_month = repeats_on_nth_day_of_month
        if row_index is not None:
            self.row_index = row_index
        if second_reminder is not None:
            self.second_reminder = second_reminder
        if start_date is not None:
            self.start_date = start_date
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if type_id is not None:
            self.type_id = type_id

    @property
    def calendar_instance_id(self):
        """Gets the calendar_instance_id of this CalendarData.  # noqa: E501


        :return: The calendar_instance_id of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._calendar_instance_id

    @calendar_instance_id.setter
    def calendar_instance_id(self, calendar_instance_id):
        """Sets the calendar_instance_id of this CalendarData.


        :param calendar_instance_id: The calendar_instance_id of this CalendarData.  # noqa: E501
        :type: int
        """

        self._calendar_instance_id = calendar_instance_id

    @property
    def calendar_type_options(self):
        """Gets the calendar_type_options of this CalendarData.  # noqa: E501


        :return: The calendar_type_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._calendar_type_options

    @calendar_type_options.setter
    def calendar_type_options(self, calendar_type_options):
        """Sets the calendar_type_options of this CalendarData.


        :param calendar_type_options: The calendar_type_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._calendar_type_options = calendar_type_options

    @property
    def center_id(self):
        """Gets the center_id of this CalendarData.  # noqa: E501


        :return: The center_id of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._center_id

    @center_id.setter
    def center_id(self, center_id):
        """Sets the center_id of this CalendarData.


        :param center_id: The center_id of this CalendarData.  # noqa: E501
        :type: str
        """

        self._center_id = center_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this CalendarData.  # noqa: E501


        :return: The created_by_user_id of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this CalendarData.


        :param created_by_user_id: The created_by_user_id of this CalendarData.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def created_by_username(self):
        """Gets the created_by_username of this CalendarData.  # noqa: E501


        :return: The created_by_username of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._created_by_username

    @created_by_username.setter
    def created_by_username(self, created_by_username):
        """Sets the created_by_username of this CalendarData.


        :param created_by_username: The created_by_username of this CalendarData.  # noqa: E501
        :type: str
        """

        self._created_by_username = created_by_username

    @property
    def created_date(self):
        """Gets the created_date of this CalendarData.  # noqa: E501


        :return: The created_date of this CalendarData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CalendarData.


        :param created_date: The created_date of this CalendarData.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def date_format(self):
        """Gets the date_format of this CalendarData.  # noqa: E501


        :return: The date_format of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this CalendarData.


        :param date_format: The date_format of this CalendarData.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def description(self):
        """Gets the description of this CalendarData.  # noqa: E501


        :return: The description of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CalendarData.


        :param description: The description of this CalendarData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this CalendarData.  # noqa: E501


        :return: The duration of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CalendarData.


        :param duration: The duration of this CalendarData.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def end_date(self):
        """Gets the end_date of this CalendarData.  # noqa: E501


        :return: The end_date of this CalendarData.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CalendarData.


        :param end_date: The end_date of this CalendarData.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def entity_id(self):
        """Gets the entity_id of this CalendarData.  # noqa: E501


        :return: The entity_id of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this CalendarData.


        :param entity_id: The entity_id of this CalendarData.  # noqa: E501
        :type: int
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this CalendarData.  # noqa: E501


        :return: The entity_type of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this CalendarData.


        :param entity_type: The entity_type of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._entity_type = entity_type

    @property
    def entity_type_options(self):
        """Gets the entity_type_options of this CalendarData.  # noqa: E501


        :return: The entity_type_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._entity_type_options

    @entity_type_options.setter
    def entity_type_options(self, entity_type_options):
        """Sets the entity_type_options of this CalendarData.


        :param entity_type_options: The entity_type_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._entity_type_options = entity_type_options

    @property
    def first_reminder(self):
        """Gets the first_reminder of this CalendarData.  # noqa: E501


        :return: The first_reminder of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._first_reminder

    @first_reminder.setter
    def first_reminder(self, first_reminder):
        """Sets the first_reminder of this CalendarData.


        :param first_reminder: The first_reminder of this CalendarData.  # noqa: E501
        :type: int
        """

        self._first_reminder = first_reminder

    @property
    def frequency(self):
        """Gets the frequency of this CalendarData.  # noqa: E501


        :return: The frequency of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this CalendarData.


        :param frequency: The frequency of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._frequency = frequency

    @property
    def frequency_nth_day_type_options(self):
        """Gets the frequency_nth_day_type_options of this CalendarData.  # noqa: E501


        :return: The frequency_nth_day_type_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._frequency_nth_day_type_options

    @frequency_nth_day_type_options.setter
    def frequency_nth_day_type_options(self, frequency_nth_day_type_options):
        """Sets the frequency_nth_day_type_options of this CalendarData.


        :param frequency_nth_day_type_options: The frequency_nth_day_type_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._frequency_nth_day_type_options = frequency_nth_day_type_options

    @property
    def frequency_options(self):
        """Gets the frequency_options of this CalendarData.  # noqa: E501


        :return: The frequency_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._frequency_options

    @frequency_options.setter
    def frequency_options(self, frequency_options):
        """Sets the frequency_options of this CalendarData.


        :param frequency_options: The frequency_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._frequency_options = frequency_options

    @property
    def human_readable(self):
        """Gets the human_readable of this CalendarData.  # noqa: E501


        :return: The human_readable of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._human_readable

    @human_readable.setter
    def human_readable(self, human_readable):
        """Sets the human_readable of this CalendarData.


        :param human_readable: The human_readable of this CalendarData.  # noqa: E501
        :type: str
        """

        self._human_readable = human_readable

    @property
    def id(self):
        """Gets the id of this CalendarData.  # noqa: E501


        :return: The id of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CalendarData.


        :param id: The id of this CalendarData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this CalendarData.  # noqa: E501


        :return: The interval of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CalendarData.


        :param interval: The interval of this CalendarData.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def last_updated_by_user_id(self):
        """Gets the last_updated_by_user_id of this CalendarData.  # noqa: E501


        :return: The last_updated_by_user_id of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_by_user_id

    @last_updated_by_user_id.setter
    def last_updated_by_user_id(self, last_updated_by_user_id):
        """Sets the last_updated_by_user_id of this CalendarData.


        :param last_updated_by_user_id: The last_updated_by_user_id of this CalendarData.  # noqa: E501
        :type: int
        """

        self._last_updated_by_user_id = last_updated_by_user_id

    @property
    def last_updated_by_username(self):
        """Gets the last_updated_by_username of this CalendarData.  # noqa: E501


        :return: The last_updated_by_username of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by_username

    @last_updated_by_username.setter
    def last_updated_by_username(self, last_updated_by_username):
        """Sets the last_updated_by_username of this CalendarData.


        :param last_updated_by_username: The last_updated_by_username of this CalendarData.  # noqa: E501
        :type: str
        """

        self._last_updated_by_username = last_updated_by_username

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this CalendarData.  # noqa: E501


        :return: The last_updated_date of this CalendarData.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this CalendarData.


        :param last_updated_date: The last_updated_date of this CalendarData.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def locale(self):
        """Gets the locale of this CalendarData.  # noqa: E501


        :return: The locale of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CalendarData.


        :param locale: The locale of this CalendarData.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def location(self):
        """Gets the location of this CalendarData.  # noqa: E501


        :return: The location of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CalendarData.


        :param location: The location of this CalendarData.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def meeting_time(self):
        """Gets the meeting_time of this CalendarData.  # noqa: E501


        :return: The meeting_time of this CalendarData.  # noqa: E501
        :rtype: LocalTime
        """
        return self._meeting_time

    @meeting_time.setter
    def meeting_time(self, meeting_time):
        """Sets the meeting_time of this CalendarData.


        :param meeting_time: The meeting_time of this CalendarData.  # noqa: E501
        :type: LocalTime
        """

        self._meeting_time = meeting_time

    @property
    def next_ten_recurring_dates(self):
        """Gets the next_ten_recurring_dates of this CalendarData.  # noqa: E501


        :return: The next_ten_recurring_dates of this CalendarData.  # noqa: E501
        :rtype: list[date]
        """
        return self._next_ten_recurring_dates

    @next_ten_recurring_dates.setter
    def next_ten_recurring_dates(self, next_ten_recurring_dates):
        """Sets the next_ten_recurring_dates of this CalendarData.


        :param next_ten_recurring_dates: The next_ten_recurring_dates of this CalendarData.  # noqa: E501
        :type: list[date]
        """

        self._next_ten_recurring_dates = next_ten_recurring_dates

    @property
    def recent_eligible_meeting_date(self):
        """Gets the recent_eligible_meeting_date of this CalendarData.  # noqa: E501


        :return: The recent_eligible_meeting_date of this CalendarData.  # noqa: E501
        :rtype: date
        """
        return self._recent_eligible_meeting_date

    @recent_eligible_meeting_date.setter
    def recent_eligible_meeting_date(self, recent_eligible_meeting_date):
        """Sets the recent_eligible_meeting_date of this CalendarData.


        :param recent_eligible_meeting_date: The recent_eligible_meeting_date of this CalendarData.  # noqa: E501
        :type: date
        """

        self._recent_eligible_meeting_date = recent_eligible_meeting_date

    @property
    def recurrence(self):
        """Gets the recurrence of this CalendarData.  # noqa: E501


        :return: The recurrence of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this CalendarData.


        :param recurrence: The recurrence of this CalendarData.  # noqa: E501
        :type: str
        """

        self._recurrence = recurrence

    @property
    def recurring_dates(self):
        """Gets the recurring_dates of this CalendarData.  # noqa: E501


        :return: The recurring_dates of this CalendarData.  # noqa: E501
        :rtype: list[date]
        """
        return self._recurring_dates

    @recurring_dates.setter
    def recurring_dates(self, recurring_dates):
        """Sets the recurring_dates of this CalendarData.


        :param recurring_dates: The recurring_dates of this CalendarData.  # noqa: E501
        :type: list[date]
        """

        self._recurring_dates = recurring_dates

    @property
    def remind_by(self):
        """Gets the remind_by of this CalendarData.  # noqa: E501


        :return: The remind_by of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._remind_by

    @remind_by.setter
    def remind_by(self, remind_by):
        """Sets the remind_by of this CalendarData.


        :param remind_by: The remind_by of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._remind_by = remind_by

    @property
    def remind_by_options(self):
        """Gets the remind_by_options of this CalendarData.  # noqa: E501


        :return: The remind_by_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._remind_by_options

    @remind_by_options.setter
    def remind_by_options(self, remind_by_options):
        """Sets the remind_by_options of this CalendarData.


        :param remind_by_options: The remind_by_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._remind_by_options = remind_by_options

    @property
    def repeating(self):
        """Gets the repeating of this CalendarData.  # noqa: E501


        :return: The repeating of this CalendarData.  # noqa: E501
        :rtype: bool
        """
        return self._repeating

    @repeating.setter
    def repeating(self, repeating):
        """Sets the repeating of this CalendarData.


        :param repeating: The repeating of this CalendarData.  # noqa: E501
        :type: bool
        """

        self._repeating = repeating

    @property
    def repeats_on_day(self):
        """Gets the repeats_on_day of this CalendarData.  # noqa: E501


        :return: The repeats_on_day of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._repeats_on_day

    @repeats_on_day.setter
    def repeats_on_day(self, repeats_on_day):
        """Sets the repeats_on_day of this CalendarData.


        :param repeats_on_day: The repeats_on_day of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._repeats_on_day = repeats_on_day

    @property
    def repeats_on_day_of_month(self):
        """Gets the repeats_on_day_of_month of this CalendarData.  # noqa: E501


        :return: The repeats_on_day_of_month of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._repeats_on_day_of_month

    @repeats_on_day_of_month.setter
    def repeats_on_day_of_month(self, repeats_on_day_of_month):
        """Sets the repeats_on_day_of_month of this CalendarData.


        :param repeats_on_day_of_month: The repeats_on_day_of_month of this CalendarData.  # noqa: E501
        :type: int
        """

        self._repeats_on_day_of_month = repeats_on_day_of_month

    @property
    def repeats_on_day_options(self):
        """Gets the repeats_on_day_options of this CalendarData.  # noqa: E501


        :return: The repeats_on_day_options of this CalendarData.  # noqa: E501
        :rtype: list[EnumOptionData]
        """
        return self._repeats_on_day_options

    @repeats_on_day_options.setter
    def repeats_on_day_options(self, repeats_on_day_options):
        """Sets the repeats_on_day_options of this CalendarData.


        :param repeats_on_day_options: The repeats_on_day_options of this CalendarData.  # noqa: E501
        :type: list[EnumOptionData]
        """

        self._repeats_on_day_options = repeats_on_day_options

    @property
    def repeats_on_nth_day_of_month(self):
        """Gets the repeats_on_nth_day_of_month of this CalendarData.  # noqa: E501


        :return: The repeats_on_nth_day_of_month of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._repeats_on_nth_day_of_month

    @repeats_on_nth_day_of_month.setter
    def repeats_on_nth_day_of_month(self, repeats_on_nth_day_of_month):
        """Sets the repeats_on_nth_day_of_month of this CalendarData.


        :param repeats_on_nth_day_of_month: The repeats_on_nth_day_of_month of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._repeats_on_nth_day_of_month = repeats_on_nth_day_of_month

    @property
    def row_index(self):
        """Gets the row_index of this CalendarData.  # noqa: E501


        :return: The row_index of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this CalendarData.


        :param row_index: The row_index of this CalendarData.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def second_reminder(self):
        """Gets the second_reminder of this CalendarData.  # noqa: E501


        :return: The second_reminder of this CalendarData.  # noqa: E501
        :rtype: int
        """
        return self._second_reminder

    @second_reminder.setter
    def second_reminder(self, second_reminder):
        """Sets the second_reminder of this CalendarData.


        :param second_reminder: The second_reminder of this CalendarData.  # noqa: E501
        :type: int
        """

        self._second_reminder = second_reminder

    @property
    def start_date(self):
        """Gets the start_date of this CalendarData.  # noqa: E501


        :return: The start_date of this CalendarData.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CalendarData.


        :param start_date: The start_date of this CalendarData.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def title(self):
        """Gets the title of this CalendarData.  # noqa: E501


        :return: The title of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CalendarData.


        :param title: The title of this CalendarData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this CalendarData.  # noqa: E501


        :return: The type of this CalendarData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CalendarData.


        :param type: The type of this CalendarData.  # noqa: E501
        :type: EnumOptionData
        """

        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this CalendarData.  # noqa: E501


        :return: The type_id of this CalendarData.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this CalendarData.


        :param type_id: The type_id of this CalendarData.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

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
        if issubclass(CalendarData, dict):
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
        if not isinstance(other, CalendarData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
