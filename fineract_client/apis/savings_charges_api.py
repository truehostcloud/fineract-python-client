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


class SavingsChargesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_savings_account_charge(self, body, savings_account_id, **kwargs):  # noqa: E501
        """Create a Savings account Charge  # noqa: E501

        Creates a Savings account Charge  Mandatory Fields for Savings account Charges: chargeId, amount  chargeId, amount, dueDate, dateFormat, locale  chargeId, amount, feeOnMonthDay, monthDayFormat, locale  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_savings_account_charge(body, savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSavingsAccountsSavingsAccountIdChargesRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :return: PostSavingsAccountsSavingsAccountIdChargesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_savings_account_charge_with_http_info(body, savings_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_savings_account_charge_with_http_info(body, savings_account_id, **kwargs)  # noqa: E501
            return data

    def add_savings_account_charge_with_http_info(self, body, savings_account_id, **kwargs):  # noqa: E501
        """Create a Savings account Charge  # noqa: E501

        Creates a Savings account Charge  Mandatory Fields for Savings account Charges: chargeId, amount  chargeId, amount, dueDate, dateFormat, locale  chargeId, amount, feeOnMonthDay, monthDayFormat, locale  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_savings_account_charge_with_http_info(body, savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSavingsAccountsSavingsAccountIdChargesRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :return: PostSavingsAccountsSavingsAccountIdChargesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'savings_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_savings_account_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `add_savings_account_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/savingsaccounts/{savingsAccountId}/charges', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostSavingsAccountsSavingsAccountIdChargesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_savings_account_charge(self, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Delete a Savings account Charge  # noqa: E501

        Note: Currently, A Savings account Charge may only be removed from Savings that are not yet approved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_savings_account_charge(savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
            return data

    def delete_savings_account_charge_with_http_info(self, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Delete a Savings account Charge  # noqa: E501

        Note: Currently, A Savings account Charge may only be removed from Savings that are not yet approved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['savings_account_id', 'savings_account_charge_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_savings_account_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `delete_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_charge_id' is set
        if ('savings_account_charge_id' not in params or
                params['savings_account_charge_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_charge_id` when calling `delete_savings_account_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501
        if 'savings_account_charge_id' in params:
            path_params['savingsAccountChargeId'] = params['savings_account_charge_id']  # noqa: E501

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
            '/v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pay_or_waive_savings_account_charge(self, body, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Pay a Savings account Charge | Waive off a Savings account Charge | Inactivate a Savings account Charge  # noqa: E501

        Pay a Savings account Charge:  An active charge will be paid when savings account is active and having sufficient balance.  Waive off a Savings account Charge:  Outstanding charge amount will be waived off.  Inactivate a Savings account Charge:  A charge will be allowed to inactivate when savings account is active and not having any dues as of today. If charge is overpaid, corresponding charge payment transactions will be reversed.  Showing request/response for 'Pay a Savings account Charge'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_or_waive_savings_account_charge(body, savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :param str command: command
        :return: PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pay_or_waive_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pay_or_waive_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
            return data

    def pay_or_waive_savings_account_charge_with_http_info(self, body, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Pay a Savings account Charge | Waive off a Savings account Charge | Inactivate a Savings account Charge  # noqa: E501

        Pay a Savings account Charge:  An active charge will be paid when savings account is active and having sufficient balance.  Waive off a Savings account Charge:  Outstanding charge amount will be waived off.  Inactivate a Savings account Charge:  A charge will be allowed to inactivate when savings account is active and not having any dues as of today. If charge is overpaid, corresponding charge payment transactions will be reversed.  Showing request/response for 'Pay a Savings account Charge'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_or_waive_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :param str command: command
        :return: PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'savings_account_id', 'savings_account_charge_id', 'command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_or_waive_savings_account_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pay_or_waive_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `pay_or_waive_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_charge_id' is set
        if ('savings_account_charge_id' not in params or
                params['savings_account_charge_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_charge_id` when calling `pay_or_waive_savings_account_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501
        if 'savings_account_charge_id' in params:
            path_params['savingsAccountChargeId'] = params['savings_account_charge_id']  # noqa: E501

        query_params = []
        if 'command' in params:
            query_params.append(('command', params['command']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_all_savings_account_charges(self, savings_account_id, **kwargs):  # noqa: E501
        """List Savings Charges  # noqa: E501

        Lists Savings Charges  Example Requests:  savingsaccounts/1/charges  savingsaccounts/1/charges?chargeStatus=all  savingsaccounts/1/charges?chargeStatus=inactive  savingsaccounts/1/charges?chargeStatus=active  savingsaccounts/1/charges?fields=name,amountOrPercentage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_savings_account_charges(savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param str charge_status: chargeStatus
        :return: list[GetSavingsAccountsSavingsAccountIdChargesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all_savings_account_charges_with_http_info(savings_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all_savings_account_charges_with_http_info(savings_account_id, **kwargs)  # noqa: E501
            return data

    def retrieve_all_savings_account_charges_with_http_info(self, savings_account_id, **kwargs):  # noqa: E501
        """List Savings Charges  # noqa: E501

        Lists Savings Charges  Example Requests:  savingsaccounts/1/charges  savingsaccounts/1/charges?chargeStatus=all  savingsaccounts/1/charges?chargeStatus=inactive  savingsaccounts/1/charges?chargeStatus=active  savingsaccounts/1/charges?fields=name,amountOrPercentage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_savings_account_charges_with_http_info(savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param str charge_status: chargeStatus
        :return: list[GetSavingsAccountsSavingsAccountIdChargesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['savings_account_id', 'charge_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all_savings_account_charges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `retrieve_all_savings_account_charges`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501

        query_params = []
        if 'charge_status' in params:
            query_params.append(('chargeStatus', params['charge_status']))  # noqa: E501

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
            '/v1/savingsaccounts/{savingsAccountId}/charges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetSavingsAccountsSavingsAccountIdChargesResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_savings_account_charge(self, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Retrieve a Savings account Charge  # noqa: E501

        Retrieves a Savings account Charge  Example Requests:  /savingsaccounts/1/charges/5   /savingsaccounts/1/charges/5?fields=name,amountOrPercentage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_savings_account_charge(savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
            return data

    def retrieve_savings_account_charge_with_http_info(self, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Retrieve a Savings account Charge  # noqa: E501

        Retrieves a Savings account Charge  Example Requests:  /savingsaccounts/1/charges/5   /savingsaccounts/1/charges/5?fields=name,amountOrPercentage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_savings_account_charge_with_http_info(savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['savings_account_id', 'savings_account_charge_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_savings_account_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `retrieve_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_charge_id' is set
        if ('savings_account_charge_id' not in params or
                params['savings_account_charge_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_charge_id` when calling `retrieve_savings_account_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501
        if 'savings_account_charge_id' in params:
            path_params['savingsAccountChargeId'] = params['savings_account_charge_id']  # noqa: E501

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
            '/v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_template18(self, savings_account_id, **kwargs):  # noqa: E501
        """Retrieve Savings Charges Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  savingsaccounts/1/charges/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_template18(savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :return: GetSavingsAccountsSavingsAccountIdChargesTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_template18_with_http_info(savings_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_template18_with_http_info(savings_account_id, **kwargs)  # noqa: E501
            return data

    def retrieve_template18_with_http_info(self, savings_account_id, **kwargs):  # noqa: E501
        """Retrieve Savings Charges Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  savingsaccounts/1/charges/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_template18_with_http_info(savings_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int savings_account_id: savingsAccountId (required)
        :return: GetSavingsAccountsSavingsAccountIdChargesTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['savings_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_template18" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `retrieve_template18`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501

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
            '/v1/savingsaccounts/{savingsAccountId}/charges/template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSavingsAccountsSavingsAccountIdChargesTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_savings_account_charge(self, body, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Update a Savings account Charge  # noqa: E501

        Currently Savings account Charges may be updated only if the Savings account is not yet approved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_savings_account_charge(body, savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, **kwargs)  # noqa: E501
            return data

    def update_savings_account_charge_with_http_info(self, body, savings_account_id, savings_account_charge_id, **kwargs):  # noqa: E501
        """Update a Savings account Charge  # noqa: E501

        Currently Savings account Charges may be updated only if the Savings account is not yet approved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_savings_account_charge_with_http_info(body, savings_account_id, savings_account_charge_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest body: (required)
        :param int savings_account_id: savingsAccountId (required)
        :param int savings_account_charge_id: savingsAccountChargeId (required)
        :return: PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'savings_account_id', 'savings_account_charge_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_savings_account_charge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_id' is set
        if ('savings_account_id' not in params or
                params['savings_account_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_id` when calling `update_savings_account_charge`")  # noqa: E501
        # verify the required parameter 'savings_account_charge_id' is set
        if ('savings_account_charge_id' not in params or
                params['savings_account_charge_id'] is None):
            raise ValueError("Missing the required parameter `savings_account_charge_id` when calling `update_savings_account_charge`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'savings_account_id' in params:
            path_params['savingsAccountId'] = params['savings_account_id']  # noqa: E501
        if 'savings_account_charge_id' in params:
            path_params['savingsAccountChargeId'] = params['savings_account_charge_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/savingsaccounts/{savingsAccountId}/charges/{savingsAccountChargeId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
