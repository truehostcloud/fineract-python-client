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


class JournalEntriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_gl_journal_entry(self, **kwargs):  # noqa: E501
        """Create \"Balanced\" Journal Entries  # noqa: E501

        Note: A Balanced (simple) Journal entry would have atleast one \"Debit\" and one \"Credit\" entry whose amounts are equal  Compound Journal entries may have \"n\" debits and \"m\" credits where both \"m\" and \"n\" are greater than 0 and the net sum or all debits and credits are equal    Mandatory Fields officeId, transactionDate   credits- glAccountId, amount, comments    debits-  glAccountId, amount, comments    Optional Fields paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gl_journal_entry(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JournalEntryCommand body:
        :param str command: command
        :return: PostJournalEntriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_gl_journal_entry_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_gl_journal_entry_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_gl_journal_entry_with_http_info(self, **kwargs):  # noqa: E501
        """Create \"Balanced\" Journal Entries  # noqa: E501

        Note: A Balanced (simple) Journal entry would have atleast one \"Debit\" and one \"Credit\" entry whose amounts are equal  Compound Journal entries may have \"n\" debits and \"m\" credits where both \"m\" and \"n\" are greater than 0 and the net sum or all debits and credits are equal    Mandatory Fields officeId, transactionDate   credits- glAccountId, amount, comments    debits-  glAccountId, amount, comments    Optional Fields paymentTypeId, accountNumber, checkNumber, routingCode, receiptNumber, bankNumber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gl_journal_entry_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param JournalEntryCommand body:
        :param str command: command
        :return: PostJournalEntriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_gl_journal_entry" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/journalentries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostJournalEntriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_reversal_journal_entry(self, transaction_id, **kwargs):  # noqa: E501
        """Update Running balances for Journal Entries  # noqa: E501

        This API calculates the running balances for office. If office ID not provided this API calculates running balances for all offices.  Mandatory Fields officeId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_reversal_journal_entry(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: transactionId (required)
        :param PostJournalEntriesTransactionIdRequest body:
        :param str command: command
        :return: PostJournalEntriesTransactionIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_reversal_journal_entry_with_http_info(transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_reversal_journal_entry_with_http_info(transaction_id, **kwargs)  # noqa: E501
            return data

    def create_reversal_journal_entry_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """Update Running balances for Journal Entries  # noqa: E501

        This API calculates the running balances for office. If office ID not provided this API calculates running balances for all offices.  Mandatory Fields officeId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_reversal_journal_entry_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_id: transactionId (required)
        :param PostJournalEntriesTransactionIdRequest body:
        :param str command: command
        :return: PostJournalEntriesTransactionIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id', 'body', 'command']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_reversal_journal_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `create_reversal_journal_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']  # noqa: E501

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
            '/v1/journalentries/{transactionId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostJournalEntriesTransactionIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_journal_entries_template(self, **kwargs):  # noqa: E501
        """get_journal_entries_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_entries_template(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id:
        :param str date_format:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_journal_entries_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_journal_entries_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_journal_entries_template_with_http_info(self, **kwargs):  # noqa: E501
        """get_journal_entries_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_entries_template_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id:
        :param str date_format:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'date_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journal_entries_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'office_id' in params:
            query_params.append(('officeId', params['office_id']))  # noqa: E501
        if 'date_format' in params:
            query_params.append(('dateFormat', params['date_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.ms-excel'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/journalentries/downloadtemplate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_journal_entries_template(self, **kwargs):  # noqa: E501
        """post_journal_entries_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_journal_entries_template(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str date_format:
        :param str locale:
        :param str uploaded_input_stream:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_journal_entries_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_journal_entries_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_journal_entries_template_with_http_info(self, **kwargs):  # noqa: E501
        """post_journal_entries_template  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_journal_entries_template_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str date_format:
        :param str locale:
        :param str uploaded_input_stream:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_format', 'locale', 'uploaded_input_stream']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_journal_entries_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'date_format' in params:
            form_params.append(('dateFormat', params['date_format']))  # noqa: E501
        if 'locale' in params:
            form_params.append(('locale', params['locale']))  # noqa: E501
        if 'uploaded_input_stream' in params:
            local_var_files['uploadedInputStream'] = params['uploaded_input_stream']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tenantid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/journalentries/uploadtemplate', 'POST',
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

    def retrieve_all1(self, **kwargs):  # noqa: E501
        """List Journal Entries  # noqa: E501

        The list capability of journal entries can support pagination and sorting.  Example Requests:  journalentries  journalentries?transactionId=PB37X8Y21EQUY4S  journalentries?officeId=1&manualEntriesOnly=true&fromDate=1 July 2013&toDate=15 July 2013&dateFormat=dd MMMM yyyy&locale=en  journalentries?fields=officeName,glAccountName,transactionDate  journalentries?offset=10&limit=50  journalentries?orderBy=transactionId&sortOrder=DESC  journalentries?runningBalance=true  journalentries?transactionDetails=true  journalentries?loanId=12  journalentries?savingsId=24  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id: officeId
        :param int gl_account_id: glAccountId
        :param bool manual_entries_only: manualEntriesOnly
        :param DateParam from_date: fromDate
        :param DateParam to_date: toDate
        :param DateParam submitted_on_date_from: submittedOnDateFrom
        :param DateParam submitted_on_date_to: submittedOnDateTo
        :param str transaction_id: transactionId
        :param int entity_type: entityType
        :param int offset: offset
        :param int limit: limit
        :param str order_by: orderBy
        :param str sort_order: sortOrder
        :param str locale: locale
        :param str date_format: dateFormat
        :param int loan_id: loanId
        :param int savings_id: savingsId
        :param bool running_balance: runningBalance
        :param bool transaction_details: transactionDetails
        :return: GetJournalEntriesTransactionIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all1_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_all1_with_http_info(self, **kwargs):  # noqa: E501
        """List Journal Entries  # noqa: E501

        The list capability of journal entries can support pagination and sorting.  Example Requests:  journalentries  journalentries?transactionId=PB37X8Y21EQUY4S  journalentries?officeId=1&manualEntriesOnly=true&fromDate=1 July 2013&toDate=15 July 2013&dateFormat=dd MMMM yyyy&locale=en  journalentries?fields=officeName,glAccountName,transactionDate  journalentries?offset=10&limit=50  journalentries?orderBy=transactionId&sortOrder=DESC  journalentries?runningBalance=true  journalentries?transactionDetails=true  journalentries?loanId=12  journalentries?savingsId=24  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id: officeId
        :param int gl_account_id: glAccountId
        :param bool manual_entries_only: manualEntriesOnly
        :param DateParam from_date: fromDate
        :param DateParam to_date: toDate
        :param DateParam submitted_on_date_from: submittedOnDateFrom
        :param DateParam submitted_on_date_to: submittedOnDateTo
        :param str transaction_id: transactionId
        :param int entity_type: entityType
        :param int offset: offset
        :param int limit: limit
        :param str order_by: orderBy
        :param str sort_order: sortOrder
        :param str locale: locale
        :param str date_format: dateFormat
        :param int loan_id: loanId
        :param int savings_id: savingsId
        :param bool running_balance: runningBalance
        :param bool transaction_details: transactionDetails
        :return: GetJournalEntriesTransactionIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'gl_account_id', 'manual_entries_only', 'from_date', 'to_date', 'submitted_on_date_from', 'submitted_on_date_to', 'transaction_id', 'entity_type', 'offset', 'limit', 'order_by', 'sort_order', 'locale', 'date_format', 'loan_id', 'savings_id', 'running_balance', 'transaction_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'office_id' in params:
            query_params.append(('officeId', params['office_id']))  # noqa: E501
        if 'gl_account_id' in params:
            query_params.append(('glAccountId', params['gl_account_id']))  # noqa: E501
        if 'manual_entries_only' in params:
            query_params.append(('manualEntriesOnly', params['manual_entries_only']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'submitted_on_date_from' in params:
            query_params.append(('submittedOnDateFrom', params['submitted_on_date_from']))  # noqa: E501
        if 'submitted_on_date_to' in params:
            query_params.append(('submittedOnDateTo', params['submitted_on_date_to']))  # noqa: E501
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))  # noqa: E501
        if 'entity_type' in params:
            query_params.append(('entityType', params['entity_type']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'locale' in params:
            query_params.append(('locale', params['locale']))  # noqa: E501
        if 'date_format' in params:
            query_params.append(('dateFormat', params['date_format']))  # noqa: E501
        if 'loan_id' in params:
            query_params.append(('loanId', params['loan_id']))  # noqa: E501
        if 'savings_id' in params:
            query_params.append(('savingsId', params['savings_id']))  # noqa: E501
        if 'running_balance' in params:
            query_params.append(('runningBalance', params['running_balance']))  # noqa: E501
        if 'transaction_details' in params:
            query_params.append(('transactionDetails', params['transaction_details']))  # noqa: E501

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
            '/v1/journalentries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetJournalEntriesTransactionIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_journal_entries(self, **kwargs):  # noqa: E501
        """retrieve_journal_entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_journal_entries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :param int entry_id:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_journal_entries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_journal_entries_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_journal_entries_with_http_info(self, **kwargs):  # noqa: E501
        """retrieve_journal_entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_journal_entries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :param int entry_id:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'entry_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_journal_entries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'entry_id' in params:
            query_params.append(('entryId', params['entry_id']))  # noqa: E501

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
            '/v1/journalentries/provisioning', 'GET',
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

    def retrieve_journal_entry_by_id(self, journal_entry_id, **kwargs):  # noqa: E501
        """Retrieve a single Entry  # noqa: E501

        Example Requests:  journalentries/1    journalentries/1?fields=officeName,glAccountId,entryType,amount  journalentries/1?runningBalance=true  journalentries/1?transactionDetails=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_journal_entry_by_id(journal_entry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int journal_entry_id: journalEntryId (required)
        :param bool running_balance: runningBalance
        :param bool transaction_details: transactionDetails
        :return: JournalEntryTransactionItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_journal_entry_by_id_with_http_info(journal_entry_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_journal_entry_by_id_with_http_info(journal_entry_id, **kwargs)  # noqa: E501
            return data

    def retrieve_journal_entry_by_id_with_http_info(self, journal_entry_id, **kwargs):  # noqa: E501
        """Retrieve a single Entry  # noqa: E501

        Example Requests:  journalentries/1    journalentries/1?fields=officeName,glAccountId,entryType,amount  journalentries/1?runningBalance=true  journalentries/1?transactionDetails=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_journal_entry_by_id_with_http_info(journal_entry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int journal_entry_id: journalEntryId (required)
        :param bool running_balance: runningBalance
        :param bool transaction_details: transactionDetails
        :return: JournalEntryTransactionItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['journal_entry_id', 'running_balance', 'transaction_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_journal_entry_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'journal_entry_id' is set
        if ('journal_entry_id' not in params or
                params['journal_entry_id'] is None):
            raise ValueError("Missing the required parameter `journal_entry_id` when calling `retrieve_journal_entry_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'journal_entry_id' in params:
            path_params['journalEntryId'] = params['journal_entry_id']  # noqa: E501

        query_params = []
        if 'running_balance' in params:
            query_params.append(('runningBalance', params['running_balance']))  # noqa: E501
        if 'transaction_details' in params:
            query_params.append(('transactionDetails', params['transaction_details']))  # noqa: E501

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
            '/v1/journalentries/{journalEntryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JournalEntryTransactionItem',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_opening_balance(self, **kwargs):  # noqa: E501
        """retrieve_opening_balance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_opening_balance(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id:
        :param str currency_code:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_opening_balance_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_opening_balance_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_opening_balance_with_http_info(self, **kwargs):  # noqa: E501
        """retrieve_opening_balance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_opening_balance_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int office_id:
        :param str currency_code:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office_id', 'currency_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_opening_balance" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'office_id' in params:
            query_params.append(('officeId', params['office_id']))  # noqa: E501
        if 'currency_code' in params:
            query_params.append(('currencyCode', params['currency_code']))  # noqa: E501

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
            '/v1/journalentries/openingbalance', 'GET',
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
