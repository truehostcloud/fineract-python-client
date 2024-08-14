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


class LoanCollateralManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_loan_collateral(self, loan_id, id, **kwargs):  # noqa: E501
        """Delete Loan Collateral  # noqa: E501

        Delete Loan Collateral  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_loan_collateral(loan_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int loan_id: loanId (required)
        :param int id: loan collateral id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_loan_collateral_with_http_info(loan_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_loan_collateral_with_http_info(loan_id, id, **kwargs)  # noqa: E501
            return data

    def delete_loan_collateral_with_http_info(self, loan_id, id, **kwargs):  # noqa: E501
        """Delete Loan Collateral  # noqa: E501

        Delete Loan Collateral  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_loan_collateral_with_http_info(loan_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int loan_id: loanId (required)
        :param int id: loan collateral id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['loan_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_loan_collateral" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'loan_id' is set
        if ('loan_id' not in params or
                params['loan_id'] is None):
            raise ValueError("Missing the required parameter `loan_id` when calling `delete_loan_collateral`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_loan_collateral`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'loan_id' in params:
            path_params['loanId'] = params['loan_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/loan-collateral-management/{id}', 'DELETE',
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

    def get_loan_collateral(self, collateral_id, **kwargs):  # noqa: E501
        """Get Loan Collateral Details  # noqa: E501

        Get Loan Collateral Details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loan_collateral(collateral_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int collateral_id: collateralId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_loan_collateral_with_http_info(collateral_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_loan_collateral_with_http_info(collateral_id, **kwargs)  # noqa: E501
            return data

    def get_loan_collateral_with_http_info(self, collateral_id, **kwargs):  # noqa: E501
        """Get Loan Collateral Details  # noqa: E501

        Get Loan Collateral Details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loan_collateral_with_http_info(collateral_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int collateral_id: collateralId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collateral_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_loan_collateral" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collateral_id' is set
        if ('collateral_id' not in params or
                params['collateral_id'] is None):
            raise ValueError("Missing the required parameter `collateral_id` when calling `get_loan_collateral`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collateral_id' in params:
            path_params['collateralId'] = params['collateral_id']  # noqa: E501

        query_params = []

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
            '/v1/loan-collateral-management/{collateralId}', 'GET',
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
