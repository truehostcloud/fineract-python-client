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


class ReportMailingJobsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_report_mailing_job(self, body, **kwargs):  # noqa: E501
        """Create a Report Mailing Job  # noqa: E501

        Mandatory Fields: name, startDateTime, stretchyReportId, emailRecipients, emailSubject, emailMessage, emailAttachmentFileFormatId, recurrence, isActive  Optional Fields: description, stretchyReportParamMap  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_report_mailing_job(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostReportMailingJobsRequest body: (required)
        :return: PostReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_report_mailing_job_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_report_mailing_job_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_report_mailing_job_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Report Mailing Job  # noqa: E501

        Mandatory Fields: name, startDateTime, stretchyReportId, emailRecipients, emailSubject, emailMessage, emailAttachmentFileFormatId, recurrence, isActive  Optional Fields: description, stretchyReportParamMap  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_report_mailing_job_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostReportMailingJobsRequest body: (required)
        :return: PostReportMailingJobsResponse
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
                    " to method create_report_mailing_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_report_mailing_job`")  # noqa: E501

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
            '/v1/reportmailingjobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostReportMailingJobsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_report_mailing_job(self, body, entity_id, **kwargs):  # noqa: E501
        """Delete a Report Mailing Job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report_mailing_job(body, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteReportMailingJobsRequest body: (required)
        :param int entity_id: entityId (required)
        :return: DeleteReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_report_mailing_job_with_http_info(body, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_report_mailing_job_with_http_info(body, entity_id, **kwargs)  # noqa: E501
            return data

    def delete_report_mailing_job_with_http_info(self, body, entity_id, **kwargs):  # noqa: E501
        """Delete a Report Mailing Job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_report_mailing_job_with_http_info(body, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteReportMailingJobsRequest body: (required)
        :param int entity_id: entityId (required)
        :return: DeleteReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_report_mailing_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_report_mailing_job`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `delete_report_mailing_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

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
            '/v1/reportmailingjobs/{entityId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteReportMailingJobsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_all_report_mailing_jobs(self, **kwargs):  # noqa: E501
        """List Report Mailing Jobs  # noqa: E501

        Example Requests:  reportmailingjobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_report_mailing_jobs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: offset
        :param int limit: limit
        :param str order_by: orderBy
        :param str sort_order: sortOrder
        :return: list[GetReportMailingJobsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all_report_mailing_jobs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all_report_mailing_jobs_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_all_report_mailing_jobs_with_http_info(self, **kwargs):  # noqa: E501
        """List Report Mailing Jobs  # noqa: E501

        Example Requests:  reportmailingjobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all_report_mailing_jobs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: offset
        :param int limit: limit
        :param str order_by: orderBy
        :param str sort_order: sortOrder
        :return: list[GetReportMailingJobsResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'order_by', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_all_report_mailing_jobs" % key
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
            '/v1/reportmailingjobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetReportMailingJobsResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_report_mailing_job(self, entity_id, **kwargs):  # noqa: E501
        """Retrieve a Report Mailing Job  # noqa: E501

        Example Requests:  reportmailingjobs/1   reportmailingjobs/1?template=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_report_mailing_job(entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int entity_id: entityId (required)
        :return: GetReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_report_mailing_job_with_http_info(entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_report_mailing_job_with_http_info(entity_id, **kwargs)  # noqa: E501
            return data

    def retrieve_report_mailing_job_with_http_info(self, entity_id, **kwargs):  # noqa: E501
        """Retrieve a Report Mailing Job  # noqa: E501

        Example Requests:  reportmailingjobs/1   reportmailingjobs/1?template=true  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_report_mailing_job_with_http_info(entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int entity_id: entityId (required)
        :return: GetReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_report_mailing_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `retrieve_report_mailing_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

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
            '/v1/reportmailingjobs/{entityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetReportMailingJobsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_report_mailing_job_template(self, **kwargs):  # noqa: E501
        """Retrieve Report Mailing Job Details Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for report mailing job applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  reportmailingjobs/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_report_mailing_job_template(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetReportMailingJobsTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_report_mailing_job_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_report_mailing_job_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_report_mailing_job_template_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve Report Mailing Job Details Template  # noqa: E501

        This is a convenience resource. It can be useful when building maintenance user interface screens for report mailing job applications. The template data returned consists of any or all of:  Field Defaults Allowed description Lists Example Request:  reportmailingjobs/template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_report_mailing_job_template_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetReportMailingJobsTemplate
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
                    " to method retrieve_report_mailing_job_template" % key
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
            '/v1/reportmailingjobs/template', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetReportMailingJobsTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_report_mailing_job(self, body, entity_id, **kwargs):  # noqa: E501
        """Update a Report Mailing Job   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_report_mailing_job(body, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutReportMailingJobsRequest body: (required)
        :param int entity_id: entityId (required)
        :return: PutReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_report_mailing_job_with_http_info(body, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_report_mailing_job_with_http_info(body, entity_id, **kwargs)  # noqa: E501
            return data

    def update_report_mailing_job_with_http_info(self, body, entity_id, **kwargs):  # noqa: E501
        """Update a Report Mailing Job   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_report_mailing_job_with_http_info(body, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutReportMailingJobsRequest body: (required)
        :param int entity_id: entityId (required)
        :return: PutReportMailingJobsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_report_mailing_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_report_mailing_job`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `update_report_mailing_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

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
            '/v1/reportmailingjobs/{entityId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PutReportMailingJobsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
