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


class AccountingRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_accounting_rule(self, **kwargs):  # noqa: E501
        """Create/Define a Accounting rule  # noqa: E501

        Define a new Accounting rule.  Mandatory Fields name, officeId, accountToDebit OR debitTags, accountToCredit OR creditTags.  Optional Fields description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_accounting_rule(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAccountingRulesRequest body:
        :return: PostAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_accounting_rule_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_accounting_rule_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_accounting_rule_with_http_info(self, **kwargs):  # noqa: E501
        """Create/Define a Accounting rule  # noqa: E501

        Define a new Accounting rule.  Mandatory Fields name, officeId, accountToDebit OR debitTags, accountToCredit OR creditTags.  Optional Fields description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_accounting_rule_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostAccountingRulesRequest body:
        :return: PostAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_accounting_rule" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/accountingrules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostAccountingRulesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_accounting_rule(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Delete a Accounting Rule  # noqa: E501

        Deletes a Accounting rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_accounting_rule(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :return: DeleteAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
            return data

    def delete_accounting_rule_with_http_info(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Delete a Accounting Rule  # noqa: E501

        Deletes a Accounting rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_accounting_rule_with_http_info(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :return: DeleteAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accounting_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_accounting_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accounting_rule_id' is set
        if ('accounting_rule_id' not in params or
                params['accounting_rule_id'] is None):
            raise ValueError("Missing the required parameter `accounting_rule_id` when calling `delete_accounting_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'accounting_rule_id' in params:
            path_params['accountingRuleId'] = params['accounting_rule_id']  # noqa: E501

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
            '/v1/accountingrules/{accountingRuleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteAccountingRulesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retreive_accounting_rule(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Retrieve a Accounting rule  # noqa: E501

        Returns the details of a defined Accounting rule.  Example Requests:  accountingrules/1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retreive_accounting_rule(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :return: AccountingRuleData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retreive_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retreive_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
            return data

    def retreive_accounting_rule_with_http_info(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Retrieve a Accounting rule  # noqa: E501

        Returns the details of a defined Accounting rule.  Example Requests:  accountingrules/1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retreive_accounting_rule_with_http_info(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :return: AccountingRuleData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accounting_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retreive_accounting_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accounting_rule_id' is set
        if ('accounting_rule_id' not in params or
                params['accounting_rule_id'] is None):
            raise ValueError("Missing the required parameter `accounting_rule_id` when calling `retreive_accounting_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'accounting_rule_id' in params:
            path_params['accountingRuleId'] = params['accounting_rule_id']  # noqa: E501

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
            '/v1/accountingrules/{accountingRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountingRuleData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_all_accounting_rules(self, **kwargs):  # noqa: E501
        """Retrieve Accounting Rules  # noqa: E501

        Returns the list of defined accounting rules.  Example Requests:  accountingrules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_accounting_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetAccountRulesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all_accounting_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all_accounting_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_all_accounting_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve Accounting Rules  # noqa: E501

        Returns the list of defined accounting rules.  Example Requests:  accountingrules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_accounting_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetAccountRulesResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all_accounting_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/accountingrules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetAccountRulesResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_template1(self, **kwargs):  # noqa: E501
        """Retrieve Accounting Rule Details Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  accountingrules/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_template1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAccountRulesTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_template1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_template1_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_template1_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve Accounting Rule Details Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for client applications. The template data returned consists of any or all of:  Field Defaults Allowed Value Lists Example Request:  accountingrules/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_template1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetAccountRulesTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_template1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/accountingrules/template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAccountRulesTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_accounting_rule(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Update a Accounting Rule  # noqa: E501

        Updates the details of a Accounting rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_accounting_rule(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :param PutAccountingRulesRequest body:
        :return: PutAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_accounting_rule_with_http_info(accounting_rule_id, **kwargs)  # noqa: E501
            return data

    def update_accounting_rule_with_http_info(self, accounting_rule_id, **kwargs):  # noqa: E501
        """Update a Accounting Rule  # noqa: E501

        Updates the details of a Accounting rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_accounting_rule_with_http_info(accounting_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int accounting_rule_id: accountingRuleId (required)
        :param PutAccountingRulesRequest body:
        :return: PutAccountingRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accounting_rule_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_accounting_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accounting_rule_id' is set
        if ('accounting_rule_id' not in params or
                params['accounting_rule_id'] is None):
            raise ValueError("Missing the required parameter `accounting_rule_id` when calling `update_accounting_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'accounting_rule_id' in params:
            path_params['accountingRuleId'] = params['accounting_rule_id']  # noqa: E501

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
            '/v1/accountingrules/{accountingRuleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutAccountingRulesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
