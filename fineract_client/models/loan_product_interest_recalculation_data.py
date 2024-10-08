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

class LoanProductInterestRecalculationData(object):
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
        'allow_compounding_on_eod': 'bool',
        'arrears_based_on_original_schedule': 'bool',
        'compounding_to_be_posted_as_transaction': 'bool',
        'id': 'int',
        'interest_recalculation_compounding_type': 'EnumOptionData',
        'is_arrears_based_on_original_schedule': 'bool',
        'is_compounding_to_be_posted_as_transaction': 'bool',
        'pre_closure_interest_calculation_strategy': 'EnumOptionData',
        'product_id': 'int',
        'recalculation_compounding_frequency_interval': 'int',
        'recalculation_compounding_frequency_nth_day': 'EnumOptionData',
        'recalculation_compounding_frequency_on_day': 'int',
        'recalculation_compounding_frequency_type': 'EnumOptionData',
        'recalculation_compounding_frequency_weekday': 'EnumOptionData',
        'recalculation_rest_frequency_interval': 'int',
        'recalculation_rest_frequency_nth_day': 'EnumOptionData',
        'recalculation_rest_frequency_on_day': 'int',
        'recalculation_rest_frequency_type': 'EnumOptionData',
        'recalculation_rest_frequency_weekday': 'EnumOptionData',
        'reschedule_strategy_type': 'EnumOptionData'
    }

    attribute_map = {
        'allow_compounding_on_eod': 'allowCompoundingOnEod',
        'arrears_based_on_original_schedule': 'arrearsBasedOnOriginalSchedule',
        'compounding_to_be_posted_as_transaction': 'compoundingToBePostedAsTransaction',
        'id': 'id',
        'interest_recalculation_compounding_type': 'interestRecalculationCompoundingType',
        'is_arrears_based_on_original_schedule': 'isArrearsBasedOnOriginalSchedule',
        'is_compounding_to_be_posted_as_transaction': 'isCompoundingToBePostedAsTransaction',
        'pre_closure_interest_calculation_strategy': 'preClosureInterestCalculationStrategy',
        'product_id': 'productId',
        'recalculation_compounding_frequency_interval': 'recalculationCompoundingFrequencyInterval',
        'recalculation_compounding_frequency_nth_day': 'recalculationCompoundingFrequencyNthDay',
        'recalculation_compounding_frequency_on_day': 'recalculationCompoundingFrequencyOnDay',
        'recalculation_compounding_frequency_type': 'recalculationCompoundingFrequencyType',
        'recalculation_compounding_frequency_weekday': 'recalculationCompoundingFrequencyWeekday',
        'recalculation_rest_frequency_interval': 'recalculationRestFrequencyInterval',
        'recalculation_rest_frequency_nth_day': 'recalculationRestFrequencyNthDay',
        'recalculation_rest_frequency_on_day': 'recalculationRestFrequencyOnDay',
        'recalculation_rest_frequency_type': 'recalculationRestFrequencyType',
        'recalculation_rest_frequency_weekday': 'recalculationRestFrequencyWeekday',
        'reschedule_strategy_type': 'rescheduleStrategyType'
    }

    def __init__(self, allow_compounding_on_eod=None, arrears_based_on_original_schedule=None, compounding_to_be_posted_as_transaction=None, id=None, interest_recalculation_compounding_type=None, is_arrears_based_on_original_schedule=None, is_compounding_to_be_posted_as_transaction=None, pre_closure_interest_calculation_strategy=None, product_id=None, recalculation_compounding_frequency_interval=None, recalculation_compounding_frequency_nth_day=None, recalculation_compounding_frequency_on_day=None, recalculation_compounding_frequency_type=None, recalculation_compounding_frequency_weekday=None, recalculation_rest_frequency_interval=None, recalculation_rest_frequency_nth_day=None, recalculation_rest_frequency_on_day=None, recalculation_rest_frequency_type=None, recalculation_rest_frequency_weekday=None, reschedule_strategy_type=None):  # noqa: E501
        """LoanProductInterestRecalculationData - a model defined in Swagger"""  # noqa: E501
        self._allow_compounding_on_eod = None
        self._arrears_based_on_original_schedule = None
        self._compounding_to_be_posted_as_transaction = None
        self._id = None
        self._interest_recalculation_compounding_type = None
        self._is_arrears_based_on_original_schedule = None
        self._is_compounding_to_be_posted_as_transaction = None
        self._pre_closure_interest_calculation_strategy = None
        self._product_id = None
        self._recalculation_compounding_frequency_interval = None
        self._recalculation_compounding_frequency_nth_day = None
        self._recalculation_compounding_frequency_on_day = None
        self._recalculation_compounding_frequency_type = None
        self._recalculation_compounding_frequency_weekday = None
        self._recalculation_rest_frequency_interval = None
        self._recalculation_rest_frequency_nth_day = None
        self._recalculation_rest_frequency_on_day = None
        self._recalculation_rest_frequency_type = None
        self._recalculation_rest_frequency_weekday = None
        self._reschedule_strategy_type = None
        self.discriminator = None
        if allow_compounding_on_eod is not None:
            self.allow_compounding_on_eod = allow_compounding_on_eod
        if arrears_based_on_original_schedule is not None:
            self.arrears_based_on_original_schedule = arrears_based_on_original_schedule
        if compounding_to_be_posted_as_transaction is not None:
            self.compounding_to_be_posted_as_transaction = compounding_to_be_posted_as_transaction
        if id is not None:
            self.id = id
        if interest_recalculation_compounding_type is not None:
            self.interest_recalculation_compounding_type = interest_recalculation_compounding_type
        if is_arrears_based_on_original_schedule is not None:
            self.is_arrears_based_on_original_schedule = is_arrears_based_on_original_schedule
        if is_compounding_to_be_posted_as_transaction is not None:
            self.is_compounding_to_be_posted_as_transaction = is_compounding_to_be_posted_as_transaction
        if pre_closure_interest_calculation_strategy is not None:
            self.pre_closure_interest_calculation_strategy = pre_closure_interest_calculation_strategy
        if product_id is not None:
            self.product_id = product_id
        if recalculation_compounding_frequency_interval is not None:
            self.recalculation_compounding_frequency_interval = recalculation_compounding_frequency_interval
        if recalculation_compounding_frequency_nth_day is not None:
            self.recalculation_compounding_frequency_nth_day = recalculation_compounding_frequency_nth_day
        if recalculation_compounding_frequency_on_day is not None:
            self.recalculation_compounding_frequency_on_day = recalculation_compounding_frequency_on_day
        if recalculation_compounding_frequency_type is not None:
            self.recalculation_compounding_frequency_type = recalculation_compounding_frequency_type
        if recalculation_compounding_frequency_weekday is not None:
            self.recalculation_compounding_frequency_weekday = recalculation_compounding_frequency_weekday
        if recalculation_rest_frequency_interval is not None:
            self.recalculation_rest_frequency_interval = recalculation_rest_frequency_interval
        if recalculation_rest_frequency_nth_day is not None:
            self.recalculation_rest_frequency_nth_day = recalculation_rest_frequency_nth_day
        if recalculation_rest_frequency_on_day is not None:
            self.recalculation_rest_frequency_on_day = recalculation_rest_frequency_on_day
        if recalculation_rest_frequency_type is not None:
            self.recalculation_rest_frequency_type = recalculation_rest_frequency_type
        if recalculation_rest_frequency_weekday is not None:
            self.recalculation_rest_frequency_weekday = recalculation_rest_frequency_weekday
        if reschedule_strategy_type is not None:
            self.reschedule_strategy_type = reschedule_strategy_type

    @property
    def allow_compounding_on_eod(self):
        """Gets the allow_compounding_on_eod of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The allow_compounding_on_eod of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_compounding_on_eod

    @allow_compounding_on_eod.setter
    def allow_compounding_on_eod(self, allow_compounding_on_eod):
        """Sets the allow_compounding_on_eod of this LoanProductInterestRecalculationData.


        :param allow_compounding_on_eod: The allow_compounding_on_eod of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: bool
        """

        self._allow_compounding_on_eod = allow_compounding_on_eod

    @property
    def arrears_based_on_original_schedule(self):
        """Gets the arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: bool
        """
        return self._arrears_based_on_original_schedule

    @arrears_based_on_original_schedule.setter
    def arrears_based_on_original_schedule(self, arrears_based_on_original_schedule):
        """Sets the arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.


        :param arrears_based_on_original_schedule: The arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: bool
        """

        self._arrears_based_on_original_schedule = arrears_based_on_original_schedule

    @property
    def compounding_to_be_posted_as_transaction(self):
        """Gets the compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: bool
        """
        return self._compounding_to_be_posted_as_transaction

    @compounding_to_be_posted_as_transaction.setter
    def compounding_to_be_posted_as_transaction(self, compounding_to_be_posted_as_transaction):
        """Sets the compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.


        :param compounding_to_be_posted_as_transaction: The compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: bool
        """

        self._compounding_to_be_posted_as_transaction = compounding_to_be_posted_as_transaction

    @property
    def id(self):
        """Gets the id of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The id of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoanProductInterestRecalculationData.


        :param id: The id of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_recalculation_compounding_type(self):
        """Gets the interest_recalculation_compounding_type of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The interest_recalculation_compounding_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._interest_recalculation_compounding_type

    @interest_recalculation_compounding_type.setter
    def interest_recalculation_compounding_type(self, interest_recalculation_compounding_type):
        """Sets the interest_recalculation_compounding_type of this LoanProductInterestRecalculationData.


        :param interest_recalculation_compounding_type: The interest_recalculation_compounding_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._interest_recalculation_compounding_type = interest_recalculation_compounding_type

    @property
    def is_arrears_based_on_original_schedule(self):
        """Gets the is_arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The is_arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: bool
        """
        return self._is_arrears_based_on_original_schedule

    @is_arrears_based_on_original_schedule.setter
    def is_arrears_based_on_original_schedule(self, is_arrears_based_on_original_schedule):
        """Sets the is_arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.


        :param is_arrears_based_on_original_schedule: The is_arrears_based_on_original_schedule of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: bool
        """

        self._is_arrears_based_on_original_schedule = is_arrears_based_on_original_schedule

    @property
    def is_compounding_to_be_posted_as_transaction(self):
        """Gets the is_compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The is_compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: bool
        """
        return self._is_compounding_to_be_posted_as_transaction

    @is_compounding_to_be_posted_as_transaction.setter
    def is_compounding_to_be_posted_as_transaction(self, is_compounding_to_be_posted_as_transaction):
        """Sets the is_compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.


        :param is_compounding_to_be_posted_as_transaction: The is_compounding_to_be_posted_as_transaction of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: bool
        """

        self._is_compounding_to_be_posted_as_transaction = is_compounding_to_be_posted_as_transaction

    @property
    def pre_closure_interest_calculation_strategy(self):
        """Gets the pre_closure_interest_calculation_strategy of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The pre_closure_interest_calculation_strategy of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._pre_closure_interest_calculation_strategy

    @pre_closure_interest_calculation_strategy.setter
    def pre_closure_interest_calculation_strategy(self, pre_closure_interest_calculation_strategy):
        """Sets the pre_closure_interest_calculation_strategy of this LoanProductInterestRecalculationData.


        :param pre_closure_interest_calculation_strategy: The pre_closure_interest_calculation_strategy of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._pre_closure_interest_calculation_strategy = pre_closure_interest_calculation_strategy

    @property
    def product_id(self):
        """Gets the product_id of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The product_id of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this LoanProductInterestRecalculationData.


        :param product_id: The product_id of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def recalculation_compounding_frequency_interval(self):
        """Gets the recalculation_compounding_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_compounding_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._recalculation_compounding_frequency_interval

    @recalculation_compounding_frequency_interval.setter
    def recalculation_compounding_frequency_interval(self, recalculation_compounding_frequency_interval):
        """Sets the recalculation_compounding_frequency_interval of this LoanProductInterestRecalculationData.


        :param recalculation_compounding_frequency_interval: The recalculation_compounding_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._recalculation_compounding_frequency_interval = recalculation_compounding_frequency_interval

    @property
    def recalculation_compounding_frequency_nth_day(self):
        """Gets the recalculation_compounding_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_compounding_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_compounding_frequency_nth_day

    @recalculation_compounding_frequency_nth_day.setter
    def recalculation_compounding_frequency_nth_day(self, recalculation_compounding_frequency_nth_day):
        """Sets the recalculation_compounding_frequency_nth_day of this LoanProductInterestRecalculationData.


        :param recalculation_compounding_frequency_nth_day: The recalculation_compounding_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_compounding_frequency_nth_day = recalculation_compounding_frequency_nth_day

    @property
    def recalculation_compounding_frequency_on_day(self):
        """Gets the recalculation_compounding_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_compounding_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._recalculation_compounding_frequency_on_day

    @recalculation_compounding_frequency_on_day.setter
    def recalculation_compounding_frequency_on_day(self, recalculation_compounding_frequency_on_day):
        """Sets the recalculation_compounding_frequency_on_day of this LoanProductInterestRecalculationData.


        :param recalculation_compounding_frequency_on_day: The recalculation_compounding_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._recalculation_compounding_frequency_on_day = recalculation_compounding_frequency_on_day

    @property
    def recalculation_compounding_frequency_type(self):
        """Gets the recalculation_compounding_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_compounding_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_compounding_frequency_type

    @recalculation_compounding_frequency_type.setter
    def recalculation_compounding_frequency_type(self, recalculation_compounding_frequency_type):
        """Sets the recalculation_compounding_frequency_type of this LoanProductInterestRecalculationData.


        :param recalculation_compounding_frequency_type: The recalculation_compounding_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_compounding_frequency_type = recalculation_compounding_frequency_type

    @property
    def recalculation_compounding_frequency_weekday(self):
        """Gets the recalculation_compounding_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_compounding_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_compounding_frequency_weekday

    @recalculation_compounding_frequency_weekday.setter
    def recalculation_compounding_frequency_weekday(self, recalculation_compounding_frequency_weekday):
        """Sets the recalculation_compounding_frequency_weekday of this LoanProductInterestRecalculationData.


        :param recalculation_compounding_frequency_weekday: The recalculation_compounding_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_compounding_frequency_weekday = recalculation_compounding_frequency_weekday

    @property
    def recalculation_rest_frequency_interval(self):
        """Gets the recalculation_rest_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_rest_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._recalculation_rest_frequency_interval

    @recalculation_rest_frequency_interval.setter
    def recalculation_rest_frequency_interval(self, recalculation_rest_frequency_interval):
        """Sets the recalculation_rest_frequency_interval of this LoanProductInterestRecalculationData.


        :param recalculation_rest_frequency_interval: The recalculation_rest_frequency_interval of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._recalculation_rest_frequency_interval = recalculation_rest_frequency_interval

    @property
    def recalculation_rest_frequency_nth_day(self):
        """Gets the recalculation_rest_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_rest_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_rest_frequency_nth_day

    @recalculation_rest_frequency_nth_day.setter
    def recalculation_rest_frequency_nth_day(self, recalculation_rest_frequency_nth_day):
        """Sets the recalculation_rest_frequency_nth_day of this LoanProductInterestRecalculationData.


        :param recalculation_rest_frequency_nth_day: The recalculation_rest_frequency_nth_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_rest_frequency_nth_day = recalculation_rest_frequency_nth_day

    @property
    def recalculation_rest_frequency_on_day(self):
        """Gets the recalculation_rest_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_rest_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: int
        """
        return self._recalculation_rest_frequency_on_day

    @recalculation_rest_frequency_on_day.setter
    def recalculation_rest_frequency_on_day(self, recalculation_rest_frequency_on_day):
        """Sets the recalculation_rest_frequency_on_day of this LoanProductInterestRecalculationData.


        :param recalculation_rest_frequency_on_day: The recalculation_rest_frequency_on_day of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: int
        """

        self._recalculation_rest_frequency_on_day = recalculation_rest_frequency_on_day

    @property
    def recalculation_rest_frequency_type(self):
        """Gets the recalculation_rest_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_rest_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_rest_frequency_type

    @recalculation_rest_frequency_type.setter
    def recalculation_rest_frequency_type(self, recalculation_rest_frequency_type):
        """Sets the recalculation_rest_frequency_type of this LoanProductInterestRecalculationData.


        :param recalculation_rest_frequency_type: The recalculation_rest_frequency_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_rest_frequency_type = recalculation_rest_frequency_type

    @property
    def recalculation_rest_frequency_weekday(self):
        """Gets the recalculation_rest_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The recalculation_rest_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._recalculation_rest_frequency_weekday

    @recalculation_rest_frequency_weekday.setter
    def recalculation_rest_frequency_weekday(self, recalculation_rest_frequency_weekday):
        """Sets the recalculation_rest_frequency_weekday of this LoanProductInterestRecalculationData.


        :param recalculation_rest_frequency_weekday: The recalculation_rest_frequency_weekday of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._recalculation_rest_frequency_weekday = recalculation_rest_frequency_weekday

    @property
    def reschedule_strategy_type(self):
        """Gets the reschedule_strategy_type of this LoanProductInterestRecalculationData.  # noqa: E501


        :return: The reschedule_strategy_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :rtype: EnumOptionData
        """
        return self._reschedule_strategy_type

    @reschedule_strategy_type.setter
    def reschedule_strategy_type(self, reschedule_strategy_type):
        """Sets the reschedule_strategy_type of this LoanProductInterestRecalculationData.


        :param reschedule_strategy_type: The reschedule_strategy_type of this LoanProductInterestRecalculationData.  # noqa: E501
        :type: EnumOptionData
        """

        self._reschedule_strategy_type = reschedule_strategy_type

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
        if issubclass(LoanProductInterestRecalculationData, dict):
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
        if not isinstance(other, LoanProductInterestRecalculationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
