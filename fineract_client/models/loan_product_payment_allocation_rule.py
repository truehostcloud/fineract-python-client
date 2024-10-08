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

class LoanProductPaymentAllocationRule(object):
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
        'allocation_types': 'list[str]',
        'created_by': 'int',
        'created_date': 'datetime',
        'created_date_time': 'datetime',
        'future_installment_allocation_rule': 'str',
        'id': 'int',
        'last_modified_by': 'int',
        'last_modified_date': 'datetime',
        'last_modified_date_time': 'datetime',
        'loan_product': 'LoanProduct',
        'new': 'bool',
        'transaction_type': 'str'
    }

    attribute_map = {
        'allocation_types': 'allocationTypes',
        'created_by': 'createdBy',
        'created_date': 'createdDate',
        'created_date_time': 'createdDateTime',
        'future_installment_allocation_rule': 'futureInstallmentAllocationRule',
        'id': 'id',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_date': 'lastModifiedDate',
        'last_modified_date_time': 'lastModifiedDateTime',
        'loan_product': 'loanProduct',
        'new': 'new',
        'transaction_type': 'transactionType'
    }

    def __init__(self, allocation_types=None, created_by=None, created_date=None, created_date_time=None, future_installment_allocation_rule=None, id=None, last_modified_by=None, last_modified_date=None, last_modified_date_time=None, loan_product=None, new=None, transaction_type=None):  # noqa: E501
        """LoanProductPaymentAllocationRule - a model defined in Swagger"""  # noqa: E501
        self._allocation_types = None
        self._created_by = None
        self._created_date = None
        self._created_date_time = None
        self._future_installment_allocation_rule = None
        self._id = None
        self._last_modified_by = None
        self._last_modified_date = None
        self._last_modified_date_time = None
        self._loan_product = None
        self._new = None
        self._transaction_type = None
        self.discriminator = None
        if allocation_types is not None:
            self.allocation_types = allocation_types
        self.created_by = created_by
        self.created_date = created_date
        self.created_date_time = created_date_time
        if future_installment_allocation_rule is not None:
            self.future_installment_allocation_rule = future_installment_allocation_rule
        if id is not None:
            self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        self.last_modified_date_time = last_modified_date_time
        if loan_product is not None:
            self.loan_product = loan_product
        if new is not None:
            self.new = new
        if transaction_type is not None:
            self.transaction_type = transaction_type

    @property
    def allocation_types(self):
        """Gets the allocation_types of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The allocation_types of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._allocation_types

    @allocation_types.setter
    def allocation_types(self, allocation_types):
        """Sets the allocation_types of this LoanProductPaymentAllocationRule.


        :param allocation_types: The allocation_types of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["PAST_DUE_PENALTY", "PAST_DUE_FEE", "PAST_DUE_PRINCIPAL", "PAST_DUE_INTEREST", "DUE_PENALTY", "DUE_FEE", "DUE_PRINCIPAL", "DUE_INTEREST", "IN_ADVANCE_PENALTY", "IN_ADVANCE_FEE", "IN_ADVANCE_PRINCIPAL", "IN_ADVANCE_INTEREST"]  # noqa: E501
        if not set(allocation_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allocation_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allocation_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allocation_types = allocation_types

    @property
    def created_by(self):
        """Gets the created_by of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The created_by of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this LoanProductPaymentAllocationRule.


        :param created_by: The created_by of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: int
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_date(self):
        """Gets the created_date of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The created_date of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this LoanProductPaymentAllocationRule.


        :param created_date: The created_date of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: datetime
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def created_date_time(self):
        """Gets the created_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The created_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this LoanProductPaymentAllocationRule.


        :param created_date_time: The created_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: datetime
        """
        if created_date_time is None:
            raise ValueError("Invalid value for `created_date_time`, must not be `None`")  # noqa: E501

        self._created_date_time = created_date_time

    @property
    def future_installment_allocation_rule(self):
        """Gets the future_installment_allocation_rule of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The future_installment_allocation_rule of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: str
        """
        return self._future_installment_allocation_rule

    @future_installment_allocation_rule.setter
    def future_installment_allocation_rule(self, future_installment_allocation_rule):
        """Sets the future_installment_allocation_rule of this LoanProductPaymentAllocationRule.


        :param future_installment_allocation_rule: The future_installment_allocation_rule of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEXT_INSTALLMENT", "LAST_INSTALLMENT", "REAMORTIZATION"]  # noqa: E501
        if future_installment_allocation_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `future_installment_allocation_rule` ({0}), must be one of {1}"  # noqa: E501
                .format(future_installment_allocation_rule, allowed_values)
            )

        self._future_installment_allocation_rule = future_installment_allocation_rule

    @property
    def id(self):
        """Gets the id of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The id of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoanProductPaymentAllocationRule.


        :param id: The id of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The last_modified_by of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this LoanProductPaymentAllocationRule.


        :param last_modified_by: The last_modified_by of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: int
        """
        if last_modified_by is None:
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501

        self._last_modified_by = last_modified_by

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The last_modified_date of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this LoanProductPaymentAllocationRule.


        :param last_modified_date: The last_modified_date of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: datetime
        """
        if last_modified_date is None:
            raise ValueError("Invalid value for `last_modified_date`, must not be `None`")  # noqa: E501

        self._last_modified_date = last_modified_date

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The last_modified_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this LoanProductPaymentAllocationRule.


        :param last_modified_date_time: The last_modified_date_time of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def loan_product(self):
        """Gets the loan_product of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The loan_product of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: LoanProduct
        """
        return self._loan_product

    @loan_product.setter
    def loan_product(self, loan_product):
        """Sets the loan_product of this LoanProductPaymentAllocationRule.


        :param loan_product: The loan_product of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: LoanProduct
        """

        self._loan_product = loan_product

    @property
    def new(self):
        """Gets the new of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The new of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this LoanProductPaymentAllocationRule.


        :param new: The new of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: bool
        """

        self._new = new

    @property
    def transaction_type(self):
        """Gets the transaction_type of this LoanProductPaymentAllocationRule.  # noqa: E501


        :return: The transaction_type of this LoanProductPaymentAllocationRule.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this LoanProductPaymentAllocationRule.


        :param transaction_type: The transaction_type of this LoanProductPaymentAllocationRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "REPAYMENT", "DOWN_PAYMENT", "MERCHANT_ISSUED_REFUND", "PAYOUT_REFUND", "GOODWILL_CREDIT", "CHARGE_REFUND", "CHARGE_ADJUSTMENT", "WAIVE_INTEREST", "CHARGE_PAYMENT", "REFUND_FOR_ACTIVE_LOAN", "INTEREST_PAYMENT_WAIVER", "INTEREST_REFUND"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

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
        if issubclass(LoanProductPaymentAllocationRule, dict):
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
        if not isinstance(other, LoanProductPaymentAllocationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
