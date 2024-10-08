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

class ExternalAssetOwnerTransferChangesData(object):
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
        'owner_external_id': 'str',
        'purchase_price_ratio': 'str',
        'settlement_date': 'date',
        'transfer_external_id': 'str'
    }

    attribute_map = {
        'owner_external_id': 'ownerExternalId',
        'purchase_price_ratio': 'purchasePriceRatio',
        'settlement_date': 'settlementDate',
        'transfer_external_id': 'transferExternalId'
    }

    def __init__(self, owner_external_id=None, purchase_price_ratio=None, settlement_date=None, transfer_external_id=None):  # noqa: E501
        """ExternalAssetOwnerTransferChangesData - a model defined in Swagger"""  # noqa: E501
        self._owner_external_id = None
        self._purchase_price_ratio = None
        self._settlement_date = None
        self._transfer_external_id = None
        self.discriminator = None
        if owner_external_id is not None:
            self.owner_external_id = owner_external_id
        if purchase_price_ratio is not None:
            self.purchase_price_ratio = purchase_price_ratio
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if transfer_external_id is not None:
            self.transfer_external_id = transfer_external_id

    @property
    def owner_external_id(self):
        """Gets the owner_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501


        :return: The owner_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :rtype: str
        """
        return self._owner_external_id

    @owner_external_id.setter
    def owner_external_id(self, owner_external_id):
        """Sets the owner_external_id of this ExternalAssetOwnerTransferChangesData.


        :param owner_external_id: The owner_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :type: str
        """

        self._owner_external_id = owner_external_id

    @property
    def purchase_price_ratio(self):
        """Gets the purchase_price_ratio of this ExternalAssetOwnerTransferChangesData.  # noqa: E501


        :return: The purchase_price_ratio of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :rtype: str
        """
        return self._purchase_price_ratio

    @purchase_price_ratio.setter
    def purchase_price_ratio(self, purchase_price_ratio):
        """Sets the purchase_price_ratio of this ExternalAssetOwnerTransferChangesData.


        :param purchase_price_ratio: The purchase_price_ratio of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :type: str
        """

        self._purchase_price_ratio = purchase_price_ratio

    @property
    def settlement_date(self):
        """Gets the settlement_date of this ExternalAssetOwnerTransferChangesData.  # noqa: E501


        :return: The settlement_date of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this ExternalAssetOwnerTransferChangesData.


        :param settlement_date: The settlement_date of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def transfer_external_id(self):
        """Gets the transfer_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501


        :return: The transfer_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :rtype: str
        """
        return self._transfer_external_id

    @transfer_external_id.setter
    def transfer_external_id(self, transfer_external_id):
        """Sets the transfer_external_id of this ExternalAssetOwnerTransferChangesData.


        :param transfer_external_id: The transfer_external_id of this ExternalAssetOwnerTransferChangesData.  # noqa: E501
        :type: str
        """

        self._transfer_external_id = transfer_external_id

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
        if issubclass(ExternalAssetOwnerTransferChangesData, dict):
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
        if not isinstance(other, ExternalAssetOwnerTransferChangesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
