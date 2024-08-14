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


class FineractEntityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_map(self, rel_id, **kwargs):  # noqa: E501
        """create_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_map(rel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int rel_id: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_map_with_http_info(rel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_map_with_http_info(rel_id, **kwargs)  # noqa: E501
            return data

    def create_map_with_http_info(self, rel_id, **kwargs):  # noqa: E501
        """create_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_map_with_http_info(rel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int rel_id: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rel_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rel_id' is set
        if ('rel_id' not in params or
                params['rel_id'] is None):
            raise ValueError("Missing the required parameter `rel_id` when calling `create_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rel_id' in params:
            path_params['relId'] = params['rel_id']  # noqa: E501

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
            '/v1/entitytoentitymapping/{relId}', 'POST',
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

    def delete4(self, map_id, **kwargs):  # noqa: E501
        """delete4  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete4(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete4_with_http_info(map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete4_with_http_info(map_id, **kwargs)  # noqa: E501
            return data

    def delete4_with_http_info(self, map_id, **kwargs):  # noqa: E501
        """delete4  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete4_with_http_info(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete4" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `delete4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501

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
            '/v1/entitytoentitymapping/{mapId}', 'DELETE',
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

    def get_entity_to_entity_mappings(self, map_id, from_id, to_id, **kwargs):  # noqa: E501
        """get_entity_to_entity_mappings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_to_entity_mappings(map_id, from_id, to_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :param int from_id: (required)
        :param int to_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity_to_entity_mappings_with_http_info(map_id, from_id, to_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_to_entity_mappings_with_http_info(map_id, from_id, to_id, **kwargs)  # noqa: E501
            return data

    def get_entity_to_entity_mappings_with_http_info(self, map_id, from_id, to_id, **kwargs):  # noqa: E501
        """get_entity_to_entity_mappings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_to_entity_mappings_with_http_info(map_id, from_id, to_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :param int from_id: (required)
        :param int to_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'from_id', 'to_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity_to_entity_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `get_entity_to_entity_mappings`")  # noqa: E501
        # verify the required parameter 'from_id' is set
        if ('from_id' not in params or
                params['from_id'] is None):
            raise ValueError("Missing the required parameter `from_id` when calling `get_entity_to_entity_mappings`")  # noqa: E501
        # verify the required parameter 'to_id' is set
        if ('to_id' not in params or
                params['to_id'] is None):
            raise ValueError("Missing the required parameter `to_id` when calling `get_entity_to_entity_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501
        if 'from_id' in params:
            path_params['fromId'] = params['from_id']  # noqa: E501
        if 'to_id' in params:
            path_params['toId'] = params['to_id']  # noqa: E501

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
            '/v1/entitytoentitymapping/{mapId}/{fromId}/{toId}', 'GET',
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

    def retrieve_all7(self, **kwargs):  # noqa: E501
        """retrieve_all7  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all7(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_all7_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_all7_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_all7_with_http_info(self, **kwargs):  # noqa: E501
        """retrieve_all7  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_all7_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
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
                    " to method retrieve_all7" % key
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
            '/v1/entitytoentitymapping', 'GET',
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

    def retrieve_one4(self, map_id, **kwargs):  # noqa: E501
        """retrieve_one4  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_one4(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_one4_with_http_info(map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_one4_with_http_info(map_id, **kwargs)  # noqa: E501
            return data

    def retrieve_one4_with_http_info(self, map_id, **kwargs):  # noqa: E501
        """retrieve_one4  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_one4_with_http_info(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_one4" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `retrieve_one4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501

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
            '/v1/entitytoentitymapping/{mapId}', 'GET',
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

    def update_map(self, map_id, **kwargs):  # noqa: E501
        """update_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_map(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_map_with_http_info(map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_map_with_http_info(map_id, **kwargs)  # noqa: E501
            return data

    def update_map_with_http_info(self, map_id, **kwargs):  # noqa: E501
        """update_map  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_map_with_http_info(map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int map_id: (required)
        :param str body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['map_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_map" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'map_id' is set
        if ('map_id' not in params or
                params['map_id'] is None):
            raise ValueError("Missing the required parameter `map_id` when calling `update_map`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['mapId'] = params['map_id']  # noqa: E501

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
            '/v1/entitytoentitymapping/{mapId}', 'PUT',
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
