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


class SurveyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_datatable_entry1(self, body, survey_name, apptable_id, **kwargs):  # noqa: E501
        """Create an entry in the survey table  # noqa: E501

        Insert and entry in a survey table (full fill the survey).  Refer Link for sample Body:  [ https://fineract.apache.org/legacy-docs/apiLive.htm#survey_create ]   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_datatable_entry1(body, survey_name, apptable_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSurveySurveyNameApptableIdRequest body: (required)
        :param str survey_name: surveyName (required)
        :param int apptable_id: apptableId (required)
        :return: PostSurveySurveyNameApptableIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_datatable_entry1_with_http_info(body, survey_name, apptable_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_datatable_entry1_with_http_info(body, survey_name, apptable_id, **kwargs)  # noqa: E501
            return data

    def create_datatable_entry1_with_http_info(self, body, survey_name, apptable_id, **kwargs):  # noqa: E501
        """Create an entry in the survey table  # noqa: E501

        Insert and entry in a survey table (full fill the survey).  Refer Link for sample Body:  [ https://fineract.apache.org/legacy-docs/apiLive.htm#survey_create ]   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_datatable_entry1_with_http_info(body, survey_name, apptable_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostSurveySurveyNameApptableIdRequest body: (required)
        :param str survey_name: surveyName (required)
        :param int apptable_id: apptableId (required)
        :return: PostSurveySurveyNameApptableIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'survey_name', 'apptable_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_datatable_entry1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_datatable_entry1`")  # noqa: E501
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `create_datatable_entry1`")  # noqa: E501
        # verify the required parameter 'apptable_id' is set
        if ('apptable_id' not in params or
                params['apptable_id'] is None):
            raise ValueError("Missing the required parameter `apptable_id` when calling `create_datatable_entry1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501
        if 'apptable_id' in params:
            path_params['apptableId'] = params['apptable_id']  # noqa: E501

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
            '/v1/survey/{surveyName}/{apptableId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostSurveySurveyNameApptableIdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_datatable_entries1(self, survey_name, client_id, fulfilled_id, **kwargs):  # noqa: E501
        """delete_datatable_entries1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_datatable_entries1(survey_name, client_id, fulfilled_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :param int fulfilled_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_datatable_entries1_with_http_info(survey_name, client_id, fulfilled_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_datatable_entries1_with_http_info(survey_name, client_id, fulfilled_id, **kwargs)  # noqa: E501
            return data

    def delete_datatable_entries1_with_http_info(self, survey_name, client_id, fulfilled_id, **kwargs):  # noqa: E501
        """delete_datatable_entries1  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_datatable_entries1_with_http_info(survey_name, client_id, fulfilled_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :param int fulfilled_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['survey_name', 'client_id', 'fulfilled_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_datatable_entries1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `delete_datatable_entries1`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `delete_datatable_entries1`")  # noqa: E501
        # verify the required parameter 'fulfilled_id' is set
        if ('fulfilled_id' not in params or
                params['fulfilled_id'] is None):
            raise ValueError("Missing the required parameter `fulfilled_id` when calling `delete_datatable_entries1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'fulfilled_id' in params:
            path_params['fulfilledId'] = params['fulfilled_id']  # noqa: E501

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
            '/v1/survey/{surveyName}/{clientId}/{fulfilledId}', 'DELETE',
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

    def get_client_survey_overview(self, survey_name, client_id, **kwargs):  # noqa: E501
        """get_client_survey_overview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_survey_overview(survey_name, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_client_survey_overview_with_http_info(survey_name, client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_client_survey_overview_with_http_info(survey_name, client_id, **kwargs)  # noqa: E501
            return data

    def get_client_survey_overview_with_http_info(self, survey_name, client_id, **kwargs):  # noqa: E501
        """get_client_survey_overview  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_survey_overview_with_http_info(survey_name, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['survey_name', 'client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client_survey_overview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `get_client_survey_overview`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `get_client_survey_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

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
            '/v1/survey/{surveyName}/{clientId}', 'GET',
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

    def get_survey_entry(self, survey_name, client_id, entry_id, **kwargs):  # noqa: E501
        """get_survey_entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_survey_entry(survey_name, client_id, entry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :param int entry_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_survey_entry_with_http_info(survey_name, client_id, entry_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_survey_entry_with_http_info(survey_name, client_id, entry_id, **kwargs)  # noqa: E501
            return data

    def get_survey_entry_with_http_info(self, survey_name, client_id, entry_id, **kwargs):  # noqa: E501
        """get_survey_entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_survey_entry_with_http_info(survey_name, client_id, entry_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param int client_id: (required)
        :param int entry_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['survey_name', 'client_id', 'entry_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_survey_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `get_survey_entry`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `get_survey_entry`")  # noqa: E501
        # verify the required parameter 'entry_id' is set
        if ('entry_id' not in params or
                params['entry_id'] is None):
            raise ValueError("Missing the required parameter `entry_id` when calling `get_survey_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'entry_id' in params:
            path_params['entryId'] = params['entry_id']  # noqa: E501

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
            '/v1/survey/{surveyName}/{clientId}/{entryId}', 'GET',
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

    def register(self, survey_name, apptable, **kwargs):  # noqa: E501
        """register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register(survey_name, apptable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param str apptable: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_with_http_info(survey_name, apptable, **kwargs)  # noqa: E501
        else:
            (data) = self.register_with_http_info(survey_name, apptable, **kwargs)  # noqa: E501
            return data

    def register_with_http_info(self, survey_name, apptable, **kwargs):  # noqa: E501
        """register  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_with_http_info(survey_name, apptable, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: (required)
        :param str apptable: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['survey_name', 'apptable', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `register`")  # noqa: E501
        # verify the required parameter 'apptable' is set
        if ('apptable' not in params or
                params['apptable'] is None):
            raise ValueError("Missing the required parameter `apptable` when calling `register`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501
        if 'apptable' in params:
            path_params['apptable'] = params['apptable']  # noqa: E501

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
            '/v1/survey/register/{surveyName}/{apptable}', 'PUT',
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

    def retrieve_survey(self, survey_name, **kwargs):  # noqa: E501
        """Retrieve survey  # noqa: E501

        Lists a registered survey table details and the Apache Fineract Core application table they are registered to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_survey(survey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: surveyName (required)
        :return: GetSurveyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_survey_with_http_info(survey_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_survey_with_http_info(survey_name, **kwargs)  # noqa: E501
            return data

    def retrieve_survey_with_http_info(self, survey_name, **kwargs):  # noqa: E501
        """Retrieve survey  # noqa: E501

        Lists a registered survey table details and the Apache Fineract Core application table they are registered to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_survey_with_http_info(survey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str survey_name: surveyName (required)
        :return: GetSurveyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['survey_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_survey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'survey_name' is set
        if ('survey_name' not in params or
                params['survey_name'] is None):
            raise ValueError("Missing the required parameter `survey_name` when calling `retrieve_survey`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'survey_name' in params:
            path_params['surveyName'] = params['survey_name']  # noqa: E501

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
            '/v1/survey/{surveyName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSurveyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_surveys(self, **kwargs):  # noqa: E501
        """Retrieve surveys  # noqa: E501

        Retrieve surveys. This allows to retrieve the list of survey tables registered .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_surveys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetSurveyResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_surveys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_surveys_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_surveys_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve surveys  # noqa: E501

        Retrieve surveys. This allows to retrieve the list of survey tables registered .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_surveys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[GetSurveyResponse]
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
                    " to method retrieve_surveys" % key
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
            '/v1/survey', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetSurveyResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
