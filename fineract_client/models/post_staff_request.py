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

class PostStaffRequest(object):
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
        'external_id': 'str',
        'firstname': 'str',
        'is_active': 'bool',
        'is_loan_officer': 'bool',
        'joining_date': 'date',
        'lastname': 'str',
        'locale': 'str',
        'mobile_no': 'str',
        'office_id': 'int'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'external_id': 'externalId',
        'firstname': 'firstname',
        'is_active': 'isActive',
        'is_loan_officer': 'isLoanOfficer',
        'joining_date': 'joiningDate',
        'lastname': 'lastname',
        'locale': 'locale',
        'mobile_no': 'mobileNo',
        'office_id': 'officeId'
    }

    def __init__(self, date_format=None, external_id=None, firstname=None, is_active=None, is_loan_officer=None, joining_date=None, lastname=None, locale=None, mobile_no=None, office_id=None):  # noqa: E501
        """PostStaffRequest - a model defined in Swagger"""  # noqa: E501
        self._date_format = None
        self._external_id = None
        self._firstname = None
        self._is_active = None
        self._is_loan_officer = None
        self._joining_date = None
        self._lastname = None
        self._locale = None
        self._mobile_no = None
        self._office_id = None
        self.discriminator = None
        if date_format is not None:
            self.date_format = date_format
        if external_id is not None:
            self.external_id = external_id
        if firstname is not None:
            self.firstname = firstname
        if is_active is not None:
            self.is_active = is_active
        if is_loan_officer is not None:
            self.is_loan_officer = is_loan_officer
        if joining_date is not None:
            self.joining_date = joining_date
        if lastname is not None:
            self.lastname = lastname
        if locale is not None:
            self.locale = locale
        if mobile_no is not None:
            self.mobile_no = mobile_no
        if office_id is not None:
            self.office_id = office_id

    @property
    def date_format(self):
        """Gets the date_format of this PostStaffRequest.  # noqa: E501


        :return: The date_format of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this PostStaffRequest.


        :param date_format: The date_format of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._date_format = date_format

    @property
    def external_id(self):
        """Gets the external_id of this PostStaffRequest.  # noqa: E501


        :return: The external_id of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PostStaffRequest.


        :param external_id: The external_id of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def firstname(self):
        """Gets the firstname of this PostStaffRequest.  # noqa: E501


        :return: The firstname of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this PostStaffRequest.


        :param firstname: The firstname of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def is_active(self):
        """Gets the is_active of this PostStaffRequest.  # noqa: E501


        :return: The is_active of this PostStaffRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this PostStaffRequest.


        :param is_active: The is_active of this PostStaffRequest.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_loan_officer(self):
        """Gets the is_loan_officer of this PostStaffRequest.  # noqa: E501


        :return: The is_loan_officer of this PostStaffRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_loan_officer

    @is_loan_officer.setter
    def is_loan_officer(self, is_loan_officer):
        """Sets the is_loan_officer of this PostStaffRequest.


        :param is_loan_officer: The is_loan_officer of this PostStaffRequest.  # noqa: E501
        :type: bool
        """

        self._is_loan_officer = is_loan_officer

    @property
    def joining_date(self):
        """Gets the joining_date of this PostStaffRequest.  # noqa: E501


        :return: The joining_date of this PostStaffRequest.  # noqa: E501
        :rtype: date
        """
        return self._joining_date

    @joining_date.setter
    def joining_date(self, joining_date):
        """Sets the joining_date of this PostStaffRequest.


        :param joining_date: The joining_date of this PostStaffRequest.  # noqa: E501
        :type: date
        """

        self._joining_date = joining_date

    @property
    def lastname(self):
        """Gets the lastname of this PostStaffRequest.  # noqa: E501


        :return: The lastname of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PostStaffRequest.


        :param lastname: The lastname of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def locale(self):
        """Gets the locale of this PostStaffRequest.  # noqa: E501


        :return: The locale of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PostStaffRequest.


        :param locale: The locale of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def mobile_no(self):
        """Gets the mobile_no of this PostStaffRequest.  # noqa: E501


        :return: The mobile_no of this PostStaffRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        """Sets the mobile_no of this PostStaffRequest.


        :param mobile_no: The mobile_no of this PostStaffRequest.  # noqa: E501
        :type: str
        """

        self._mobile_no = mobile_no

    @property
    def office_id(self):
        """Gets the office_id of this PostStaffRequest.  # noqa: E501


        :return: The office_id of this PostStaffRequest.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this PostStaffRequest.


        :param office_id: The office_id of this PostStaffRequest.  # noqa: E501
        :type: int
        """

        self._office_id = office_id

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
        if issubclass(PostStaffRequest, dict):
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
        if not isinstance(other, PostStaffRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
