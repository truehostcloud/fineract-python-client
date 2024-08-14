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

class PostLoansRepaymentSchedulePeriods(object):
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
        'due_date': 'date',
        'fee_charges_due': 'int',
        'fee_charges_outstanding': 'int',
        'period': 'int',
        'principal_disbursed': 'int',
        'principal_loan_balance_outstanding': 'int',
        'total_actual_cost_of_loan_for_period': 'int',
        'total_due_for_period': 'int',
        'total_original_due_for_period': 'int',
        'total_outstanding_for_period': 'int',
        'total_overdue': 'int'
    }

    attribute_map = {
        'due_date': 'dueDate',
        'fee_charges_due': 'feeChargesDue',
        'fee_charges_outstanding': 'feeChargesOutstanding',
        'period': 'period',
        'principal_disbursed': 'principalDisbursed',
        'principal_loan_balance_outstanding': 'principalLoanBalanceOutstanding',
        'total_actual_cost_of_loan_for_period': 'totalActualCostOfLoanForPeriod',
        'total_due_for_period': 'totalDueForPeriod',
        'total_original_due_for_period': 'totalOriginalDueForPeriod',
        'total_outstanding_for_period': 'totalOutstandingForPeriod',
        'total_overdue': 'totalOverdue'
    }

    def __init__(self, due_date=None, fee_charges_due=None, fee_charges_outstanding=None, period=None, principal_disbursed=None, principal_loan_balance_outstanding=None, total_actual_cost_of_loan_for_period=None, total_due_for_period=None, total_original_due_for_period=None, total_outstanding_for_period=None, total_overdue=None):  # noqa: E501
        """PostLoansRepaymentSchedulePeriods - a model defined in Swagger"""  # noqa: E501
        self._due_date = None
        self._fee_charges_due = None
        self._fee_charges_outstanding = None
        self._period = None
        self._principal_disbursed = None
        self._principal_loan_balance_outstanding = None
        self._total_actual_cost_of_loan_for_period = None
        self._total_due_for_period = None
        self._total_original_due_for_period = None
        self._total_outstanding_for_period = None
        self._total_overdue = None
        self.discriminator = None
        if due_date is not None:
            self.due_date = due_date
        if fee_charges_due is not None:
            self.fee_charges_due = fee_charges_due
        if fee_charges_outstanding is not None:
            self.fee_charges_outstanding = fee_charges_outstanding
        if period is not None:
            self.period = period
        if principal_disbursed is not None:
            self.principal_disbursed = principal_disbursed
        if principal_loan_balance_outstanding is not None:
            self.principal_loan_balance_outstanding = principal_loan_balance_outstanding
        if total_actual_cost_of_loan_for_period is not None:
            self.total_actual_cost_of_loan_for_period = total_actual_cost_of_loan_for_period
        if total_due_for_period is not None:
            self.total_due_for_period = total_due_for_period
        if total_original_due_for_period is not None:
            self.total_original_due_for_period = total_original_due_for_period
        if total_outstanding_for_period is not None:
            self.total_outstanding_for_period = total_outstanding_for_period
        if total_overdue is not None:
            self.total_overdue = total_overdue

    @property
    def due_date(self):
        """Gets the due_date of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The due_date of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PostLoansRepaymentSchedulePeriods.


        :param due_date: The due_date of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def fee_charges_due(self):
        """Gets the fee_charges_due of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The fee_charges_due of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._fee_charges_due

    @fee_charges_due.setter
    def fee_charges_due(self, fee_charges_due):
        """Sets the fee_charges_due of this PostLoansRepaymentSchedulePeriods.


        :param fee_charges_due: The fee_charges_due of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._fee_charges_due = fee_charges_due

    @property
    def fee_charges_outstanding(self):
        """Gets the fee_charges_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The fee_charges_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._fee_charges_outstanding

    @fee_charges_outstanding.setter
    def fee_charges_outstanding(self, fee_charges_outstanding):
        """Sets the fee_charges_outstanding of this PostLoansRepaymentSchedulePeriods.


        :param fee_charges_outstanding: The fee_charges_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._fee_charges_outstanding = fee_charges_outstanding

    @property
    def period(self):
        """Gets the period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PostLoansRepaymentSchedulePeriods.


        :param period: The period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def principal_disbursed(self):
        """Gets the principal_disbursed of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The principal_disbursed of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._principal_disbursed

    @principal_disbursed.setter
    def principal_disbursed(self, principal_disbursed):
        """Sets the principal_disbursed of this PostLoansRepaymentSchedulePeriods.


        :param principal_disbursed: The principal_disbursed of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._principal_disbursed = principal_disbursed

    @property
    def principal_loan_balance_outstanding(self):
        """Gets the principal_loan_balance_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The principal_loan_balance_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._principal_loan_balance_outstanding

    @principal_loan_balance_outstanding.setter
    def principal_loan_balance_outstanding(self, principal_loan_balance_outstanding):
        """Sets the principal_loan_balance_outstanding of this PostLoansRepaymentSchedulePeriods.


        :param principal_loan_balance_outstanding: The principal_loan_balance_outstanding of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._principal_loan_balance_outstanding = principal_loan_balance_outstanding

    @property
    def total_actual_cost_of_loan_for_period(self):
        """Gets the total_actual_cost_of_loan_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The total_actual_cost_of_loan_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._total_actual_cost_of_loan_for_period

    @total_actual_cost_of_loan_for_period.setter
    def total_actual_cost_of_loan_for_period(self, total_actual_cost_of_loan_for_period):
        """Sets the total_actual_cost_of_loan_for_period of this PostLoansRepaymentSchedulePeriods.


        :param total_actual_cost_of_loan_for_period: The total_actual_cost_of_loan_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._total_actual_cost_of_loan_for_period = total_actual_cost_of_loan_for_period

    @property
    def total_due_for_period(self):
        """Gets the total_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The total_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._total_due_for_period

    @total_due_for_period.setter
    def total_due_for_period(self, total_due_for_period):
        """Sets the total_due_for_period of this PostLoansRepaymentSchedulePeriods.


        :param total_due_for_period: The total_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._total_due_for_period = total_due_for_period

    @property
    def total_original_due_for_period(self):
        """Gets the total_original_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The total_original_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._total_original_due_for_period

    @total_original_due_for_period.setter
    def total_original_due_for_period(self, total_original_due_for_period):
        """Sets the total_original_due_for_period of this PostLoansRepaymentSchedulePeriods.


        :param total_original_due_for_period: The total_original_due_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._total_original_due_for_period = total_original_due_for_period

    @property
    def total_outstanding_for_period(self):
        """Gets the total_outstanding_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The total_outstanding_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._total_outstanding_for_period

    @total_outstanding_for_period.setter
    def total_outstanding_for_period(self, total_outstanding_for_period):
        """Sets the total_outstanding_for_period of this PostLoansRepaymentSchedulePeriods.


        :param total_outstanding_for_period: The total_outstanding_for_period of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._total_outstanding_for_period = total_outstanding_for_period

    @property
    def total_overdue(self):
        """Gets the total_overdue of this PostLoansRepaymentSchedulePeriods.  # noqa: E501


        :return: The total_overdue of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :rtype: int
        """
        return self._total_overdue

    @total_overdue.setter
    def total_overdue(self, total_overdue):
        """Sets the total_overdue of this PostLoansRepaymentSchedulePeriods.


        :param total_overdue: The total_overdue of this PostLoansRepaymentSchedulePeriods.  # noqa: E501
        :type: int
        """

        self._total_overdue = total_overdue

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
        if issubclass(PostLoansRepaymentSchedulePeriods, dict):
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
        if not isinstance(other, PostLoansRepaymentSchedulePeriods):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
