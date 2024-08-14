# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.  # noqa: E501

    OpenAPI spec version: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fineract_client.api_client import ApiClient


class DepositAccountOnHoldFundTransactionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_all28(self, savings_id, **kwargs):  # noqa: E501
        """retrieve_all28  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all28(savings_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_id: (required)
        :param int guarantor_funding_id:
        :param int offset:
        :param int limit:
        :param str order_by:
        :param str sort_order:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all28_with_http_info(savings_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all28_with_http_info(savings_id, **kwargs)  # noqa: E501
            return data

    def retrieve_all28_with_http_info(self, savings_id, **kwargs):  # noqa: E501
        """retrieve_all28  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all28_with_http_info(savings_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_id: (required)
        :param int guarantor_funding_id:
        :param int offset:
        :param int limit:
        :param str order_by:
        :param str sort_order:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['savings_id', 'guarantor_funding_id', 'offset', 'limit', 'order_by', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all28" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'savings_id' is set
        if ('savings_id' not in params or
                params['savings_id'] is None):
            raise ValueError("Missing the required parameter `savings_id` when calling `retrieve_all28`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_id' in params:
            path_params['savingsId'] = params['savings_id']  # noqa: E501

        query_params = []
        if 'guarantor_funding_id' in params:
            query_params.append(('guarantorFundingId', params['guarantor_funding_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/savingsaccounts/{savingsId}/onholdtransactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
